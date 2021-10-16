# Employee Record System
from tkinter import *
from tkinter import messagebox
from openpyxl import load_workbook
import xlrd
import pandas as pd

root = Tk()  # Main window
f = Frame(root)
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
root.title("Simple Employee Record System")
root.geometry("830x395")
root.configure(background="Black")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

firstname = StringVar()  # Declaration of all variables
lastname = StringVar()
id = StringVar()
dept = StringVar()
designation = StringVar()
remove_firstname = StringVar()
remove_lastname = StringVar()
searchfirstname = StringVar()
searchlastname = StringVar()
sheet_data = []
row_data = []


def emp_dict(*args):  # To add a new entry and check if entry already exist in excel sheet
    # print("done")
    workbook_name = "sample.xlsx"
    workbook = xlrd.open_workbook(workbook_name)
    worksheet = workbook.sheet_by_index(0)

    wb = load_workbook(workbook_name)
    page = wb.active

    p = 0
    for i in range(worksheet.nrows):
        for j in range(worksheet.ncols):
            cellvalue = worksheet.cell_value(i, j)
            print(cellvalue)
            sheet_data.append([])
            sheet_data[p] = cellvalue
            p += 1
    print(sheet_data)
    fl = firstname.get()
    fsl = fl.lower()
    ll = lastname.get()
    lsl = ll.lower()
    if (fsl and lsl) in sheet_data:
        print("found")
        messagebox.showerror("Error", "This Employee already exist")
    else:
        print("not found")
        for info in args:
            page.append(info)
        messagebox.showinfo("Done", "Successfully added the employee record")

    wb.save(filename=workbook_name)


def add_entries():  # to append all data and add entries on click the button
    a = " "
    f = firstname.get()
    f1 = f.lower()
    l = lastname.get()
    l1 = l.lower()
    d = dept.get()
    d1 = d.lower()
    de = designation.get()
    de1 = de.lower()
    list1 = list(a)
    list1.append(f1)
    list1.append(l1)
    list1.append(d1)
    list1.append(de1)
    emp_dict(list1)


def add_info():  # for taking user input to add the enteries
    frame2.pack_forget()
    frame3.pack_forget()
    emp_first_name = Label(frame1, text="Enter first name of the employee: ", bg="red", fg="white")
    emp_first_name.grid(row=1, column=1, padx=10)
    e1 = Entry(frame1, textvariable=firstname)
    e1.grid(row=1, column=2, padx=10)
    e1.focus()
    emp_last_name = Label(frame1, text="Enter last name of the employee: ", bg="red", fg="white")
    emp_last_name.grid(row=2, column=1, padx=10)
    e2 = Entry(frame1, textvariable=lastname)
    e2.grid(row=2, column=2, padx=10)
    emp_dept = Label(frame1, text="Select department of employee: ", bg="red", fg="white")
    emp_dept.grid(row=3, column=1, padx=10)
    dept.set("Select Option")
    e4 = OptionMenu(frame1, dept, "Select Option", "IT", "Operations", "Sales")
    e4.grid(row=3, column=2, padx=10)
    emp_desig = Label(frame1, text="Select designation of Employee: ", bg="red", fg="white")
    emp_desig.grid(row=4, column=1, padx=10)
    designation.set("Select Option")
    e5 = OptionMenu(frame1, designation, "Select Option", "Manager", "Asst Manager", "Project Manager", "Team Lead",
                    "Senior Tester",
                    "Junior Tester", "Senior Developer", "Junior Developer", "Intern")
    e5.grid(row=4, column=2, padx=10)
    button4 = Button(frame1, text="Add entries", command=add_entries)
    button4.grid(row=5, column=2, pady=10)

    frame1.configure(background="Red")
    frame1.pack(pady=10)


def clear_all():  # for clearing the entry widgets
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()


