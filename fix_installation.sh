#!/bin/bash
# Fix Installation Script for WebMobi QA Automation
# This script fixes common installation issues

echo "🔧 Fixing installation issues..."

# Check if we're in a virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Warning: Not in a virtual environment. Activate it first:"
    echo "   source .venv/bin/activate  (or source venv/bin/activate)"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "📌 Python version: $(python3 --version)"

# Install build tools if needed
if ! command -v g++ &> /dev/null; then
    echo "❌ g++ not found. Installing build tools..."
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y build-essential g++ python3-dev
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y gcc gcc-c++ python3-devel
    elif command -v pacman &> /dev/null; then
        sudo pacman -S base-devel gcc python
    fi
fi

# Create symlink for g++-11 if it doesn't exist and g++-13 is available
if ! command -v g++-11 &> /dev/null && command -v g++-13 &> /dev/null; then
    echo "🔗 Creating symlink: g++-11 -> g++-13"
    sudo ln -sf $(which g++-13) /usr/bin/g++-11 || echo "⚠️  Could not create symlink (may need sudo)"
fi

# Upgrade pip and setuptools
echo "⬆️  Upgrading pip and setuptools..."
pip install --upgrade pip setuptools wheel

# Try installing with updated requirements
echo "📦 Installing dependencies..."
pip install --upgrade playwright python-dotenv

# Install Playwright browsers
echo "🌐 Installing Playwright browsers..."
playwright install chromium

echo ""
echo "✅ Installation complete!"
echo ""
echo "Next steps:"
echo "1. Create .env file with your credentials:"
echo "   EMAIL=your_email@example.com"
echo "   PASSWORD=your_password"
echo ""
echo "2. Run the script:"
echo "   python test_event_creation.py"

