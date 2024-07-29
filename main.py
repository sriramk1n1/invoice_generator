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
from PIL import Image

#Button Functions

def about():
    window = ctk.CTkToplevel(root)
    window.attributes("-topmost",True)
    window.geometry(placewindowcenter(700,580,window))
    window.title("About")
    f1=ctk.CTkFrame(window,fg_color='transparent')
    f1.grid(row=1,column=0,padx=30)
    f2=ctk.CTkFrame(window,fg_color='transparent')
    f2.grid(row=2,column=0,sticky='nsew')
    my_image1 = ctk.CTkImage(light_image=Image.open("bills\img1.jpg"),
                                  dark_image=Image.open("bills\img1.jpg"),
                                  size=(100, 120))
    image_label1 = ctk.CTkLabel(f1, image=my_image1, text="")
    my_image2 = ctk.CTkImage(light_image=Image.open("bills\img2.jpg"),
                                  dark_image=Image.open("bills\img2.jpg"),
                                  size=(100, 120))
    image_label2 = ctk.CTkLabel(f1, image=my_image2, text="")
    my_image3 = ctk.CTkImage(light_image=Image.open("bills\img3.jpg"),
                                  dark_image=Image.open("bills\img3.jpg"),
                                  size=(100, 120))
    image_label3 = ctk.CTkLabel(f1, image=my_image3, text="")
    my_image4 = ctk.CTkImage(light_image=Image.open("bills\img4.jpg"),
                                  dark_image=Image.open("bills\img4.jpg"),
                                  size=(100, 120))
    image_label4 = ctk.CTkLabel(f1, image=my_image4, text="")
    image_label1.grid(column=0,row=1,padx=25,pady=10,sticky='e')
    image_label2.grid(column=1,row=1,padx=25,pady=10,sticky='e')
    image_label3.grid(column=2,row=1,padx=25,pady=10,sticky='e')
    image_label4.grid(column=3,row=1,padx=25,pady=10,sticky='e')
    l1=ctk.CTkLabel(window,text="This project was made by,",font=("Roboto Medium", 14))
    l1.grid(row=0,column=0,sticky='w',padx=10,pady=10)
    l2=ctk.CTkLabel(f1,text="Sriram Kini",font=("Roboto Medium", 12))
    l2.grid(row=2,column=0,sticky='e',padx=45,pady=0)
    l22=ctk.CTkLabel(f1,text="4NM21CS170",font=("Roboto Medium", 12))
    l22.grid(row=3,column=0,sticky='e',padx=40,pady=0)

    l3=ctk.CTkLabel(f1,text="Sudesh Nayak",font=("Roboto Medium", 12))
    l3.grid(row=2,column=1,sticky='e',padx=35,pady=0)
    l32=ctk.CTkLabel(f1,text="4NM21CS175",font=("Roboto Medium", 12))
    l32.grid(row=3,column=1,sticky='e',padx=35,pady=0)

    l3=ctk.CTkLabel(f1,text="Thushar",font=("Roboto Medium", 12))
    l3.grid(row=2,column=2,sticky='e',padx=55,pady=0)
    l32=ctk.CTkLabel(f1,text="4NM21CS193",font=("Roboto Medium", 12))
    l32.grid(row=3,column=2,sticky='e',padx=40,pady=0)
    l4=ctk.CTkLabel(f1,text="Yasir Manzoor Sheikh",font=("Roboto Medium", 12))
    l4.grid(row=2,column=3,sticky='e',padx=30,pady=0,columnspan=2)
    l42=ctk.CTkLabel(f1,text="4NM21CS215",font=("Roboto Medium", 12))
    l42.grid(row=3,column=3,sticky='e',padx=50,pady=0,columnspan=2)
    l5=ctk.CTkLabel(f2,text="Under the guidance of,",font=("Roboto Medium", 14))
    l5.grid(row=0,column=0,sticky='w',padx=10,pady=(15,0))
    l6=ctk.CTkLabel(f2,text="Dr. Radhakrishna Associate Professor, Dept. of Comp. Science & Eng. NMAM Inst. of Technology,",font=("Roboto Medium", 14))
    l6.grid(row=1,column=0,padx=60,pady=0)

    l7=ctk.CTkLabel(f2,text="Nitte, .As part of internship - II activity (April 2023).",font=("Roboto Medium", 14))
    l7.grid(row=2,column=0,sticky='w',padx=10,pady=0)

    l8=ctk.CTkLabel(f2,text="It involves a GUI where user can create,edit and generate the invoices in pdf format.")
    l8.grid(row=3,column=0,padx=10,sticky='w',pady=0)
    l9=ctk.CTkLabel(f2,text="Functionalities: ")
    l9.grid(row=4,column=0,sticky='w',padx=10,pady=0)

    l10=ctk.CTkLabel(f2,text="- Display current bill number and entries in table")
    l10.grid(row=5,column=0,sticky='w',padx=10,pady=0)

    l11=ctk.CTkLabel(f2,text="- Add Entry: Add the entry to current bill")
    l11.grid(row=6,column=0,sticky='w',padx=10,pady=0)
    l12=ctk.CTkLabel(f2,text="- Edit Entry: Edit entries in current bill")
    l12.grid(row=7,column=0,sticky='w',padx=10,pady=0)
    l13=ctk.CTkLabel(f2,text="- Delete last entry: Delete last entry in current bill")
    l13.grid(row=8,column=0,sticky='w',padx=10,pady=0)
    l14=ctk.CTkLabel(f2,text="- Download: Save current bill in user specified folder in pdf format")
    l14.grid(row=9,column=0,sticky='w',padx=10,pady=0)
    l15=ctk.CTkLabel(f2,text="- Previous Invoices: View/Edit/Download previously generated bills")
    l15.grid(row=10,column=0,sticky='w',padx=10,pady=0)
    
