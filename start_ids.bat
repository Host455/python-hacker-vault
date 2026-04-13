@echo off
echo Creating desktop shortcut...
set SCRIPT_PATH=%~dp0start_server.py
set SHORTCUT_PATH=%USERPROFILE%\Desktop\Start IDS System.lnk

powershell "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%SHORTCUT_PATH%'); $SC.TargetPath = 'pythonw.exe'; $SC.Arguments = '%SCRIPT_PATH%'; $SC.WorkingDirectory = '%~dp0'; $SC.Save()"

echo Shortcut created! You can now start the IDS System by double-clicking the shortcut on your desktop.
pause 