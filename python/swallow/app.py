from preprocessing import preprocessing
from classifiy import classifiy
from mapping import mapping
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox

text = r'*.txt'

def file_find():
    file = filedialog.askopenfilenames(filetypes=(("Text file", text), ('all file', '*.*')), initialdir=r'C:\\Users')
    en_filepath.delete(0, END)
    en_filepath.insert(END, file[0])

def save_folder():
    dir_path = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    en_folderpath.delete(0, END)
    en_folderpath.insert(END, dir_path)

def processing():
    print(len(en_filepath.get()), en_folderpath.get(), len(en_folderpath.get()), en_filepath.get())
    if len(en_filepath.get()) != 0 or len(en_folderpath.get()) != 0:
        df = preprocessing(en_filepath.get())
        df, li = classifiy(df)
        m = mapping(df)

        m.save(os.path.join(en_folderpath.get(), 'map.html'))
        df.to_csv(os.path.join(en_folderpath.get(), 'data_frame.csv'))
    else:
        messagebox.showinfo('error')

root = Tk()

en_filepath = Entry(root, width=100)
en_filepath.pack(fill='x', padx=1, pady=1)

en_folderpath = Entry(root, width=100)
en_folderpath.pack(fill='x', padx=1, pady=1)

fr_bt = Frame(root)
fr_bt.pack(fill='x', padx=1, pady=1)

bt_upload = Button(fr_bt, text="save path", width=10, command=save_folder)
bt_upload.pack(side='right', padx=1, pady=1)
bt_find = Button(fr_bt, text='find file', width=10, command=file_find)
bt_find.pack(side='right', padx=1, pady=1)
bt_processing = Button(fr_bt, text='data processing', width=15, command=processing)
bt_processing.pack(side='right', padx=1, pady=1)

root.mainloop()
