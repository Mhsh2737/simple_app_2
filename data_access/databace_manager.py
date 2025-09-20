import sqlite3

def create_table_product():
    connection = sqlite3.connect("pdt.db")
    cursor = connection.cursor()
    cursor.execute("create table prodacts (id integer primary key autoincrement, title text, brand text, price integer, expiry_date text)")
    connection.commit()
    connection.close()

def save_product(title, brand, price, expiry_date):
    connection = sqlite3.connect("pdt.db")
    cursor = connection.cursor()
    cursor.execute("insert into prodacts (title , brand , price , expiry_date) values(? , ? , ? , ?)",
                            [title, brand, price, expiry_date])
    connection.commit()
    connection.close()

