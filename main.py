"""
Created on Sun Oct  3 10:33:32 2021

@author: kaione Daniels
"""
from __future__ import print_function
from functools import partial

import ezgmail
from header import *
from tkfunctions import *
import sys
import tkinter as tk


# os.chdir(r'C:\path\to\credentials_json_file')

# ezgmail.init()

# ezgmail.send('al4480771@gmail.com', 'Test', 'Test\nTest')


def main():
    # alpha()
    # saveContact()
    # saveContact()
    # h.deleteContact()
    # h.printContact()

    ###GUI initialization
    top = tk.Tk()
    top.geometry("500x500")
    top.title("Email Program")
    forceexit_arg = partial(forceexit, top)

    B_Store = tk.Button(top, text="Store Email", command=saveContact)
    B_Store.pack()
    B_Delete = tk.Button(top, text="Delete Email", command=deleteContact)
    B_Delete.pack()
    B_Print = tk.Button(top, text="Print Emails", command=printContact)
    B_Print.pack()
    # B_Send
    forceexit_arg = partial(forceexit,top)
    B_Quit = tk.Button(top, text="Quit", command=top.destroy)
    B_Quit.pack()

    top.mainloop()


if __name__ == "__main__":
    main()