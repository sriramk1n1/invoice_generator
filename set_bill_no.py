import sqlite3
import database

def dropalltables():
    conn = sqlite3.connect('bills\invoice.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table_name in tables:
        table_name = table_name[0]
        cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
        print(f"Dropped table: {table_name}")

    cbno=database.getbnowithoutincrement()
    database.createtable(cbno)

    conn.commit()
    conn.close()



print("Enter the bill number to set (All the bill data will be deleted.)\n")
bno=int(input())
database.setbno(bno)
dropalltables()
print("Press any key to quit")
input()

