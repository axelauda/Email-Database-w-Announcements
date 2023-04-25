# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 11:12:36 2021

@author: Kaione Daniels


"""

from __future__ import print_function
from functools import partial

import ezgmail
import sys
import os
import tkinter as tk

#notes 
    #could have two emails that are same'
    #change email function
    
#saving text file into matrix

def readFile():
    matrix = []
    file = open("contactInfo.txt", "r")
    
    rows = file.readlines()
    
    for row in rows:
        matrix.append(row.split("~"))
        
    print(matrix)
    file.close()
    
    return matrix

def submitAnswer(fn_question, main_window, ln_question, email_question):
    firstName = fn_question.get()
    lastName = ln_question.get()
    email = email_question.get()
    
    file = open("contactInfo.txt", "a")
    file.write(firstName + "~" + lastName + '~' + email + "~" + "\n")
    file.close()
    alpha() #reordering matrix
    
    main_window.quit()
    main_window.destroy()
    
#saving contact into text file
def saveContact():
    
    main_window = tk.Tk()
    main_window.geometry("500x800")
    main_window.title("Save Contact")
    
    #display contact
    fn_label = tk.Label(main_window, text="First Name:")
    fn_question = tk.Entry(main_window)
    fn_label.pack()
    fn_question.pack()
    
     #display contact
    ln_label = tk.Label(main_window, text="Last Name:")
    ln_question = tk.Entry(main_window)
    ln_label.pack()
    ln_question.pack()
    
     #display contact
    email_label = tk.Label(main_window, text="Email:")
    email_question = tk.Entry(main_window)
    email_label.pack()
    email_question.pack()
    
    subAns = partial(submitAnswer, fn_question, main_window, ln_question, email_question)
    time_submit = tk.Button(main_window, text = "Submit", command = subAns)
    time_submit.pack()
    
    #exiting to main menu
    time_quit = tk.Button(main_window, text="Exit to Main Menu", command = main_window.destroy)
    time_quit.pack()
    
    main_window.mainloop()
        
        
             ####
       # firstName = str(input("Type first name: "))
       # lastName = str(input("Type last name: "))
       # email = str(input("Type email: "))
        
       # file = open("contactInfo.txt", "a")
        
       # file.write(firstName + "~" + lastName + '~' + email + "~" + "\n")
    
       # file.close()
      #  alpha() #reordering matrix
    
        
def display_delete(fn_question, main_window):
    matrix = readFile()
    matrix_possible = []
    search = fn_question.get()
    
    for rows in matrix:
        first_name = rows[0]
        last_name = rows[1]
        email = rows[2]

        if(first_name == search or last_name == search or email == search):
            matrix_possible.append(rows)
        
    
    main_window.destroy() #destroying old window
       
    main_window = tk.Tk()
    main_window.geometry("500x800")
    main_window.title("Removing Email from the Chain")
    chosen_email = tk.StringVar()
    
    # display contact
    fn_label = tk.Label(main_window, text="Choose which one to Delete")
    fn_label.pack()
   
    #tk.Radiobutton(main_window, text="listed_email", padx = 20, variable=v, value=1).pack(anchor=tk.W)
  
    print(matrix_possible)
    
    for rows in matrix_possible:
        listed_email = "FN: " + rows[0] + " LN: " + rows[1] + "Email: " + rows[2]
        tk.Radiobutton(main_window, text= listed_email, padx = 20, variable=chosen_email, value=1).pack(anchor=tk.W)

    print(chosen_email)

    deleted = partial(delete, chosen_email, main_window)
    time_submit = tk.Button(main_window, text="Submit", command=deleted)
    time_submit.pack()
    
    main_window.mainloop()

#def delete(chosen_email):

    
    ##deleting email##
def deleteContact():

    while True:
        main_window = tk.Tk()
        main_window.geometry("500x800")
        main_window.title("Save Contact")

        # display contact
        fn_label = tk.Label(main_window, text="Put Email, First Name, or Last Name to search:")
        fn_question = tk.Entry(main_window)
        fn_label.pack()
        fn_question.pack()



        delCon = partial(display_delete, fn_question, main_window)
        time_submit = tk.Button(main_window, text="Submit", command=delCon)
        time_submit.pack()

        # exiting to main menu
        time_quit = tk.Button(main_window, text="Exit to Main Menu", command=main_window.destroy)
        time_quit.pack()
        main_window.mainloop()

        deleted = False

        matrix = readFile()
        file = open("contactInfo.txt", "w")
        email = str(input("Type email to delete: "))
        # print(matrix)

        count = 0
        for row in matrix:
            if (row[2] == email):
                del matrix[count]
                print("contact deleted")
                deleted = True
                break
            count += 1

        if deleted != True:
            print("email not found")

        for row in matrix:
            file.write(row[0] + "~" + row[1] + '~' + row[2] + "~" + "\n")

        file.close()

    
def alpha():
    matrix = readFile()
    
    matrix.sort()
    
    file = open("contactInfo.txt", "w")
    for row in matrix:
        file.write(row[0] + "~" + row[1] + '~' + row[2] + "~" + "\n")
    
    file.close()
    
    
def printContact():

    main_window = tk.Tk()
    main_window.geometry("500x800")
    main_window.title("Contact List")

    # exiting to main menu
    time_quit = tk.Button(main_window, text="Exit to Main Menu", command=main_window.destroy)
    time_quit.pack()
    main_window.mainloop()

    matrix = readFile()
    #count = 0

    line = tk.Text(main_window)

    for row in matrix:

        line.insert(tk.INSERT, str(row[0]))
        line.pack()

        #Old print in terminal
        #print('Contact ' + str(count) + ':')
        #print('     Name: ' + row[0] + ' ' + row[1])
        #print('     Email: ' + row[2])

        #count += 1