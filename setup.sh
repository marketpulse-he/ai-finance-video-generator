#!/usr/bin/env bash
# ============================================================
# AI Finance Video Generator - Setup Script (Mac/Linux)
# ============================================================
# This script installs everything you need in one command.
# Usage: bash setup.sh

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo ""
echo "============================================"
echo " AI Finance Video Generator"
echo " One-Click Setup"
echo "============================================"
echo ""

# Check Python version
PYTHON_CMD=""
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo -e "${RED}[ERROR] Python is not installed.${NC}"
    echo "  Install Python 3.8+ from: https://www.python.org/downloads/"
    exit 1
fi

PY_VERSION=$($PYTHON_CMD --version 2>&1 | grep -oP '\d+\.\d+' | head -1)
echo -e "${GREEN}[✓]${NC} Python $PY_VERSION detected"

# Extract major.minor
MAJOR=$(echo $PY_VERSION | cut -d. -f1)
MINOR=$(echo $PY_VERSION | cut -d. -f2)

if [ "$MAJOR" -lt 3 ] || ([ "$MAJOR" -eq 3 ] && [ "$MINOR" -lt 8 ]); then
    echo -e "${RED}[ERROR] Python 3.8+ is required (found $PY_VERSION)${NC}"
    exit 1
fi

# Check pip
PIP_CMD=""
if command -v pip3 &> /dev/null; then
    PIP_CMD="pip3"
elif command -v pip &> /dev/null; then
    PIP_CMD="pip"
else
    # Try python -m pip
    if $PYTHON_CMD -m pip --version &> /dev/null; then
        PIP_CMD="$PYTHON_CMD -m pip"
    else
        echo -e "${RED}[ERROR] pip is not installed.${NC}"
        echo "  Install pip: https://pip.pypa.io/en/stable/installation/"
        exit 1
    fi
fi

echo -e "${GREEN}[✓]${NC} pip detected"

# Create virtual environment (optional but recommended)
if command -v virtualenv &> /dev/null || $PYTHON_CMD -m venv --help &> /dev/null; then
    echo ""
    echo "  Creating virtual environment..."
    if $PYTHON_CMD -m venv venv &> /dev/null; then
        echo -e "${GREEN}[✓]${NC} Virtual environment created"
        echo "  Activate it: source venv/bin/activate"
        # Use pip from venv
        PIP_CMD="venv/bin/pip"
    else
        echo -e "${YELLOW}[!]${NC} Could not create venv, installing globally"
    fi
fi

# Install dependencies
echo ""
echo "  Installing dependencies..."
echo ""

$PIP_CMD install --upgrade pip 2>/dev/null || true
$PIP_CMD install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo -e "${RED}[ERROR] Dependency installation failed.${NC}"
    echo "  Try: pip install -r requirements.txt"
    exit 1
fi

echo ""
echo -e "${GREEN}[✓]${NC} Dependencies installed successfully!"
echo ""

# Create output directories
mkdir -p output/audio
mkdir -p output/video
mkdir -p output/thumbnails

echo -e "${GREEN}[✓]${NC} Output directories created"

# Verify installation
echo ""
echo "  Verifying installation..."
$PYTHON_CMD -c "
import PIL, numpy, moviepy, edge_tts
print('  [✓] Pillow', PIL.__version__)
print('  [✓] NumPy', numpy.__version__)
print('  [✓] MoviePy', moviepy.__version__)
print('  [✓] edge-tts (loaded)')
print()
print('  All dependencies ready!')
"

echo ""
echo "============================================"
echo -e "${GREEN}  Setup Complete!${NC}"
echo "============================================"
echo ""
echo "  Quick Start:"
echo "    Generate 1 short:     python generate_tiktok_short.py"
echo "    Batch 3 shorts:       python run_shorts.py"
echo "    Customize config:     edit config/settings.py"
echo "    Edit templates:       edit config/templates.py"
echo ""
echo "  Output videos go to:   output/video/"
echo "============================================"
echo ""