def addentry():
    sno=database.rowcount(currentbillno)+1
    date=entry0.get()
    cno=entry01.get()
    consignee=entry1.get()
    destination=entry2.get()
    weight=entry3.get()
    amount=entry4.get()
    entry01.delete(0,tk.END)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    try:
        if not amount=="":
                float(amount)
        database.add_row(sno,date,cno,consignee,destination,weight,amount,currentbillno)
        populatetable()
    except:
        messagebox.showinfo("Error","Amount must be number")
    entry1.focus()

def editentry():
    window = ctk.CTkToplevel(root)
    window.attributes("-topmost",True)
    window.geometry(placewindowcenter(200,350,window))
    window.title("Edit entry")
    window.grab_set()
    window.grid_columnconfigure(0,weight=1)
    def fn1(choice):
        d1,d2,d3,d4,d5,d6=database.getcontent(choice,currentbillno)
        e0.insert(tk.END,str(d1))
        e01.insert(tk.END,str(d2))
        e1.insert(tk.END,str(d3))
        e2.insert(tk.END,str(d4))
        e3.insert(tk.END,str(d5))
        e4.insert(tk.END,str(d6))

    cbox=ctk.CTkComboBox(window, values=[str(x) for x in range(1,database.rowcount(currentbillno)+1)],command=fn1)
    cbox.set("Sr.No.")
    cbox.grid(row=0,column=0,padx=30,pady=(20,5))
    e0=ctk.CTkEntry(window,placeholder_text="Date")
    e01=ctk.CTkEntry(window,placeholder_text="Consig. No.")
    e1=ctk.CTkEntry(window,placeholder_text="Consignee")
    e2=ctk.CTkEntry(window,placeholder_text="Destination")
    e3=ctk.CTkEntry(window,placeholder_text="Weight")
    e4=ctk.CTkEntry(window,placeholder_text="Amount")
    e0.grid(row=2,column=0,padx=30,pady=5)
    e01.grid(row=3,column=0,padx=30,pady=5)
    e1.grid(row=4,column=0,padx=30,pady=5)
    e2.grid(row=4,column=0,padx=30,pady=5)
    e3.grid(row=6,column=0,padx=30,pady=5)
    e4.grid(row=7,column=0,padx=30,pady=(5,20))
    def ffn1():
        d1=e0.get()
        d2=e01.get()
        d3=e1.get()
        d4=e2.get()
        d5=e3.get()
        d6=e4.get()
        try:
            if not d6=="":
                float(d6)
                id=cbox.get()
                database.setcontent(id,d1,d2,d3,d4,d5,d6,currentbillno)
                window.destroy()
                populatetable()
            else:
                id=cbox.get()
                database.setcontent(id,d1,d2,d3,d4,d5,0,currentbillno)
                window.destroy()
                populatetable()
        except:
            messagebox.showinfo("Error","Amount must be number")
        
    bb = ctk.CTkButton(window,text="Save",command=ffn1)
    bb.grid(row=8,column=0)
    window.mainloop()
    
