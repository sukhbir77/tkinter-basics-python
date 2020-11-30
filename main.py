import tkinter
from tkinter import *
from tkinter import messagebox
from functools import partial

#win = Tk()
#win.geometry("500x500")
# Grid method
# Place method to place the buttons acc. to pixels.
# Pack method to simply place buttons acc. to their commands.

#------------------BUTTON--------------------------
'''
def pr():
    print('Hi')
b = Button(win, text="Button", command = pr, padx = 20, pady = 10, activeforeground = 'red')
b.place(x = 100, y = 200)
'''
#----------------CANVAS-----------------------------
'''c = Canvas(win, height = 250, width = 300, bg = 'blue')
coord = 10,50,240,210
arc = c.create_arc(coord, start = 90, extent= 90, fill = 'red')
line = c.create_line(10,10,200,200, fill = 'white')
c.pack()'''
#------------------CHECK_BUTTONS && RADIO_BUTTONS-----
'''
c1 = IntVar()
c2 = IntVar()
cb = Checkbutton(win, text = 'Music', offvalue = 0, onvalue = 1, height = 5, width = 10, variable = c1)
cb.pack()

cb2 = Checkbutton(win, text = 'Video', offvalue = 0, onvalue = 1, height = 5, width = 10, variable = c2)
cb2.pack()
'''
'''

var = IntVar()
r1 = Radiobutton(win, text = 'Option 1', variable = var, value = 1)
r1.pack()
r2 = Radiobutton(win, text = 'Option 2', variable = var, value = 2)
r2.pack()
r3 = Radiobutton(win, text = 'Option 3', variable = var, value = 3)
r3.pack()
'''
#----------------Entry Widgets -----------------------------------
'''
l = Label(win, text = 'Username')
l.pack(side = LEFT)
e = Entry(win)
e.pack(side = RIGHT)
t = Text(win)
t.insert(INSERT, 'HELLO')
t.pack()
'''
#-------------CALCULATOR----------------------------
'''
def sum(label,x1,x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum = int(n1) + int(n2)
    label.configure(text = f'Sum is : {sum}')
    return

l1 = Label(win, text = 'First No')
l1.grid(row = 1, column = 0)
l2 = Label(win, text = 'Second No')
l2.grid(row = 2, column = 0)
label = Label(win)
label.grid(row = 4, column = 0)

x1 = StringVar()
x2 = StringVar()

e1 = Entry(win, textvariable = x1)
e1.grid(row = 1 , column = 2)

e2 = Entry(win, textvariable = x2)
e2.grid(row = 2 , column = 2)

sum = partial(sum,label,x1,x2)

b = Button(win, text = 'Calculate', command = sum)
b.grid(row  = 3, column = 0)
'''
# ---------------------Window_Configuration-------------
'''
frame  = Frame(win)
frame.pack()

frame2 = Frame(win)
frame2.pack(side=BOTTOM)

rb = Button(frame, text = "Button")
rb.pack(side = LEFT)

rb2 = Button(frame2, text = "Button")
rb2.pack(side = BOTTOM)
'''
# Listbox---------------------------
'''
lb = Listbox(win)
lb.insert(1, 'python')
lb.insert(2, 'c')
lb.insert(3, 'C++')
lb.insert(4, 'ruby')
lb.insert(5, 'json')
lb.pack()
'''
# Top Level -------------------------

'''win.title('First Window')
top = Toplevel()
top.title('Second Window')
'''

#-----------------Message_Box-------------
'''def hello():
    messagebox.showinfo('from Computer', 'Hey There')

b = Button(win, text = 'PopUP', command = hello)
b.pack()
'''
#----------------Menu_Buttons_Menu_Bars--------------

'''mb = Menubutton(win, text = 'FILE')
mb.grid()
mb.menu = Menu(mb)
mb['menu'] = mb.menu

x1 = IntVar()
x2 = IntVar()

mb.menu.add_checkbutton(label = 'Open', variable = x1)
mb.menu.add_checkbutton(label = 'Close', variable = x2)

mb.pack()'''

# Complete Menu Bar------------------------------------


'''def nothing():
    file = Toplevel(win)
    button = Button(file, text = 'DO NOTHING')
    button.pack()

menubar = Menu(win)

filemenu = Menu(menubar)
filemenu.add_command(label = 'New Window', command = nothing)
filemenu.add_command(label = 'Open', command = nothing)
filemenu.add_command(label = 'Close', command = nothing)
filemenu.add_separator()
filemenu.add_command(label = 'FUCK', command = nothing)
filemenu.add_command(label = 'SAVE AS', command = nothing)
filemenu.add_command(label = 'Delete', command = nothing)
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = win.quit)

menubar.add_cascade(label = 'File', menu = filemenu)


editmenu = Menu(menubar)
filemenu = Menu(menubar)

editmenu.add_command(label = 'Undo', command = nothing)
editmenu.add_command(label = 'REDO', command = nothing)
editmenu.add_command(label = 'Cut', command = nothing)
editmenu.add_separator()
editmenu.add_command(label = 'copy', command = nothing)
editmenu.add_command(label = 'Select All', command = nothing)
editmenu.add_command(label = 'Save all', command = nothing)
editmenu.add_separator()
editmenu.add_command(label = 'Exit', command = win.quit)

menubar.add_cascade(label = 'EXit', menu = editmenu)
win.config(menu = menubar)
'''
#ScrollBar-------------------------------------------
'''
s = Scale(win)
s.pack()
#Spin box
sb = Spinbox(win, from_ = 0, to = 10)
sb.pack()
#Scrollbar
scrollbar = Scrollbar(win)
scrollbar.pack(side = RIGHT, fill = Y)
list = Listbox(win, yscrollcommand = scrollbar.set)

for line in range(100):
    list.insert(END, 'THis is line no is '+ str(line))
list.pack(side = LEFT, fill = BOTH)
scrollbar.config(command = list.yview)
'''
#--------------Panned_Window--------------------------

'''pw = PanedWindow()
pw.pack(fill = BOTH, expand = 1)


left = Entry(pw, bd = 5)
pw.add(left)

pw2 = PanedWindow(pw, orient = VERTICAL)
pw.add(pw2)

top = Scale(pw2, orient = HORIZONTAL)
pw2.add(top)

bottom = Button(pw2, text = 'OK')
pw2.add(bottom)
mainloop()
#win.mainloop()'''

#---------------Geometry_Widgets--------------------

win = Tk()

'''b = 0
for i in range(6):
    for j in range(6):
        b = b + 1
        Button(win, text = str(b), borderwidth = 1).grid(row = i , column = j)
'''
win.mainloop()
