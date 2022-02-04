#! /usr/bin/env python3

import tkinter
import re

class MKWindow:
    def __init__(self):
        # Create the main window and adjust size.
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("200x150")

        # Create the entry field "Character Extractor" and label it.
        self.label0 = tkinter.Label(self.mainWindow, text="Character Extractor")
        self.wordEntry = tkinter.Entry(self.mainWindow)

        # Create the Extract Vowel and Consonant Buttons
        self.labelValue = tkinter.StringVar()
        self.labelValue.set("-")
        self.outputLabel = tkinter.Label(self.mainWindow, textvariable=self.labelValue)
        self.convertButton0 = tkinter.Button(self.mainWindow, text="Extract Vowels", command=self.exVowels)
        self.convertButton1 = tkinter.Button(self.mainWindow, text="Extract Consonants", command=self.exConsonants)
        self.convertButton2 = tkinter.Button(self.mainWindow, text="Reset", command=self.xReset)


        # Display the fields and buttons
        self.label0.pack()
        self.wordEntry.pack()

        self.outputLabel.pack()
        self.convertButton0.pack()
        self.convertButton1.pack()
        self.convertButton2.pack()


        # Start and display main window.
        tkinter.mainloop()


    # Define the two functions used to parse the string entered.
    def exVowels(self):
        try:
            # Get the string value entered
            word = str(self.wordEntry.get())
            # Finding all the values and creating an iterator
            vowels0 = re.findall('[aeiouyAEIOUY]', word)
            # Initializing an array
            myarray = []
            # Assigning my iterable to an array (Not sure I need to do this but did.)
            myarray = vowels0
            # Initialize variables for my loop
            a=""
            x=0
            # Loop for my array
            while x < len(myarray):
                # Concatenating each element into a single string
                a = str(a + myarray[x])
                x += 1
            if a != "":
                self.labelValue.set(a)
            else:
                self.labelValue.set("-")
        except:
            self.labelValue.set("Invalid Data Entry")

    def exConsonants(self):
        try:
            # Get the value entered
            word = str(self.wordEntry.get())
            # Finding all the values and creating an iterator
            consonants0 = re.findall('[bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTWXZ]', word)
            # Initializing an array
            myarray = []
            # Assigning my iterable to an array (Not sure I need to do this but did.)
            myarray = consonants0
            # Initialize variables for my loop
            a=""
            x=0
            # Loop for my array
            while x < len(myarray):
                # Concatenating each element into a single string
                a = str(a + myarray[x])
                x += 1
            if a != "":
                self.labelValue.set(a)
            else:
                self.labelValue.set("-")
        except:
            self.labelValue.set("Invalid Data Entry")

    # A function to clear the field and parse result.
    def xReset(self):
        self.wordEntry.delete(0, tkinter.END)
        self.labelValue.set("-")


        
# Run the program
myWindow = MKWindow()
