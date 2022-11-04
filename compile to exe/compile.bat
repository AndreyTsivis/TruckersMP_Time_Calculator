echo off

cd ..
pip install pyinstaller
pyinstaller --onefile --distpath "compile to exe/" "main.py"

del /s /q /f main.spec
rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null