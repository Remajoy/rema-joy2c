from tkinter import*
import sqlite3

root=Tk()
root.title('My CRUD RJ project')
root.geometry("500x500")

conn=sqlite3.connect('my_data.db')

c=conn.cursor()

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name=Entry(root,width=30)
l_name.grid(row=0,column=1,padx=20)
age=Entry(root,width=30)
age.grid(row=2,column=1,padx=20)
address=Entry(root,width=30)
address.grid(row=3,column=1,padx=20)
email=Entry(root,width=30)
email.grid(row=4,column=1,padx=20)

'''
c.execute(" " "CREATE TABLE"studentinfo"(
"mydata" (
"f_name"	TEXT,
"l_name"	TEXT,
"age"	INTEGER,
"address"	TEXT,
"email"	TEXT
))
'''              


root.mainloop()
