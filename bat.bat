:loop

taskkill /F /im python.exe
taskkill /F /im phantomjs.exe

python C:\Users\Administrator\Desktop\new-arrivals-monitor\test.py


ping -n 5 127.0.0.1>nul

goto loop




pause