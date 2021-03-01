from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)   
        e1.insert(END,selected_tuple[1])
        e2.delete(0, END)   
        e2.insert(END,selected_tuple[2])
    except IndexError:
        pass

def search_command():
    list1.delete(0, END)
    for row in backend.search(account_text.get(), password_text.get()):
        list1.insert(END, row)


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def add_command():
    backend.insert(account_text.get(), password_text.get())
    list1.delete(0,END)
    list1.insert(END,(account_text.get(), password_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], account_text.get(), password_text.get())

window = Tk()

window.wm_title('Password Manager')

l1 = Label(window, text='Account')
l1.grid(row=0, column=0)

l2 = Label(window, text='Password')
l2.grid(row=0, column=3)



account_text=StringVar()
e1 = Entry(window, textvariable=account_text)
e1.grid(row=0, column=2)

password_text=StringVar()
e2 = Entry(window, textvariable=password_text)
e2.grid(row=0, column=4)



list1 = Listbox(window, height=8, width=40)
list1.grid(row=2, column=1, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=3, rowspan=6)



list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row)


b1 = Button(window, text='View All', width=12, command = view_command)
b1.grid(row=3, column=4)

b2 = Button(window, text='Add Entry', width=12, command=add_command)
b2.grid(row=4, column=4)

b3 = Button(window, text='Delete Selected', width=12,command=delete_command)
b3.grid(row=5, column=4)

b4 = Button(window, text='Update', width=12, command=update_command)
b4.grid(row=6, column=4)

b5  =Button(window, text='Search', width=12, command=search_command)
b5.grid(row=7, column=4)
window.mainloop()
