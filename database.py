import sqlite3


def rowcount():
    conn = sqlite3.connect('bills/currentbill.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM bill")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return count

def add_row(sno,date,consignee,destination,weight,amount):
    conn = sqlite3.connect('bills/currentbill.db')
    cursor = conn.cursor()
    t=(sno,date,consignee,destination,weight,amount)
    cursor.execute("INSERT INTO bill VALUES (?,?,?,?,?,?)",t)
    conn.commit()
    conn.close()

   

def allrows():
    conn = sqlite3.connect('bills/currentbill.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bill")
    b= cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return b

def deleterow():
    conn = sqlite3.connect('bills/currentbill.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bill WHERE rowid=(SELECT MAX(rowid) FROM bill);")
    conn.commit()
    cursor.close()
    conn.close()

def totalamount():
    conn = sqlite3.connect('bills/currentbill.db')
    cursor = conn.cursor()
    a=cursor.execute("SELECT SUM(AMOUNT) FROM bill")
    b= a.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return b

def deleteall():
    conn = sqlite3.connect('bills/currentbill.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bill")
    conn.commit()
    cursor.close()
    conn.close()

def getbno():
    conn = sqlite3.connect('bills/billno.db')
    cursor = conn.cursor()
    a = cursor.execute("SELECT bno FROM billno WHERE rowid=1")
    b = a.fetchone()[0]
    cursor.execute("UPDATE billno SET bno=(?) WHERE rowid=1",str(b+1))
    conn.commit()
    cursor.close()
    conn.close()
    return b

def getbnowithoutincrement():
    conn = sqlite3.connect('bills/billno.db')
    cursor = conn.cursor()
    a = cursor.execute("SELECT bno FROM billno WHERE rowid=1")
    b = a.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return b
