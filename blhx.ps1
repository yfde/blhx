Start-Process -filepath "F:\Program Files (x86)\Nemu\EmulatorShell\nemulauncher.exe"
Start-Process powershell -verb RunAs -ArgumentList "cd 'D:\OneDrive - HKUST Connect\Atom_Workspace\blhx' ; python blhx_auto.py ; pause"