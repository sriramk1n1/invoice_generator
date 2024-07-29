import sqlite3


def createtable(bno):
    conn = sqlite3.connect('bills/invoice.db')
    cursor = conn.cursor()
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS b{bno}
                   (
                   SNO INT,
                   DATE TEXT,
                   CNO INT,
                   CONSIGNEE TEXT,
                   DESTINATION TEXT,
                   WEIGHT REAL,
                   AMOUNT REAL
                   )""")
    conn.commit()
    cursor.close()
    conn.close()

def rowcount(bno):
    conn = sqlite3.connect('bills/invoice.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM b{bno}")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return count

def getcontent(rowid,bno):
    conn = sqlite3.connect('bills/invoice.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM b{bno} WHERE rowid=(?)",rowid)
    a = cursor.fetchone()
    cursor.close()
    conn.close()
    return a[1],a[2],a[3],a[4],a[5],a[6]

def setcontent(id,d1,d2,d3,d4,d5,d6,bno):
    conn = sqlite3.connect('bills/invoice.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE b{bno} set DATE = ?, CNO = ?, CONSIGNEE = ?, DESTINATION = ?, WEIGHT = ?, AMOUNT = ? WHERE SNO = ?",(d1,d2,d3,d4,d5,d6,id))
    conn.commit()
    cursor.close()
    conn.close()

def add_row(sno,date,cno,consignee,destination,weight,amount,bno):
    conn = sqlite3.connect('bills/invoice.db')
    cursor = conn.cursor()
    t=(sno,date,cno,consignee,destination,weight,amount)
    cursor.execute(f"INSERT INTO b{bno} VALUES (?,?,?,?,?,?,?)",t)
    conn.commit()
    conn.close()

   

def allrows(bno):
    conn = sqlite3.connect('bills/invoice.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM b{bno}")
    b= cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return b

def deleterow(bno):
    conn = sqlite3.connect('bills/invoice.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM b{bno} WHERE rowid=(SELECT MAX(rowid) FROM b{bno});")
    conn.commit()
    cursor.close()
    conn.close()

def totalamount(bno):
    conn = sqlite3.connect('bills/invoice.db')
    cursor = conn.cursor()
    a=cursor.execute(f"SELECT SUM(AMOUNT) FROM b{bno}")
    b= a.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return b


def incrementbno():
    conn = sqlite3.connect('bills/billno.db')
    cursor = conn.cursor()
    a = cursor.execute("SELECT bno FROM billno WHERE rowid=1")
    b = a.fetchone()[0]
    cursor.execute("UPDATE billno SET bno=(?) WHERE rowid=1",(str(b+1),))
    conn.commit()
    cursor.close()
    conn.close()


def setbno(no):
    conn = sqlite3.connect('bills/billno.db')
    cursor = conn.cursor()
    a = cursor.execute("UPDATE billno SET bno=(?) WHERE rowid=1",str(no))
    conn.commit()
    cursor.close()
    conn.close()
def getbnowithoutincrement():
    conn = sqlite3.connect('bills/billno.db')
    cursor = conn.cursor()
    a = cursor.execute("SELECT bno FROM billno WHERE rowid=1")
    b = a.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return b
