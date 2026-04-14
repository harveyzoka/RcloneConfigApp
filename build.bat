@echo off
echo =======================================================
echo Building Rclone Auto-Mount Manager Executable (Conda)
echo =======================================================

:: Use conda to run python and build
call conda run -n rclone_gui_env pyinstaller --noconsole --onedir --windowed --icon="app_icon.ico" --add-data="app_icon.ico;." --name="RcloneAutoMount" main.py

echo.
echo =======================================================
echo Build Complete! Executable is located in the "dist" folder.
echo =======================================================
pause
