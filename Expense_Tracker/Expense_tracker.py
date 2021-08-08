from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3 as sq


# database

def init():
    conn = sq.connect('Expense.db')
    cur = conn.cursor()
    query = '''
        CREATE TABLE IF NOT EXISTS expenses (
            data string,
            name string,
            title string,
            expense number
            )
    '''
    cur.execute(query)
    conn.commit()


def submitexpense():
    values = [date_entry.get(), Name.get(), Title.get(), Expense.get()]
    print(values)
    Etable.insert('', 'end', values=values)

    conn = sq.connect('Expense.db')
    cur = conn.cursor()
    query = '''
    INSERT OR IGNORE INTO expenses VALUES
    (?,?,?,?)
    '''
    cur.execute(query, (date_entry.get(), Name.get(), Title.get(), Expense.get()))
    conn.commit()


def viewexpenses():
    conn = sq.connect('Expense.db')
    cur = conn.cursor()
    query = '''
    SELECT * FROM expenses WHERE expense IS NOT NULL
    '''
    query1 = '''
    SELECT DISTINCT FROM expenses ORDER BY expense
    '''
    total = '''
    SELECT SUM(expense) FROM expenses
    '''
    cur.execute(query)
    rows = cur.fetchall()
    # print(rows)
    cur.execute(total)
    amount = cur.fetchall()[0]
    # print(amount)

    l = Label(root, text='Date\tName\tTitle\tExpense', font=('arial', 15, 'bold'), bg="#4e004e", fg="white")
    l.grid(row=6, column=0, padx=7, pady=7, ipadx=10, ipady=2)

    st = ''
    for i in rows:
        for j in i:
            st += str(j) + '\t'
        st += '\n'

    lastlabel = Label(root, text=st, font=('arial', 14), fg='#4e004e', bg='#dfffdf')
    lastlabel.grid(row=7, column=0, padx=7, pady=7)

    labelprice = Label(root, text=f'Sum: {amount[0]}', font=('arial', 14), fg='#4e004e', bg='#dfffdf')
    labelprice.grid(row=7, column=1, padx=7, pady=7)


init()
root = Tk()
root.title('Expense Tracker')
root.geometry('800x600')
root.config(bg='#dfffdf')

# Label for data
dataLabel = Label(root, text='Date', font=('arial', 15, 'bold'), bg="#4e004e", fg="white", width=12)
dataLabel.grid(row=0, column=0, padx=150, pady=7)

date_entry = DateEntry(root, width=18, font=('arial', 15, 'bold'))
date_entry.grid(row=0, column=1, padx=7, pady=7)

# Name
Name = StringVar()
namelabel = Label(root, text="Name", font=('arial', 15, 'bold'), bg='#4e004e', fg="white", width=12)
namelabel.grid(row=1, column=0, pady=7)

NameEntry = Entry(root, textvariable=Name, font=('arial', 15, 'bold'))
NameEntry.grid(row=1, column=1, pady=7)

# Title
Title = StringVar()
titlelabel = Label(root, text="Title", font=('arial', 15, 'bold'), bg='#4e004e', fg="white", width=12)
titlelabel.grid(row=2, column=0, pady=7)

TitleEntry = Entry(root, textvariable=Title, font=('arial', 15, 'bold'))
TitleEntry.grid(row=2, column=1, pady=7)

# Expense
Expense = IntVar()
expenselabel = Label(root, text="Expense", font=('arial', 15, 'bold'), bg='#4e004e', fg="white", width=12)
expenselabel.grid(row=3, column=0, pady=7)

ExpensEntry = Entry(root, textvariable=Expense, font=('arial', 15, 'bold'))
ExpensEntry.grid(row=3, column=1, pady=7)

# Button
submit = Button(root, text='Submit', font=('arial', 15, 'bold'), bg='#4e004e', fg="white", width=12,
                activebackground='white', activeforeground='#4e004e', command=submitexpense)
submit.grid(row=4, column=0, pady=7)

viewexpense = Button(root, text='View Expense', font=('arial', 15, 'bold'), bg='#4e004e', fg="white", width=12,
                     activebackground='white', activeforeground='#4e004e', command=viewexpenses)
viewexpense.grid(row=4, column=1, pady=7)

Exit = Button(root, text='Exit', font=('arial', 15, 'bold'), bg='#4e004e', fg="white", width=12,
                activebackground='white', activeforeground='#4e004e', command=exit)
Exit.grid(row=6, column=1, pady=7)
# all saved expense.................................
Elist = ['Date', 'Name', 'Title', 'Expense']
Etable = ttk.Treeview(root, column=Elist, show='headings', height=10)
for item in Elist:
    Etable.heading(item, text=item.title())
Etable.grid(row=5, column=0, pady=7, columnspan=3)

mainloop()
