from tkinter import *
import sqlite3

app = Tk()
app.title('Contact Management App')
app.geometry('800x600')
app.configure(background='#4287f5')

dbase = sqlite3.connect('pythondatabase.db')
dbase.execute('''CREATE TABLE IF NOT EXISTS new(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Dept TEXT NOT NULL,
    Year TEXT NOT NULL,
    Clg TEXT NOT NULL,
    Contact TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE)''')
dbase.commit()

name = StringVar()
dept = StringVar()
year = StringVar()
clg = StringVar()
contact = StringVar()
email = StringVar()

def submit_data():
    namedata = name.get()
    deptdata = dept.get()
    yeardata = year.get()
    clgdata = clg.get()
    contactdata = contact.get()
    emaildata = email.get()
    
    try:
        # Insert data in db
        dbase.execute('INSERT INTO new (Name, Dept, Year, Clg, Contact, Email) VALUES (?, ?, ?, ?, ?, ?)', 
                      (namedata, deptdata, yeardata, clgdata, contactdata, emaildata))
        dbase.commit()
        print("Data inserted successfully")
    except sqlite3.IntegrityError:
        print("Error: This email is already registered.")

# Label and entry for Name
lb1 = Label(app, text='Name:', bg='#4287f5', fg='white', font=('Arial', 15))
lb1.place(x=210, y=20)
en1 = Entry(app, font=('Arial', 15), textvariable=name)
en1.place(x=400, y=20)

# Label and entry for Department
lb2 = Label(app, text='Department:', bg='#4287f5', fg='white', font=('Arial', 15))
lb2.place(x=210, y=50)
en2 = Entry(app, font=('Arial', 15), textvariable=dept)
en2.place(x=400, y=50)

# Label and entry for Year
lb3 = Label(app, text='Year:', bg='#4287f5', fg='white', font=('Arial', 15))
lb3.place(x=210, y=80)
en3 = Entry(app, font=('Arial', 15), textvariable=year)
en3.place(x=400, y=80)

# Label and entry for College Name
lb4 = Label(app, text='College Name:', bg='#4287f5', fg='white', font=('Arial', 15))
lb4.place(x=210, y=110)
en4 = Entry(app, font=('Arial', 15), textvariable=clg)
en4.place(x=400, y=110)

# Label and entry for Contact
lb5 = Label(app, text='Contact:', bg='#4287f5', fg='white', font=('Arial', 15))
lb5.place(x=210, y=140)
en5 = Entry(app, font=('Arial', 15), textvariable=contact)
en5.place(x=400, y=140)

# Label and entry for email
lb5 = Label(app, text='Mail Id:', bg='#4287f5', fg='white', font=('Arial', 15))
lb5.place(x=210, y=140)
en5 = Entry(app, font=('Arial', 15), textvariable=email)
en5.place(x=400, y=140)

# Submit button
b1 = Button(app, text='Submit', bg='violet', fg='black', font=('Arial', 15), 
            activebackground='red', activeforeground='white', command=submit_data)
b1.place(x=350, y=200)


app.mainloop()

# Close database connection 
dbase.close()
