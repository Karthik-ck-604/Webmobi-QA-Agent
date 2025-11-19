"""
Helper script to find the correct selector for the "Create Event" button.
This script will log in and then pause, allowing you to inspect the page.
"""

import os
import time
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

if not email or not password:
    print("❌ Please set EMAIL and PASSWORD in .env file")
    exit(1)

print("🔍 Button Selector Finder")
print("=" * 60)
print("This script will log in and then pause so you can inspect the page.")
print("Open browser DevTools (F12) to find the button selector.")
print("=" * 60)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    
    try:
        # Navigate and login
        print("\n📍 Navigating to https://events.webmobi.com...")
        page.goto('https://events.webmobi.com')
        page.wait_for_load_state('networkidle')
        
        print("🔐 Logging in...")
        email_input = page.locator('input[type="email"], input[name="email"], input[id="email"]').first
        password_input = page.locator('input[type="password"], input[name="password"], input[id="password"]').first
        login_button = page.locator('button[type="submit"], button:has-text("Log in"), button:has-text("Login")').first
        
        email_input.fill(email)
        password_input.fill(password)
        login_button.click()
        
        page.wait_for_load_state('networkidle')
        time.sleep(3)
        print("✅ Logged in successfully")
        
        # Find all buttons and links
        print("\n🔍 Analyzing page for buttons and links...")
        print("=" * 60)
        
        buttons = page.locator('button, a[href], [role="button"]').all()
        print(f"\nFound {len(buttons)} buttons/links. Showing first 30:\n")
        
        for i, btn in enumerate(buttons[:30], 1):
            try:
                text = btn.inner_text(timeout=10000)
                is_visible = btn.is_visible(timeout=10000)
                
                # Try to get attributes
                try:
                    btn_id = btn.get_attribute('id') or ''
                    btn_class = btn.get_attribute('class') or ''
                    btn_data_testid = btn.get_attribute('data-testid') or ''
                except:
                    btn_id = ''
                    btn_class = ''
                    btn_data_testid = ''
                
                if 'create' in text.lower() or 'new' in text.lower() or 'add' in text.lower() or is_visible:
                    marker = "⭐" if ('create' in text.lower() or 'new' in text.lower() or 'add' in text.lower()) else "  "
                    print(f"{marker} {i}. Text: '{text[:60]}'")
                    if btn_id:
                        print(f"      ID: {btn_id}")
                    if btn_class:
                        print(f"      Class: {btn_class[:60]}")
                    if btn_data_testid:
                        print(f"      data-testid: {btn_data_testid}")
                    print(f"      Visible: {is_visible}")
                    print()
            except:
                pass
        
        print("=" * 60)
        print("\n⏸️  Browser will stay open for 60 seconds.")
        print("   Use this time to:")
        print("   1. Open DevTools (F12)")
        print("   2. Inspect the 'Create Event' button")
        print("   3. Note its ID, class, or other attributes")
        print("   4. Update the selector in test_event_creation.py")
        print("\n   Press Ctrl+C to close early, or wait 60 seconds...")
        
        try:
            time.sleep(60)
        except KeyboardInterrupt:
            # Allow clean exit on Ctrl+C during sleep
            raise
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        try:
            page.screenshot(path='debug_selector_finder.png')
            print("📸 Screenshot saved as 'debug_selector_finder.png'")
        except:
            pass  # Screenshot might fail if browser is closed
    finally:
        # Safely close browser, handling connection errors gracefully
        try:
            browser.close()
            print("\n🔒 Browser closed")
        except Exception:
            # Browser might already be closed or connection lost (e.g., on Ctrl+C)
            # This is expected behavior when interrupting, so we silently handle it
            pass

