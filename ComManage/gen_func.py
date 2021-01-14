import os
import webbrowser
from tkinter import filedialog

#to open youtube
def Open_Program():
    webbrowser.open("https://www.youtube.com/watch?v=4C-beigiD_0")

#to open folder in the system
def Open_Folder():
    my_pgm = filedialog.askopenfilename()
    os.system('"%s"' % my_pgm)