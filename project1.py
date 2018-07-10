from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox
from tkinter.colorchooser import askcolor
import datetime
import webbrowser
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile


def line():
    lin = "_" * 60
    text.insert(INSERT, lin)


def date():
    data = datetime.date.today()
    text.insert(INSERT, data)


def normal():
    text.config(font=("Arial", 10))


def bold():
    text.config(font=("Arial", 10, "bold"))


def underline():
    text.config(font=("Arial", 10, "underline"))


def italic():
    text.config(font=("Arial", 10, "italic"))


def font():
    (triple, color) = askcolor()
    if color:
        text.config(foreground=color)


def kill():
    root.destroy()


def about():
    pass


def opn():
    text.delete(1.0, END)
    file = open(askopenfilename(), 'r')
    if file != '':
        txt = file.read()
        text.insert(INSERT, txt)
    else:
        pass


def save():
    filename = asksaveasfilename()

    if filename:
        alltext = text.get(1.0, END)
        open(filename, 'w').write(alltext)


def copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())


def paste():
    try:
        teext = text.selection_get(selection='CLIPBOARD')
        text.insert(INSERT, teext)
    except:
        tkMessageBox.showerror("Error", " ")


"""
def clear():
    sel = text.get(SEL_FIRST, SEL_LAST)
    text.delete(SEL_FIRST, SEL_LAST)
"""


def clearall():
    text.delete(1.0, END)


def background():
    (triple, color) = askcolor()
    if color:
        text.config(background=color)


def about():
    ab = Toplevel(root)
    txt = "ABOUT THE EDITOR." \
          "A text editor is a type of computer program that edits plain text. Such programs are sometimes known as 'notepad' software, " \
          "following the naming of Microsoft Notepad. Text editors are provided with operating systems and software development packages, " \
          "and can be used to change configuration files, documentation files and programming language source code."
    la = Label(ab, text=txt, foreground='blue')
    la.pack()


def web():
    webbrowser.open('https://www.instagram.com/ayushmat/?hl=en')


def cut(event=None):
    text.event_generate("<<Cut>>")
    return


def undo(event=None):
    text.event_generate("<<Undo>>")
    return


def redo(event=None):
    text.event_generate("<<Redo>>")
    return


def select_all(event=None):
    text.tag_add("sel", '1.0', 'end')
    return


def deselect_all(event=None):
    text.tag_remove("sel", '1.0', 'end')
    return


root = Tk()
root.title("PYTHON TEXT EDITOR")
menu = Menu(root)
filemenu = Menu(root)
root.config(menu=menu)
menu.add_cascade(label="File...", menu=filemenu)
filemenu.add_command(label="Open...", command=opn)
filemenu.add_command(label="Save...", command=save)
filemenu.add_separator()
filemenu.add_command(label="EXIT", command=kill)

modmenu = Menu(root)
menu.add_cascade(label="Modify...", menu=modmenu)
modmenu.add_command(label="Cut...", command=cut)
modmenu.add_command(label="Copy...", command=copy)
modmenu.add_command(label="Paste", command=paste)
modmenu.add_separator()
modmenu.add_command(label="Clear All...", command=clearall)
modmenu.add_separator()
modmenu.add_command(label="Undo...", command=undo)
modmenu.add_command(label="Redo...", command=redo)
modmenu.add_separator()
modmenu.add_command(label="Select All...", command=select_all)
modmenu.add_command(label="DeSelect All...", command=deselect_all)

insmenu = Menu(root)
menu.add_cascade(label="Insert...", menu=insmenu)
insmenu.add_command(label="Date...", command=date)
insmenu.add_command(label="Line...", command=line)
formatmenu = Menu(menu)
menu.add_cascade(label="Format...", menu=formatmenu)
formatmenu.add_cascade(label="Colour...", command=font)
formatmenu.add_separator()
formatmenu.add_radiobutton(label='Normal...', command=normal)
formatmenu.add_radiobutton(label='Bold...', command=bold)
formatmenu.add_radiobutton(label='Underline...', command=underline)
formatmenu.add_radiobutton(label='Italic...', command=italic)

helpmenu = Menu(menu)
menu.add_cascade(label="   ?", menu=helpmenu)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Website", command=web)
text = Text(root, height=30, width=60, font=("Arial", 10))
scroll = Scrollbar(root, command=text.yview)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
text.pack()
root.resizable(0, 0)
root.mainloop()
