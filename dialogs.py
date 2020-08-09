"""Shows dialogs"""

from tkinter import *

class OkDismissDialog():
    def __init__(self, message, func):
        dialog = Tk()
        message = Label(dialog, text=message)
        message.pack()