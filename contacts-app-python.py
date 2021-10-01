from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Contacts App")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
AGE = StringVar()
ADDRESS = StringVar()
CONTACT_NUMBER = StringVar()


def InsertData():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `contacts` (contact_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, gender TEXT, age TEXT, address TEXT, contact_number TEXT)")
    cursor.execute("SELECT * FROM `contacts` ORDER BY `first_name` ASC")
    contacts_data = cursor.fetchall()
    for contact in contacts_data:
        tree.insert(parent = '', index= 'end', values=contact)
    cursor.close()
    conn.close()

def SubmitData():
    if FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or AGE.get() == "" or ADDRESS.get() == "" or CONTACT_NUMBER.get() == "":
        tkMessageBox.showwarning('', 'Please fill all the data', icon="warning")
    else:

        tree.delete(*tree.get_children())
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `contacts` (first_name, last_name, gender, age, address, contact_number) VALUES(?, ?, ?, ?, ?, ?)", (str(
            FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), int(AGE.get()), str(ADDRESS.get()), str(CONTACT_NUMBER.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `contacts` ORDER BY `first_name` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        ADDRESS.set("")
        CONTACT_NUMBER.set("")

def UpdateData():

    tree.delete(*tree.get_children())
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE `contacts` SET `first_name` = ?, `last_name` = ?, `gender` =?, `age` = ?,  `address` = ?, `contact_number` = ? WHERE `contact_id` = ?", (str(
        FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(AGE.get()), str(ADDRESS.get()), str(CONTACT_NUMBER.get()), int(contact_id)))
    conn.commit()
    cursor.execute("SELECT * FROM `contacts` ORDER BY `first_name` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS.set("")
    CONTACT_NUMBER.set("")



def SearchData():
    def search(sv):
        if sv.get()!='':
            result_tree.delete(*result_tree.get_children())
            conn = sqlite3.connect("contacts.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM `contacts` WHERE  first_name LIKE '{sv.get()}%' or last_name LIKE '{sv.get()}%' ")
            contacts_data = cursor.fetchall()
            print(contacts_data)
            for contact in contacts_data:
                result_tree.insert(parent='', index='end', values=contact)
                print(contact)
            cursor.close()
            conn.close()

    sv = StringVar()
    SearchWindow = Toplevel()
    SearchWindow.title("Search Contact")
    width = 1000
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width / 2)) - (width / 2)
    y = ((screen_height / 2)) - (height / 2)
    # SearchWindow.resizable(0, 0)
    SearchWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    FormTitle = Frame(SearchWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(SearchWindow)
    ContactForm.pack(side=TOP, pady=10)
    lbl_title = Label(FormTitle, text="Search Contact",font=('arial', 16), width=300)
    lbl_title.pack(fill=X)
    lbl_lastname = Label(ContactForm, text="Name",font=('arial', 14), bd=5)
    lbl_lastname.grid(row=0, sticky=W)
    firstname = Entry(ContactForm, textvariable=sv, font=('arial', 14))
    sv.trace("w", lambda name, index, mode, sv=sv: search(sv))
    e = Entry(root, textvariable=sv)
    firstname.grid(row=0, column=1)

    TreeFrame = Frame(SearchWindow, width=500)
    TreeFrame.pack(side=TOP)
    scrollbarx = Scrollbar(TreeFrame, orient=HORIZONTAL)
    scrollbary = Scrollbar(TreeFrame, orient=VERTICAL)

    result_tree = ttk.Treeview(TreeFrame, columns=("Contact ID", "First Name", "Last Name", "Gender", "Age", "Address","Contact No"), height=400, selectmode="extended",yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=result_tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=result_tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    result_tree.heading('Contact ID', text="Contact ID", anchor=W)
    result_tree.heading('First Name', text="First Name", anchor=W)
    result_tree.heading('Last Name', text="Last Name", anchor=W)
    result_tree.heading('Gender', text="Gender", anchor=W)
    result_tree.heading('Age', text="Age", anchor=W)
    result_tree.heading('Address', text="Address", anchor=W)
    result_tree.heading('Contact No', text="Contact No", anchor=W)
    result_tree.column('#0', stretch=NO, minwidth=0, width=0)
    result_tree.column('#1', stretch=NO, minwidth=0, width=0)
    result_tree.column('#2', stretch=NO, minwidth=100, width=120)
    result_tree.column('#3', stretch=NO, minwidth=100, width=120)
    result_tree.column('#4', stretch=NO, minwidth=100, width=70)
    result_tree.column('#5', stretch=NO, minwidth=100, width=50)
    result_tree.column('#6', stretch=NO, minwidth=150, width=250)
    result_tree.column('#7', stretch=NO, minwidth=150, width=250)
    result_tree.pack()
    result_tree.bind('<Double-Button-1>', OnSelected)


def OnSelected(event):

    def destroy_box_and_update():
        UpdateWindow.destroy()
        UpdateData()

    global contact_id, UpdateWindow
    curItem = tree.focus()
    print(curItem)
    contents = (tree.item(curItem))
    print(contents)
    selected_item = contents['values']
    print(selected_item)
    contact_id = selected_item[0]
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS.set("")
    CONTACT_NUMBER.set("")
    FIRSTNAME.set(selected_item[1])
    LASTNAME.set(selected_item[2])
    AGE.set(selected_item[4])
    ADDRESS.set(selected_item[5])
    CONTACT_NUMBER.set(selected_item[6])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact List")
    width = 600
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()

    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER,
                       value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER,
                         value="Female",  font=('arial', 14)).pack(side=LEFT)

    lbl_title = Label(FormTitle, text="Edit Contact",
                      font=('arial', 16), width=300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="First Name",
                          font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Last Name",
                         font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="Contact No.", font=('arial', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)

    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('arial', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(ContactForm, textvariable=AGE,  font=('arial', 14))
    age.grid(row=3, column=1)
    address = Entry(ContactForm, textvariable=ADDRESS,  font=('arial', 14))
    address.grid(row=4, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT_NUMBER, font=('arial', 14))
    contact.grid(row=5, column=1)

    btn_updatecon = Button(ContactForm, text="Edit",
                           width=50, command=destroy_box_and_update)
    btn_updatecon.grid(row=6, columnspan=2, pady=10)


def DeleteData():
    if not tree.selection():
        result = tkMessageBox.showwarning(
            '', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion(
            '', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("contacts.db")
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM `contacts` WHERE `contact_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def AddNewWindow():
    global NewWindow
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS.set("")
    CONTACT_NUMBER.set("")
    NewWindow = Toplevel()
    NewWindow.title("Contact List")
    width = 600
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=20)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER,
                       value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER,
                         value="Female",  font=('arial', 14)).pack(side=LEFT)

    lbl_title = Label(FormTitle, text="Add Contact",
                      font=('arial', 16),  width=300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="First Name",
                          font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Last Name",
                         font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="Contact No.", font=('arial', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)

    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('arial', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(ContactForm, textvariable=AGE,  font=('arial', 14))
    age.grid(row=3, column=1)
    address = Entry(ContactForm, textvariable=ADDRESS,  font=('arial', 14))
    address.grid(row=4, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT_NUMBER, font=('arial', 14))
    contact.grid(row=5, column=1)

    btn_addcon = Button(ContactForm, text="Save", width=50, command=SubmitData)
    btn_addcon.grid(row=6, columnspan=2, pady=10)

Mid = Frame(root, width=500)
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, )
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)

TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)

btn_add = Button(MidLeft, text="+ ADD NEW", fg ='white', bg="green",command=AddNewWindow)
btn_add.pack()
btn_search = Button(MidLeft, text="@ SEARCH", fg='white', bg="BLUE", command=SearchData)
btn_search.pack()
btn_delete = Button(MidRight, text="X DELETE", fg='white', bg="red", command=DeleteData)
btn_delete.pack()

scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Contact ID", "First Name", "Last Name", "Gender", "Age", "Address",
                                          "Contact No"), height=300, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Contact ID', text="Contact ID", anchor=W)
tree.heading('First Name', text="First Name", anchor=W)
tree.heading('Last Name', text="Last Name", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Age', text="Age", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Contact No', text="Contact No", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=150, width=200)
tree.column('#3', stretch=NO, minwidth=150, width=200)
tree.column('#4', stretch=NO, minwidth=100, width=100)
tree.column('#5', stretch=NO, minwidth=50, width=100) 
tree.column('#6', stretch=NO, minwidth=250, width=300)
tree.column('#7', stretch=NO, minwidth=250, width=300)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

InsertData()
root.mainloop()