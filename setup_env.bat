@echo off
echo =======================================================
echo Cài đặt môi trường Python venv: rclone_env
echo =======================================================

:: Create standard virtual environment instead of conda due to channel issues
python -m venv rclone_env

:: Activate and install dependencies
call rclone_env\Scripts\activate.bat
pip install -r requirements.txt

echo.
echo =======================================================
echo Hoàn thành! Môi trường đã sẵn sàng.
echo Để sử dụng thủ công, chạy hàm: rclone_env\Scripts\activate.bat
echo =======================================================
pause
