import eel
import data_reader
import tkinter
from tkinter import filedialog

@eel.expose
def send_data_to_python(settings):
    data_reader.get_result(settings)


@eel.expose
def open_file_path():
    app = tkinter.Tk()
    app.withdraw()
    app.wm_attributes('-topmost', 1)
    file_path = filedialog.askopenfilename(title='Open a file', initialdir='', filetypes=(('csv files', '*.csv'),('All files', '*.*')))
    return file_path


@eel.expose
def open_dir_path():
    app = tkinter.Tk()
    app.withdraw()
    app.wm_attributes('-topmost', 1)
    dir_path = filedialog.askdirectory()
    return dir_path