def previous_invoice():
    #when a bill is selected, function to clear table and load from selected bill no
    def fn1(choice):
        mydict=database.allrows(choice)
        table2.delete(*table2.get_children())
        for row in mydict:
                table2.insert('', tk.END, values=row)
        total=database.totalamount(choice)
        lastrow=("","","","","","Total:",total)
        table2.insert('',tk.END,values=lastrow)

    window = ctk.CTkToplevel(root)
    window.attributes("-topmost",True)
    window.geometry(placewindowcenter(630,500,window))
    window.title("Previous Invoices")
    
    window.grid_columnconfigure(0,weight=1)
    window.grid_rowconfigure(1,weight=1)
    fr=ctk.CTkFrame(window)
    fr.grid_rowconfigure(0,weight=1)
    fr.grid_columnconfigure(0,weight=1)

    
    column=["Sr.No.","Date","Consig. No.","Consignee","Destination","Weight","Amount"]
    table2 = ttk.Treeview(fr, columns=column,show='headings')
    for col in column:
        table2.heading(col, text=col)
        table2.column(col,anchor="center",width=100)
    v1=str(database.getbnowithoutincrement()-1) if database.getbnowithoutincrement()>1 else "1" 
    mydict=database.allrows(v1)
    table2.delete(*table2.get_children())
    for row in mydict:
            table2.insert('', tk.END, values=row)
    total=database.totalamount(v1)
    lastrow=("","","","","","Total:",total)
    table2.insert('',tk.END,values=lastrow)

    table2.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)
    fr.grid(row=1,column=0,sticky='nsew',padx=10,pady=10,columnspan=4)

    cbox=ctk.CTkComboBox(window, values=[str(x) for x in range(1,database.getbnowithoutincrement())],command=fn1)
    cbox.grid(row=0,column=0,padx=10,pady=10,sticky='w')
    cbox.set(v1)

    def populate():
        mydict=database.allrows(int(cbox.get()))
        table2.delete(*table2.get_children())
        for row in mydict:
                table2.insert('', tk.END, values=row)
        total=database.totalamount(int(cbox.get()))
        lastrow=("","","","","","Total:",total)
        table2.insert('',tk.END,values=lastrow)

    def edite():
        window2 = ctk.CTkToplevel(window)
        window2.attributes("-topmost",True)
        window2.geometry(placewindowcenter(200,350,window2))
        window2.title("Edit entry")
        window2.grab_set()
        window2.grid_columnconfigure(0,weight=1)
        def fn1(choice):
            d1,d2,d3,d4,d5,d6=database.getcontent(choice,cbox.get())
            e0.insert(tk.END,str(d1))
            e01.insert(tk.END,str(d2))
            e1.insert(tk.END,str(d3))
            e2.insert(tk.END,str(d4))
            e3.insert(tk.END,str(d5))
            e4.insert(tk.END,str(d6))

        cbox1=ctk.CTkComboBox(window2, values=[str(x) for x in range(1,database.rowcount(int(cbox.get()))+1)],command=fn1)
        cbox1.set("Sr.No.")
        cbox1.grid(row=0,column=0,padx=30,pady=(20,5))
        e0=ctk.CTkEntry(window2,placeholder_text="Date")
        e01=ctk.CTkEntry(window2,placeholder_text="Consig. No.")
        e1=ctk.CTkEntry(window2,placeholder_text="Consignee")
        e2=ctk.CTkEntry(window2,placeholder_text="Destination")
        e3=ctk.CTkEntry(window2,placeholder_text="Weight")
        e4=ctk.CTkEntry(window2,placeholder_text="Amount")
        e0.grid(row=2,column=0,padx=30,pady=5)
        e01.grid(row=3,column=0,padx=30,pady=5)
        e1.grid(row=4,column=0,padx=30,pady=5)
        e2.grid(row=4,column=0,padx=30,pady=5)
        e3.grid(row=6,column=0,padx=30,pady=5)
        e4.grid(row=7,column=0,padx=30,pady=(5,20))
        def ffn1():
            d1=e0.get()
            d2=e01.get()
            d3=e1.get()
            d4=e2.get()
            d5=e3.get()
            d6=e4.get()
            try:
                if not d6=="":
                    float(d6)
                    id=cbox1.get()
                    database.setcontent(id,d1,d2,d3,d4,d5,d6,int(cbox.get()))
                    window2.destroy()
                    populate()
                else:
                    id=cbox1.get()
                    database.setcontent(id,d1,d2,d3,d4,d5,0,int(cbox.get()))
                    window2.destroy()
                    populate()
            except:
                messagebox.showinfo("Error","Amount must be number")
        
        bb = ctk.CTkButton(window2,text="Save",command=ffn1)
        bb.grid(row=8,column=0)
        window2.mainloop()
    def addentrye():
        window3 = ctk.CTkToplevel(window)
        window3.wm_attributes("-topmost",True)
        window3.grab_set()
        window3.geometry(placewindowcenter(200,350,window3))
        window3.title("Add Entry")
        window3.grid_columnconfigure(0,weight=1)

        def ffn1():
            sno=database.rowcount(cbox.get())+1
            date=e0.get()
            cno=e01.get()
            consignee=e1.get()
            destination=e2.get()
            weight=e3.get()
            amount=e4.get()
            try:
                if not amount=="":
                    float(amount)
                database.add_row(sno,date,cno,consignee,destination,weight,amount,cbox.get())
                window3.destroy()
                populate()
            except:
                messagebox.showinfo("Error","Amount must be number")

        e0=ctk.CTkEntry(window3,placeholder_text="Date")
        e01=ctk.CTkEntry(window3,placeholder_text="Consig. No.")
        e1=ctk.CTkEntry(window3,placeholder_text="Consignee")
        e2=ctk.CTkEntry(window3,placeholder_text="Destination")
        e3=ctk.CTkEntry(window3,placeholder_text="Weight")
        e4=ctk.CTkEntry(window3,placeholder_text="Amount")
        e0.grid(row=0,column=0,padx=30,pady=5)
        e01.grid(row=1,column=0,padx=30,pady=5)
        e1.grid(row=2,column=0,padx=30,pady=5)
        e2.grid(row=3,column=0,padx=30,pady=5)
        e3.grid(row=4,column=0,padx=30,pady=5)
        e4.grid(row=5,column=0,padx=30,pady=(5,20))
        e0.insert(0,datetime.date.today().strftime("%d/%m/%Y"))
        bb = ctk.CTkButton(window3,text="Save",command=ffn1)
        bb.grid(row=6,column=0)
        window3.lift()

        window3.mainloop()

    def deletee():
        database.deleterow(int(cbox.get()))
        populate()

    def downloade():
       def ffn1():
            d1=e11.get()
            d2=e22.get()
            d3=e33.get()
            d4=e44.get()
            generate_bill.generatepdf(cbox.get(),d1,d2,d3,d4)
            file_path = filedialog.asksaveasfilename(initialfile="Bill_No_"+cbox.get()+".pdf",defaultextension=".pdf",parent=w2)
            w2.destroy()
            shutil.move("bills\Bill_No_"+cbox.get()+".pdf",file_path)
       w2 = ctk.CTkToplevel(window)
       w2.attributes("-topmost",True)
       w2.geometry(placewindowcenter(300,270,w2))
       w2.title("Add additional info")
       w2.grab_set()
       w2.grid_columnconfigure(0,weight=1)
       e11=ctk.CTkEntry(w2,placeholder_text="Enter to address")
       e11.grid(row=2,column=0,padx=30,pady=10,sticky='ew')
       e22=ctk.CTkEntry(w2,placeholder_text="Enter Bill Title")
       e22.grid(row=3,column=0,padx=30,pady=10,sticky='ew')
       b11=ctk.CTkButton(w2,text="Download",command=ffn1)
       b11.grid(row=4,column=0,padx=10,pady=10)
       e33=ctk.CTkEntry(w2,placeholder_text="Enter Bill Date")
       e33.grid(row=0,column=0,padx=30,pady=10,sticky='ew')
       e44=ctk.CTkEntry(w2,placeholder_text="Enter Billing Month")
       e44.grid(row=1,column=0,padx=30,pady=10,sticky='ew')
       e33.insert(0,datetime.date.today().strftime("%d/%m/%Y"))
       e44.insert(0,datetime.date.today().strftime("%B"))
       w2.mainloop()

    b1=ctk.CTkButton(window,text="Add Entry",command=addentrye)
    b1.grid(row=2,column=0,sticky='e',padx=10,pady=(10,20))
    b2=ctk.CTkButton(window,text="Edit entry",command=edite)
    b2.grid(row=2,column=1,sticky='e',padx=10,pady=(10,20))

    b3=ctk.CTkButton(window,text="Delete last entry",command=deletee)
    b3.grid(row=2,column=2,sticky='e',padx=10,pady=(10,20))
    b4=ctk.CTkButton(window,text="Download",command=downloade)
    b4.grid(row=2,column=3,sticky='e',padx=10,pady=(10,20))

    window.mainloop()

