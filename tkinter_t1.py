import tkinter as tk

from tkinter import *
from tkinter import ttk

print(" Add Button")
#Add Button
button = ttk.Button(text = "Click Here")
button.pack()
#button.state(['disabled'])

print("Add Checkbox")
#Add CheckBox
ckb = ttk.Checkbutton(text = 'Sri Lanka')
ckb.pack()

print("Add Input Box")
#Add Input Box
inp = ttk.Entry(width = 25)
inp.pack()

