import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import database
import datetime
import generate_bill
from tkinter import filedialog
import shutil
from tkinter import messagebox
import datetime


def ent(event):
       addentry()

def addentry():
    sno=database.rowcount()+1
    date=datetime.date.today().strftime("%d/%m/%Y")
    consignee=entry1.get()
    destination=entry2.get()
    weight=entry3.get()
    amount=entry4.get()
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    try:
        if not amount=="":
                float(amount)
        database.add_row(sno,date,consignee,destination,weight,amount)
        populatetable()
    except:
        messagebox.showinfo("Error","Amount must be number")
    root.focus()

        

def deleteentry():
        database.deleterow()
        populatetable()

def download():
       billno=database.getbno()
       generate_bill.generatepdf(str(billno))
       file_path = filedialog.asksaveasfilename(initialfile="Bill_No_"+str(billno)+".pdf",defaultextension=".pdf")
       shutil.copy2("bills\Bill_No_"+str(billno)+".pdf",file_path)
       database.deleteall()
       populatetable()
       label_1.configure(text="Bill No: "+str(database.getbnowithoutincrement()))
         
       


def populatetable():
        mydict=database.allrows()
        table.delete(*table.get_children())
        for row in mydict:
                table.insert('', tk.END, values=row)
        table.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)
        total=database.totalamount()
        lastrow=("","","","","Total:",total)
        table.insert('',tk.END,values=lastrow)
    
root = ctk.CTk()
style = ttk.Style()
style.theme_use("default")
if root._get_appearance_mode()=="dark":
        style.configure("Treeview",
                                background="#2a2d2e",
                                foreground="white",
                                rowheight=30,
                                fieldbackground="#343638",
                                bordercolor="#343638",
                                borderwidth=0,
                                font=('Arial', 16),
                                )
        style.map('Treeview', background=[('selected', '#22559b')])
        
        style.configure("Treeview.Heading",
                                background="#343638",
                                foreground="white",
                                relief="flat",
                                font=('Arial', 16))
        style.map("Treeview.Heading",
                        background=[('active', '#3484F0')])
else:
        style.configure("Treeview",
                                background="#ebebeb",
                                foreground="black",
                                rowheight=30,
                                fieldbackground="white",
                                bordercolor="#343638",
                                borderwidth=0,
                                font=('Arial', 16),
                                )
        style.map('Treeview', background=[('selected', '#22559b')])
        
        style.configure("Treeview.Heading",
                                background="#dbdbdb",
                                foreground="black",
                                relief="flat",
                                font=('Arial', 16))
        style.map("Treeview.Heading",
                        background=[('active', '#3484F0')])
root.title("Invoice Generator")
root.iconbitmap('bills\icon.ico')
root.geometry("780x520")

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

f1=ctk.CTkFrame(root,
                width=200,
                corner_radius=0)
f1.grid(row=0, column=0, sticky="nswe")

f2 = ctk.CTkFrame(master=root)
f2.grid(row=0, column=1, sticky="nswe", padx=15, pady=15)

f2.grid_rowconfigure(0,weight=1)
f2.grid_columnconfigure(0,weight=1)

column=["Sr.No.","Date","Consignee","Destination","Weight","Amount"]
table = ttk.Treeview(f2, columns=column,show='headings')
for col in column:
        table.heading(col, text=col)
        table.column(col,anchor="center",width=100)
populatetable()

label_1 = ctk.CTkLabel(master=f1,
                        text="Bill No: "+str(database.getbnowithoutincrement()),
                        font=("Roboto Medium", -16))
label_1.grid(row=1, column=0, pady=(0,20), padx=35, sticky='w')
label_2 = ctk.CTkLabel(master=f1,
                        text="Date: "+str(datetime.date.today().strftime("%d/%m/%Y")),
                        font=("Roboto Medium", -16))
label_2.grid(row=0, column=0, pady=(20,10), padx=30)

entry1=ctk.CTkEntry(f1,placeholder_text="Consignee")
entry2=ctk.CTkEntry(f1,placeholder_text="Destination")
entry3=ctk.CTkEntry(f1,placeholder_text="Weight")
entry4=ctk.CTkEntry(f1,placeholder_text="Amount")
entry1.grid(row=2,column=0,padx=30,pady=5)
entry2.grid(row=3,column=0,padx=30,pady=5)
entry3.grid(row=4,column=0,padx=30,pady=5)
entry4.grid(row=5,column=0,padx=30,pady=5)

btn1=ctk.CTkButton(f1,text="Add Entry",command=addentry)
btn1.grid(row=6,column=0,padx=30,pady=5)

f1.grid_rowconfigure(7,weight=1)

btn2=ctk.CTkButton(f1,text="Delete Entry",command=deleteentry)
btn2.grid(row=8,column=0,padx=30,pady=5)

btn3=ctk.CTkButton(f1,text="Download",command=download)
root.bind("<Return>",ent)
btn3.grid(row=9,column=0,padx=30,pady=(10,40))
root.mainloop()

