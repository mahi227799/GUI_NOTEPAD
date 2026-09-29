from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


# ============================================================
# FUNCTIONS
# ============================================================

def newfile():
    global file

    root.title("GUI NOTEPAD")
    file = None

    textarea.delete(1.0, END)


def openfile():
    global file

    file = askopenfilename(
        defaultextension=".txt",
        filetypes=[
            ("Text Documents", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if file == "":
        file = None

    else:
        root.title(os.path.basename(file) + " - Notepad")

        textarea.delete(1.0, END)

        with open(file, "r", encoding="utf-8") as f:
            textarea.insert(1.0, f.read())


def savefile():
    global file

    if file is None:

        file = asksaveasfilename(
            initialfile="untitled.txt",
            defaultextension=".txt",
            filetypes=[
                ("Text Documents", "*.txt"),
                ("All Files", "*.*")
            ]
        )

        if file == "":
            file = None
            return

    with open(file, "w", encoding="utf-8") as f:
        f.write(textarea.get(1.0, END))

    root.title(os.path.basename(file) + " - Notepad")

    print("File saved")


def quitapp():
    root.destroy()


def cut():
    textarea.event_generate("<<Cut>>")


def copy():
    textarea.event_generate("<<Copy>>")


def paste():
    textarea.event_generate("<<Paste>>")


def about():
    showinfo(
        "Notepad",
        "Simple GUI Notepad"
    )


# ============================================================
# MAIN WINDOW
# ============================================================

root = Tk()

root.title("GUI NOTEPAD")

root.geometry("800x500")

root.minsize(
    500,
    300
)


# ============================================================
# CURRENT FILE
# ============================================================

file = None


# ============================================================
# TEXT AREA
# ============================================================

textarea = Text(
    root,
    font=("Arial", 13),
    undo=True
)

textarea.pack(
    expand=True,
    fill=BOTH
)


# ============================================================
# SCROLLBAR
# ============================================================

scrollbar = Scrollbar(
    textarea
)

scrollbar.pack(
    side=RIGHT,
    fill=Y
)

scrollbar.config(
    command=textarea.yview
)

textarea.config(
    yscrollcommand=scrollbar.set
)


# ============================================================
# MENU BAR
# ============================================================

menubar = Menu(root)


# ---------------- FILE MENU ----------------

filemenu = Menu(
    menubar,
    tearoff=0
)

filemenu.add_command(
    label="New",
    command=newfile
)

filemenu.add_command(
    label="Open",
    command=openfile
)

filemenu.add_command(
    label="Save",
    command=savefile
)

filemenu.add_separator()

filemenu.add_command(
    label="Exit",
    command=quitapp
)

menubar.add_cascade(
    label="File",
    menu=filemenu
)


# ---------------- EDIT MENU ----------------

editmenu = Menu(
    menubar,
    tearoff=0
)

editmenu.add_command(
    label="Cut",
    command=cut
)

editmenu.add_command(
    label="Copy",
    command=copy
)

editmenu.add_command(
    label="Paste",
    command=paste
)

menubar.add_cascade(
    label="Edit",
    menu=editmenu
)


# ---------------- HELP MENU ----------------

helpmenu = Menu(
    menubar,
    tearoff=0
)

helpmenu.add_command(
    label="About",
    command=about
)

menubar.add_cascade(
    label="Help",
    menu=helpmenu
)


root.config(
    menu=menubar
)


# ============================================================
# KEYBOARD SHORTCUTS
# ============================================================

root.bind(
    "<Control-n>",
    lambda event: newfile()
)

root.bind(
    "<Control-o>",
    lambda event: openfile()
)

root.bind(
    "<Control-s>",
    lambda event: savefile()
)


# ============================================================
# START PROGRAM
# ============================================================

root.mainloop()