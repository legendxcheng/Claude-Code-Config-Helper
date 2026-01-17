@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul 2>&1
title Claude Config Helper Skill Installer

REM Get the directory where this script is located
set "SCRIPT_DIR=%~dp0"

REM Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo   ======================================================
    echo   ERROR: Python is not installed or not in PATH
    echo   ======================================================
    echo.
    echo   Please install Python from:
    echo   https://www.python.org/downloads/
    echo.
    echo   Make sure to check "Add Python to PATH" during install.
    echo.
    pause
    exit /b 1
)

REM Call the Python script with all arguments
python "%SCRIPT_DIR%install_skill.py" %*

REM If launched by double-click (no arguments), pause before closing
if "%~1"=="" (
    REM Python script handles its own exit in interactive mode
    REM This is just a fallback in case of unexpected exit
    if %errorlevel% neq 0 (
        echo.
        echo   An error occurred. Press any key to close...
        pause >nul
    )
)

exit /b %errorlevel%
