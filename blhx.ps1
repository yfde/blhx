Start-Process -filepath "F:\Program Files\Netease\MuMuPlayer-12.0\shell\MuMuPlayer.exe"
Start-Process powershell -verb RunAs -ArgumentList "cd 'F:\blhx' ; python blhx_auto.py ; pause"