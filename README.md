# Python Key Logger

- this is a python script that runs in the background and watchs your keyboard inputs then save these inputs in a text file
- to run the .pyw file you just have to click it and it will start in the background
- to stop it you will need to run this command in the terminal `TASKKILL /F /IM pythonw.exe`
- compiling the code makes windows unable to delete it
- use this command to compile the code `py -m nuitka --mingw64 <filename>.py --standalone --onefile`
- but to make it run in the background use `py -m nuitka --onefile --windows-disable-console <filename>.py`
