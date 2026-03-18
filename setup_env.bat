@echo off
echo =======================================================
echo Cai dat moi truong Conda: rclone_gui_env
echo =======================================================

:: Create conda environment (Python 3.10)
call conda create -n rclone_gui_env python=3.10 -y

:: Install requirements inside conda env
call conda run -n rclone_gui_env pip install -r requirements.txt

echo.
echo =======================================================
echo Hoan thanh!
echo Moi truong cua ban gio do dung 100% Anaconda quan ly.
echo De su dung, hay chay lenh: conda activate rclone_gui_env
echo =======================================================
pause
