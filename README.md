# WebMobi Events QA Automation

A Python automation script using Playwright to automate event creation on the WebMobi Events platform. This script automatically logs in, creates a new event, fills in the details, and validates the creation.

## 📋 Table of Contents

- [What This Project Does](#what-this-project-does)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [How to Run](#how-to-run)
- [Project File Structure](#project-file-structure)
- [Troubleshooting](#troubleshooting)

---

## 🎯 What This Project Does

This automation script performs the following tasks:

1. **Loads Credentials** - Reads your email and password from a `.env` file
2. **Navigates to Website** - Opens https://events.webmobi.com in a browser
3. **Logs In** - Automatically enters your credentials and logs in
4. **Finds Create Button** - Locates and clicks the "Create Event" button
5. **Fills Event Details** - Enters dummy event data (name, description, date, time)
6. **Submits Event** - Submits the event creation form
7. **Validates Success** - Checks if the event was created successfully

---

## 🔧 Prerequisites

Before you begin, make sure you have:

- **Python 3.8 or higher** installed on your system
- **pip** (Python package manager) - usually comes with Python
- **Internet connection** to download packages and access the website
- **Valid WebMobi Events account** credentials

### Check Your Python Version

```bash
python3 --version
```

You should see something like: `Python 3.8.x` or higher.

---

## 📦 Installation & Setup

Follow these steps in order:

### Step 1: Navigate to Project Directory

Open your terminal and go to the project folder:

```bash
cd /home/karthik_ck/Desktop/webmobi
```

### Step 2: Create Virtual Environment (Recommended)

A virtual environment keeps your project dependencies isolated:

```bash
python3 -m venv .venv
```

**Activate the virtual environment:**

```bash
source .venv/bin/activate
```

You should see `(.venv)` in your terminal prompt, which means the virtual environment is active.

> **Note:** You need to activate the virtual environment every time you open a new terminal session.

### Step 3: Install Python Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This installs:
- `playwright` - Browser automation framework
- `python-dotenv` - For reading environment variables from `.env` file

**Expected output:** You should see installation progress and "Successfully installed..." messages.

### Step 4: Install Playwright Browsers

Playwright needs browser binaries to run:

```bash
playwright install chromium
```

This downloads the Chromium browser (may take a few minutes).

**Expected output:** You should see download progress and "Installing browsers..." messages.

### Step 5: Create .env File

Create a file named `.env` in the project root directory:

```bash
nano .env
```

**Add your credentials in this format:**

```
EMAIL=your_email@example.com
PASSWORD=your_actual_password
```

**Important:**
- Replace `your_email@example.com` with your actual email
- Replace `your_actual_password` with your actual password
- No spaces around the `=` sign
- Save the file: Press `Ctrl+X`, then `Y`, then `Enter`

> **Security Note:** Never share your `.env` file or commit it to version control. It's already in `.gitignore`.

### Step 6: Verify Installation

Check that everything is installed correctly:

```bash
python3 -c "import playwright; print('✅ Playwright installed')"
python3 -c "from dotenv import load_dotenv; print('✅ python-dotenv installed')"
```

Both commands should print success messages.

---

## 🚀 How to Run

### Quick Start

Once everything is set up, simply run:

```bash
python3 test_event_creation.py
```

### Detailed Run Steps

1. **Activate Virtual Environment** (if not already active):
   ```bash
   source .venv/bin/activate
   ```

2. **Verify .env File Exists:**
   ```bash
   cat .env
   ```
   Should show your EMAIL and PASSWORD.

3. **Run the Script:**
   ```bash
   python3 test_event_creation.py
   ```

### What Happens When You Run

1. The script opens a browser window (Chromium)
2. Navigates to https://events.webmobi.com
3. Automatically fills in your login credentials
4. Clicks the login button
5. Waits for the page to load
6. Searches for and clicks the "Create Event" button
7. Fills in event details
8. Submits the form
9. Validates the result

**The browser stays visible** so you can watch the automation in action!

### Expected Output

When running successfully, you'll see output like:

```
🔍 Button Selector Finder
============================================================
This script will log in and then pause so you can inspect the page.
Open browser DevTools (F12) to find the button selector.
============================================================

📍 Navigating to https://events.webmobi.com...
🔐 Logging in...
✅ Logged in successfully

🔍 Analyzing page for buttons and links...
============================================================

Found 25 buttons/links. Showing first 30:

⭐ 1. Text: 'Create Event'
      Visible: True

============================================================

⏸️  Browser will stay open for 60 seconds.
   Use this time to:
   1. Open DevTools (F12)
   2. Inspect the 'Create Event' button
   3. Note its ID, class, or other attributes
   4. Update the selector in test_event_creation.py

   Press Ctrl+C to close early, or wait 60 seconds...
```

---

## 📁 Project File Structure

Here's the complete structure of this project:

```
webmobi/
│
├── 📄 test_event_creation.py    # Main automation script
│   └── Helper script to find button selectors and test login
│
├── 📄 requirements.txt            # Python package dependencies
│   └── Lists: playwright, python-dotenv
│
├── 📄 README.md                   # This file - complete documentation
│
├── 📄 FILE_STRUCTURE.md          # Detailed file structure explanation
│
├── 📄 fix_installation.sh       # Automated fix script for installation issues
│
├── 📄 .gitignore                 # Git ignore rules
│   └── Excludes: .env, __pycache__, venv/, etc.
│
├── 🔒 .env                       # Your credentials (EMAIL, PASSWORD)
│   └── ⚠️  NOT in git - you create this file
│
└── 📁 Generated Files (created automatically):
    │
    ├── .venv/                    # Virtual environment
    │   └── Created with: python3 -m venv .venv
    │
    ├── debug_selector_finder.png # Screenshot saved on errors
    │
    └── playwright-report/        # Test reports (if generated)
```

### File Descriptions

| File | Purpose |
|------|---------|
| `test_event_creation.py` | Main script - logs in and helps find button selectors |
| `requirements.txt` | Lists all Python packages needed for the project |
| `.env` | Stores your login credentials (you create this) |
| `.gitignore` | Prevents committing sensitive files to git |
| `fix_installation.sh` | Helper script to fix common installation issues |
| `README.md` | Complete documentation (this file) |
| `FILE_STRUCTURE.md` | Detailed explanation of project structure |

---

## 🔍 Troubleshooting

### Problem: "EMAIL and PASSWORD must be set in .env file"

**Solution:**
1. Make sure `.env` file exists in the project root
2. Check the file format:
   ```bash
   cat .env
   ```
   Should show:
   ```
   EMAIL=your_email@example.com
   PASSWORD=your_password
   ```
3. No spaces around `=` sign
4. No quotes around values

### Problem: "ModuleNotFoundError: No module named 'playwright'"

**Solution:**
```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Problem: "Browser not found" or "Executable doesn't exist"

**Solution:**
```bash
playwright install chromium
```

### Problem: "g++-11 failed: No such file or directory" (Build Error)

**Solution:**

This happens on Python 3.13. Fix it with:

```bash
# Create symlink for g++-11
sudo ln -sf /usr/bin/g++-13 /usr/bin/g++-11

# Or run the automated fix script
chmod +x fix_installation.sh
./fix_installation.sh
```

### Problem: Script runs but can't find the "Create Event" button

**Solution:**

The script is designed to help you find the button. It will:
1. Log in successfully
2. Show all buttons on the page
3. Keep browser open for 60 seconds
4. Let you inspect with DevTools (F12)

Use the output to identify the correct button selector, then update the script if needed.

### Problem: Browser closes immediately or script exits too fast

**Solution:**

The script is designed to pause for 60 seconds after login. If you need more time:
- Edit `test_event_creation.py`
- Find `time.sleep(60)` (around line 96)
- Change to a longer duration, e.g., `time.sleep(120)` for 2 minutes

### Problem: "Connection closed" error when pressing Ctrl+C

**Solution:**

This is already fixed! The script now handles interruptions gracefully. You can press Ctrl+C without errors.

---

## 💡 Tips & Best Practices

1. **Always activate virtual environment** before running the script
2. **Keep .env file secure** - never share it or commit it to git
3. **Check the output** - the script provides helpful debugging information
4. **Use DevTools** - Press F12 in the browser to inspect elements
5. **Take screenshots** - The script saves screenshots on errors for debugging

---

## 📚 Additional Resources

- [Playwright Python Documentation](https://playwright.dev/python/)
- [Python-dotenv Documentation](https://pypi.org/project/python-dotenv/)
- [Playwright Selectors Guide](https://playwright.dev/python/docs/selectors)

---

## ✅ Quick Reference

### Setup (One-time)
```bash
cd /home/karthik_ck/Desktop/webmobi
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
nano .env  # Add your credentials
```

### Run (Every time)
```bash
cd /home/karthik_ck/Desktop/webmobi
source .venv/bin/activate
python3 test_event_creation.py
```

### All-in-One Command (After Setup)
```bash
cd /home/karthik_ck/Desktop/webmobi && source .venv/bin/activate && python3 test_event_creation.py
```

---

## 📤 Pushing to GitHub

Want to share your project on GitHub? See the complete guide:

**[GITHUB_SETUP.md](GITHUB_SETUP.md)** - Step-by-step instructions for:
- Creating a GitHub repository
- Initializing Git
- Pushing your code
- Security best practices

**Quick Start:**
```bash
git init
git add .
git commit -m "Initial commit: WebMobi Events QA Automation"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

> ⚠️ **Important:** Never commit your `.env` file! It's already in `.gitignore` for your safety.

---

## 🎉 You're All Set!

Follow the steps above, and you'll be running the automation script in no time. If you encounter any issues, check the [Troubleshooting](#troubleshooting) section above.

**Happy Automating!** 🚀