def download():
       global currentbillno
       def ffn1():
            global currentbillno
            billno=database.getbnowithoutincrement()
            d1=e11.get()
            d2=e22.get()
            d3=e33.get()
            d4=e44.get()
            w2.destroy()
            generate_bill.generatepdf(str(billno),d1,d2,d3,d4)
            database.incrementbno()
            currentbillno += 1
            database.createtable(currentbillno)
            populatetable()
            label_1.configure(text="Bill No: "+str(currentbillno))
            file_path = filedialog.asksaveasfilename(initialfile="Bill_No_"+str(billno)+".pdf",defaultextension=".pdf")
            shutil.move("bills\Bill_No_"+str(billno)+".pdf",file_path)

       w2 = ctk.CTkToplevel(root)
       w2.attributes("-topmost",True)
       w2.geometry(placewindowcenter(300,279,w2))
       w2.title("Add additional info")
       w2.grab_set()
       w2.grid_columnconfigure(0,weight=1)
       e11=ctk.CTkEntry(w2,placeholder_text="Enter to address")
       e11.grid(row=2,column=0,padx=30,pady=10,sticky='ew')
       e22=ctk.CTkEntry(w2,placeholder_text="Enter Bill Title")
       e22.grid(row=3,column=0,padx=30,pady=10,sticky='ew')
       b11=ctk.CTkButton(w2,text="Download",command=ffn1)
       b11.grid(row=4,column=0,padx=10,pady=10)
       e33=ctk.CTkEntry(w2,placeholder_text="Enter Bill Date")
       e33.grid(row=0,column=0,padx=30,pady=10,sticky='ew')
       e44=ctk.CTkEntry(w2,placeholder_text="Enter Billing Month")
       e44.grid(row=1,column=0,padx=30,pady=10,sticky='ew')
       e33.insert(0,datetime.date.today().strftime("%d/%m/%Y"))
       e44.insert(0,datetime.date.today().strftime("%B"))
       w2.mainloop()

