from preprocessing import preprocessing
from classifiy import classifiy
from mapping import mapping_dot
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
from mapping import mapping_line
from pandas import concat

text = r'*.txt'

def file_find(insert):
    file = filedialog.askopenfilenames(filetypes=(("Text file", text), ('all file', '*.*')), initialdir=r'C:\\Users')
    if insert == 1:
        en_filepath.delete(0, END)
        en_filepath.insert(END, file[0])
    elif insert == 2:
        en_filepath_2.delete(0, END)
        en_filepath_2.insert(END, file[0])

def save_folder(e):
    dir_path = filedialog.askdirectory(parent=root,initialdir=r"C:\\Users",title='Please select a directory')
    en_folderpath.delete(0, END)
    en_folderpath.insert(END, dir_path)

def processing():
    is_compare = False

    if len(en_filepath.get()) != 0 or len(en_folderpath.get()) != 0:
        df = preprocessing(en_filepath.get())

        if len(en_filepath_2.get()) != 0:
            is_compare = True
            df_2 = preprocessing(en_filepath_2.get())

        try:
            df, li = classifiy(df, roop_count=int(number.get()))
            if is_compare:
                df_2, li_2 = classifiy(df, roop_count=int(number.get()))
        except:
            messagebox.showerror('숫자를 입력하십시오')

        if is_compare:
            m = mapping_dot(df)
            m2 = mapping_dot(df, color='red')
            m2.save(os.path.join(en_folderpath.get(), 'map2.html'))
        else:
            m = mapping_dot(df)

        m.save(os.path.join(en_folderpath.get(), 'map.html'))

        df_compare = concat([df, df_2], axis=0)
        df.to_csv(os.path.join(en_folderpath.get(), 'data_frame.csv'))
        if is_compare:
            df_2.to_csv(os.path.join(en_folderpath.get(), 'data_frame_2.csv'))
            df_compare.to_csv(os.path.join((en_folderpath.get()), 'data_frame_compare.csv'))
    else:
        messagebox.showinfo('error')

root = Tk()
root.title("Swallow")

# 1st data(require)

en_filepath_lable = Label(root, text="처리 할 데이터")
en_filepath_lable.pack()

en_filepath = Entry(root, width=90)
en_filepath.pack()
en_filepath.bind('<1>', lambda e: file_find(1))

# 2st data

en_filepath_2 = Entry(root, width=90)
en_filepath_2.pack(padx=25)
en_filepath_2.bind('<1>', lambda e: file_find(2))

# path(require)

fo_root = Frame()
fo_root.pack(pady=20)

en_folder_path_lable = Label(fo_root, text="저장 할 폴더")
en_folder_path_lable.pack()

en_folderpath = Entry(fo_root, width=50)
en_folderpath.pack(padx=15)
en_folderpath.bind('<1>', save_folder)

# loop number(require)

number = Entry(root, width=10)
number.pack()

# button(intrection)

fr_bt = Frame(root)
fr_bt.pack(fill='x', padx=1, pady=1)

bt_processing = Button(fr_bt, text='데이터 처리', width=15, command=processing)
bt_processing.pack(side='right', padx=15, pady=5)


root.mainloop()