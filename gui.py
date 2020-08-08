from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from pathlib import Path
from os import name as osname
from main import getSongs

def btnGetPressed():
    tkinter.messagebox.showinfo(message="You may be asked for putting the redirect url on terminal, put it there and the software will start!")
    getSongs(txtUserID.get(), targetDirectory)

def btnSetFolderPressed():
    global targetDirectory
    targetDirectory = tkinter.filedialog.askdirectory()
    Label(root, text=f"Selected directory: \"{targetDirectory}\"").grid(row=2, column=2)

root = Tk() # Creates the window

titleFont = ("sans-serif", 28, "normal")
simpleFont = ("sans-serif", 12, "normal")

root.title("Spotify Extractor")
root.resizable(False, False)
root.iconphoto(True, PhotoImage(file=str(Path("images/icon128.png"))))

lblWelcome = Label(root, text="Spotify Extractor", font=titleFont)
lblWelcome.grid(row=0, columnspan=4)

lblTypeUser = Label(root, text="Type in your user ID for Spotify:", font=simpleFont)
lblTypeUser.grid(row=1, column=0)

txtUserID = Entry(root)
txtUserID.grid(row=1, column=1)

lblSetFolder = Label(root, text="Select the folder where the songs will go:", font=simpleFont)
lblSetFolder.grid(row=2, column=0)

btnSetFolder = Button(root, text="Select Folder", command=btnSetFolderPressed)
btnSetFolder.grid(row=2, column=1)

btnGet = Button(root, text="Obter músicas", command=btnGetPressed)
btnGet.grid(row=3, columnspan=2)

lblCopyright = Label(root, text="Copyright Dyefferson AzevedoⒸ 2020")
lblCopyright.grid(row=4, columnspan=4)

if osname == "nt": # Making icon work with windows
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

root.mainloop() # Shows the window, actually