def deleteentry():
        database.deleterow(currentbillno)
        populatetable()
#set current bill
currentbillno=database.getbnowithoutincrement()

#function to place new windows in center of screen          
def placewindowcenter(x,y,window):
    ws1 = window.winfo_screenwidth()
    hs1 = window.winfo_screenheight()
    x1 = (ws1//2) - (x//2)
    y1 = (hs1//2) - (y//2)
    return f"{x}x{y}+{x1}+{y1}"

#function to clear table and load current updated values into it.
def populatetable():
        mydict=database.allrows(currentbillno)
        table.delete(*table.get_children())
        for row in mydict:
                table.insert('', tk.END, values=row)
        table.grid(row=0,column=0,sticky='nsew',padx=10,pady=10,columnspan=5)
        total=database.totalamount(currentbillno)
        lastrow=("","","","","","Total:",total)
        table.insert('',tk.END,values=lastrow)

#function to detect dark or light theme and set correct colour to table as it doesnt belong to customtkinter, it does not have auto theme change.
def setcorrecttheme():
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

#main window
root = ctk.CTk()
style = ttk.Style()
style.theme_use("default")
root.title("Invoice Generator")
root.iconbitmap('bills\icon.ico')
root.geometry(placewindowcenter(840,520,root))
setcorrecttheme()

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

f1=ctk.CTkFrame(root,width=200,corner_radius=0)
f1.grid(row=0, column=0, sticky="nswe")

f2 = ctk.CTkFrame(master=root)
f2.grid(row=0, column=1, sticky="nswe", padx=15, pady=15)

f2.grid_rowconfigure(0,weight=1)
f2.grid_columnconfigure(0,weight=1)

column=["Sr.No.","Date","Consig. No.","Consignee","Destination","Weight","Amount"]
table = ttk.Treeview(f2, columns=column,show='headings')
for col in column:
        table.heading(col, text=col)
        table.column(col,anchor="center",width=100)
populatetable()

label_1 = ctk.CTkLabel(master=f1,
                        text="Bill No: "+str(currentbillno),
                        font=("Roboto Medium", -16))
label_1.grid(row=1, column=0, pady=(10,0), padx=38, sticky='w')
label_2 = ctk.CTkLabel(master=f1,
                        text="Date: "+str(datetime.date.today().strftime("%d/%m/%Y")),
                        font=("Roboto Medium", -16))
label_2.grid(row=2, column=0, pady=5, padx=30)

entry0=ctk.CTkEntry(f1)
entry0.insert(0,datetime.date.today().strftime("%d/%m/%Y"))
entry01=ctk.CTkEntry(f1,placeholder_text="Consig. No.")
entry1=ctk.CTkEntry(f1,placeholder_text="Consignee")
entry2=ctk.CTkEntry(f1,placeholder_text="Destination")
entry3=ctk.CTkEntry(f1,placeholder_text="Weight")
entry4=ctk.CTkEntry(f1,placeholder_text="Amount")
entry0.grid(row=3,column=0,padx=20,pady=(10,5))
entry01.grid(row=4,column=0,padx=30,pady=5)
entry1.grid(row=5,column=0,padx=30,pady=5)
entry2.grid(row=6,column=0,padx=30,pady=5)
entry3.grid(row=7,column=0,padx=30,pady=5)
entry4.grid(row=8,column=0,padx=30,pady=5)
def ent(event):
     addentry()
root.bind("<Return>",ent)

entry0.bind('<Down>', lambda event:entry01.focus())
entry0.bind('<Up>', lambda event:entry4.focus())

entry01.bind('<Down>', lambda event:entry1.focus())
entry01.bind('<Up>', lambda event:entry0.focus())

entry1.bind('<Down>', lambda event:entry2.focus())
entry1.bind('<Up>', lambda event:entry01.focus())

entry2.bind('<Down>', lambda event:entry3.focus())
entry2.bind('<Up>', lambda event:entry1.focus())

entry3.bind('<Down>', lambda event:entry4.focus())
entry3.bind('<Up>', lambda event:entry2.focus())

entry4.bind('<Down>', lambda event:entry0.focus())
entry4.bind('<Up>', lambda event:entry3.focus())

btn1=ctk.CTkButton(f1,text="Add Entry",command=addentry)
btn1.grid(row=9,column=0,padx=30,pady=20)

btn5=ctk.CTkButton(f2,text="Previous invoice",command=previous_invoice)
btn5.grid(row=1,column=1,sticky='e',padx=5,pady=5)

btn4=ctk.CTkButton(f2,text="Edit entry",command=editentry)
btn4.grid(row=1,column=3,sticky='e',padx=5,pady=5)

btn2=ctk.CTkButton(f2,text="Delete last entry",command=deleteentry)
btn2.grid(row=1,column=2,sticky='e',padx=5,pady=5)

btn3=ctk.CTkButton(f2,text="Download",command=download)

btn3.grid(row=1,column=4,sticky='e',padx=5,pady=5)

if root._get_appearance_mode()=="dark":  
    btn5=ctk.CTkButton(f1,text="Invoice Generator",font=("Roboto Medium", -16),fg_color='#2b2b2b',border_color='#343638',border_width=1,border_spacing=8,command=about)
else:
    btn5=ctk.CTkButton(f1,text="Invoice Generator",font=("Roboto Medium", -16),fg_color='#ebebeb',border_color='#ffffff',border_width=1,border_spacing=8,command=about,text_color='black')
btn5.grid(row=0,column=0,padx=30,pady=20)

root.mainloop()

