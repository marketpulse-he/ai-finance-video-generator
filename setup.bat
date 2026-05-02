@echo off
REM ============================================================
REM AI Finance Video Generator - Setup Script (Windows)
REM ============================================================
REM Run this file as Administrator for best results.
REM Double-click or run: setup.bat

setlocal enabledelayedexpansion

echo.
echo ============================================
echo  AI Finance Video Generator
echo  One-Click Setup
echo ============================================
echo.

REM Check Python
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed or not in PATH.
    echo   Download Python 3.8+ from: https://www.python.org/downloads/
    echo   Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

REM Get Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PY_VER=%%i
echo [OK] Python %PY_VER% detected

REM Check version is high enough
for /f "tokens=1,2 delims=." %%a in ("%PY_VER%") do (
    set PY_MAJOR=%%a
    set PY_MINOR=%%b
)

if %PY_MAJOR% LSS 3 (
    echo [ERROR] Python 3.8+ is required (found %PY_VER%)
    pause
    exit /b 1
)
if %PY_MAJOR% EQU 3 if %PY_MINOR% LSS 8 (
    echo [ERROR] Python 3.8+ is required (found %PY_VER%)
    pause
    exit /b 1
)

REM Check pip
where pip >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    python -m pip --version >nul 2>nul
    if !ERRORLEVEL! NEQ 0 (
        echo [ERROR] pip is not installed.
        echo   Run: python -m ensurepip --upgrade
        pause
        exit /b 1
    )
    set PIP_CMD=python -m pip
) else (
    set PIP_CMD=pip
)
echo [OK] pip detected

REM Upgrade pip
echo.
echo  Upgrading pip...
%PIP_CMD% install --upgrade pip >nul 2>nul

REM Install dependencies
echo.
echo  Installing dependencies (this may take a few minutes)...
echo.
%PIP_CMD% install -r requirements.txt

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Dependency installation failed.
    echo   Try: pip install -r requirements.txt
    pause
    exit /b 1
)

echo.
echo [OK] Dependencies installed successfully!

REM Create output directories
if not exist "output\audio" mkdir output\audio
if not exist "output\video" mkdir output\video
if not exist "output\thumbnails" mkdir output\thumbnails
echo [OK] Output directories created

REM Verify installation
echo.
echo  Verifying installation...
python -c "import PIL; print('[OK] Pillow', PIL.__version__)"
python -c "import numpy; print('[OK] NumPy', numpy.__version__)"
python -c "import moviepy; print('[OK] MoviePy', moviepy.__version__)"
python -c "import edge_tts; print('[OK] edge-tts (loaded)')"

echo.
echo ============================================
echo  Setup Complete!
echo ============================================
echo.
echo  Quick Start:
echo    Generate 1 short:     python generate_tiktok_short.py
echo    Batch 3 shorts:       python run_shorts.py
echo    Customize config:     edit config\settings.py
echo    Edit templates:       edit config\templates.py
echo.
echo  Output videos go to:   output\video\
echo ============================================
echo.

pause
