@echo off
echo Installing pyinstaller...
pip install pyinstaller
echo Building...
pyinstaller --onefile xchat.py