from tkinter import *
import tkinter as tk
from gui_frames import Login
from tkinter import messagebox
from user_report import end_session_write


HEIGHT = 550
WIDTH = 1000
DARK_PURPLE = '#790E8B'
PURPLE = '#AB47BC'
LIGHT_PINK = '#FFCCCB'
PINK = '#EF9A9A'


def root_centered(root):
    w = 1000
    h = 550

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = tk.Tk()
    root.configure(bg='#F3DFC1')

    root_centered(root)

    login = Login(root, "Login")

    def on_closing():
        if messagebox.askokcancel("Quit", "Are you sure you want to quit? Make sure to log out for privacy reasons."):
            end_session_write("test")
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

    root.mainloop()


if __name__ == '__main__':
    main()
