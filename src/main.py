import eel
import os

if __name__ == '__main__':
    eel.init('frontend')
    try:
        #Start the application and pass all initial params below
        eel.start('index.html', size=(400, 400))
    except (SystemExit, MemoryError, KeyboardInterrupt):
        #Handle errors and the potential hanging python.exe process
        os.system('taskkill /F /IM python.exe /T')
