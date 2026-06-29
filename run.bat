@echo off
setlocal
cd /d "%~dp0"
python init_db.py
python delivery_bot_craw_util.py
endlocal

