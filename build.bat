@echo off
echo =======================================================
echo Building Rclone Auto-Mount Manager Executable
echo =======================================================

:: Use the virtual environment to build
call rclone_env\Scripts\activate.bat
pyinstaller --noconsole --onefile --windowed --name="RcloneAutoMount" main.py

echo.
echo =======================================================
echo Build Complete! Executable is located in the "dist" folder.
echo =======================================================
pause
