import tkinter
from tkinter import filedialog
from tkinter import ttk
import data_reader


def start():

    def open_file():
        filetypes = (
            ('csv files', '*.csv'),
            ('All files', '*.*')
        )

        file_path = filedialog.askopenfilename(title='Open a file', initialdir='C:\\Users\\stas2\\Documents\\Programming\\PyProjects\\SchwarzArtur\\AtrhurSchwarz\\data',filetypes=filetypes)
        path_entry.insert(tkinter.END, file_path)


    def process(file_format, is_header, file_path):
        data_reader.get_result(file_format, is_header, file_path)


    app = tkinter.Tk()
    app.iconphoto(False, tkinter.PhotoImage(file='icon\\icon.png'))
    app.title('Schwarz test')
    app.geometry("300x100")
    app.resizable(False, False)


    combobox_output_format_list = ['file format', 'json', 'csv', 'xlsx']

    combobox_output_format = ttk.Combobox(app,width="10",values=combobox_output_format_list)
    combobox_output_format.current(0)
    combobox_output_format.grid(row=0,column=0)


    check_is_header = tkinter.BooleanVar()

    check_button_is_header = tkinter.Checkbutton(
        app,
        text='Header',
        variable=check_is_header,
        offvalue=False,
        onvalue=True
    )
    check_button_is_header.grid(row=1,column=0)
   

    button_open_file = tkinter.Button(app, text='Open a file', command=lambda: open_file())
    button_open_file.grid(row=0,column=1,stick='wens',rowspan=2)


    button_process = tkinter.Button(app, text='Process', command=lambda: process(combobox_output_format.get(), check_is_header.get(), path_entry.get()))
    button_process.grid(row=0,column=2,stick='wens',rowspan=2)


    path_entry = tkinter.Entry(app)
    path_entry.grid(row=2,column=0,columnspan=3,stick='we')

    app.grid_rowconfigure(0, minsize=40)
    app.grid_rowconfigure(1, minsize=40)
    app.grid_columnconfigure(0, minsize=100)
    app.grid_columnconfigure(1, minsize=100)
    app.grid_columnconfigure(2, minsize=100)

    app.mainloop()