def remove_emp():  # for taking user input to remove enteries
    clear_all()
    emp_first_name = Label(frame2, text="Enter first name of the employee", bg="red", fg="white")
    emp_first_name.grid(row=1, column=1, padx=10)
    e6 = Entry(frame2, textvariable=remove_firstname)
    e6.grid(row=1, column=2, padx=10)
    e6.focus()
    emp_last_name = Label(frame2, text="Enter last name of the employee", bg="red", fg="white")
    emp_last_name.grid(row=2, column=1, padx=10)
    e7 = Entry(frame2, textvariable=remove_lastname)
    e7.grid(row=2, column=2, padx=10)
    remove_button = Button(frame2, text="Click to remove", command=remove_entry)
    remove_button.grid(row=3, column=2, pady=10)
    frame2.configure(background="Red")
    frame2.pack(pady=10)


def remove_entry():  # to remove entry from excel sheet
    rsf = remove_firstname.get()
    rsf1 = rsf.lower()
    print(rsf1)
    rsl = remove_lastname.get()
    rsl1 = rsl.lower()
    print(rsl1)
    workbook_name = "sample.xlsx"
    path = "sample.xlsx"
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)

    for row_num in range(sheet.nrows):
        row_value = sheet.row_values(row_num)
        if (row_value[1] == rsf1 and row_value[2] == rsl1):
            print(row_value)
            print("found")
            file = "sample.xlsx"
            x = pd.ExcelFile(file)
            dfs = x.parse(x.sheet_names[0])
            dfs = dfs[dfs['First Name'] != rsf]
            dfs.to_excel("sample.xlsx", sheet_name='Employee', index=False)
            messagebox.showinfo("Done", "Successfully removed the Employee record")
    clear_all()


def search_emp():  # can implement search by 1st name,last name,emp id, designation
    clear_all()
    emp_first_name = Label(frame3, text="Enter first name of the employee", bg="red",
                           fg="white")  # to take user input to seach
    emp_first_name.grid(row=1, column=1, padx=10)
    e8 = Entry(frame3, textvariable=searchfirstname)
    e8.grid(row=1, column=2, padx=10)
    e8.focus()
    emp_last_name = Label(frame3, text="Enter last name of the employee", bg="red", fg="white")
    emp_last_name.grid(row=2, column=1, padx=10)
    e9 = Entry(frame3, textvariable=searchlastname)
    e9.grid(row=2, column=2, padx=10)
    search_button = Button(frame3, text="Click to search", command=search_entry)
    search_button.grid(row=3, column=2, pady=10)

    frame3.configure(background="Red")
    frame3.pack(pady=10)


def search_entry():
    sf = searchfirstname.get()
    ssf1 = sf.lower()
    print(ssf1)
    sl = searchlastname.get()
    ssl1 = sl.lower()
    print(ssl1)
    path = "sample.xlsx"
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)

    for row_num in range(sheet.nrows):
        row_value = sheet.row_values(row_num)
        if (row_value[1] == ssf1 and row_value[2] == ssl1):
            print(row_value)
            print("found")
            messagebox.showinfo("Done", "Searched Employee Exist")
            clear_all()
    # else:
    if (row_value[1] != ssf1 and row_value[2] != ssl1):
        print("Not found")
        messagebox.showerror("Sorry", "Employee Record does not Exist")
        clear_all()


# Main window buttons and labels

label1 = Label(root, text="SIMPLE EMPLOYEE RECORD SYSTEM")
label1.config(font=('Italic', 16, 'bold'), justify=CENTER, background="Orange", fg="Yellow", anchor="center")
label1.pack(fill=X)

label2 = Label(f, text="Select an action: ", font=('bold', 12), background="Black", fg="White")
label2.pack(side=LEFT, pady=10)
button1 = Button(f, text="Add", background="Brown", fg="White", command=add_info, width=8)
button1.pack(side=LEFT, ipadx=20, pady=10)
button2 = Button(f, text="Remove", background="Brown", fg="white", command=remove_emp, width=8)
button2.pack(side=LEFT, ipadx=20, pady=10)
button3 = Button(f, text="Search", background="Brown", fg="White", command=search_emp, width=8)
button3.pack(side=LEFT, ipadx=20, pady=10)
button6 = Button(f, text="Close", background="Brown", fg="White", width=8, command=root.destroy)
button6.pack(side=LEFT, ipadx=20, pady=10)
f.configure(background="Black")
f.pack()

root.mainloop()
