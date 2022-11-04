echo off

cd ..
pip install pyinstaller
pyinstaller --onefile --distpath "compile to exe/" "TruckersMP-Time-Calc.py"

del /s /q /f TruckersMP-Time-Calc.spec
rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null