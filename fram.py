#!/usr/bin/env python
# -*- coding:utf-8 -*-

# File Name: tkinter.py
# Author: saturn
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-16 16:24:00

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message: ', 'Hello %s' %name)

app=Application()

app.master.title('hello world')

app.mainloop()
