import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from datetime import datetime

expired_items = []
today = datetime.now()
today_date = today.date()
total_price = 0

products = [
    {"id": "1", "title": "شیر", "brand": "پاک", "price": 15000 ,"expiry_date": "2024-10-15"},
    {"id": "2", "title": "نان", "brand": "سحر", "price": 5000 ,"expiry_date": "2027-10-20"},
    {"id": "3", "title": "پنیر", "brand": "آنا", "price": 95000 ,"expiry_date": "2024-11-01"},
    {"id": "4", "title": "ماست", "brand": "پاک", "price": 100000 ,"expiry_date": "2029-10-18"},
    {"id": "5", "title": "تخم مرغ", "brand": "تلاونگ", "price": 20000 ,"expiry_date": "2020-11-10"},
    {"id": "6", "title": "شکلات", "brand": "باراکا", "price": 100000 ,"expiry_date": "2023-01-05"}
]

for product in products:
    expiry_date = datetime.strptime(product["expiry_date"], '%Y-%m-%d').date()
    if expiry_date < today_date:
        expired_items.append(product)
        total_price += product["price"]

def create_product_table_window(data):
    window = Tk()
    window.title("Expired product report")
    window.iconbitmap("")
    window.geometry("800x400")

    columns = ("id", "title", "brand", "price", "expiry_date")
    tree = ttk.Treeview(window, columns=columns, show="headings")

    Label(window, text="id", font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=11, height=2,
          bg="light green", fg="dark blue").place(x=20, y=9)
    tree.column("id", width=3, anchor=tk.CENTER)

    Label(window, text="title", font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=21, height=2,
          bg="light green", fg="dark blue").place(x=125, y=9)
    tree.column("title", width=100, anchor=tk.CENTER)

    Label(window, text="brand", font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=17, height=2,
          bg="light green", fg="dark blue").place(x=330, y=9)
    tree.column("brand", width=70, anchor=tk.CENTER)

    Label(window, text="price :", font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=15, height=2,
          bg="light green", fg="dark blue").place(x=503, y=9)
    tree.column("price", width=50, anchor=tk.E)

    Label(window, text="expiry_date", font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=12, height=2,
          bg="light green", fg="dark blue").place(x=655, y=9)
    tree.column("expiry_date", width=20, anchor=tk.CENTER)

    for product in expired_items:
        tree.insert("", tk.END,values=(product["id"], product["title"], product["brand"], product["price"], product["expiry_date"]))
        tree.pack(pady=55, padx=20, fill=tk.BOTH, expand=True)

        total_price_label = tk.Label(window, text=total_price, width=33,bg="white",anchor=tk.W).place(x=210, y=363)
        Button(window, text="Total Expired Price:",font=("Arial", 12, "bold"),bg="light green",fg="dark blue",padx=10, pady=5).place(x=20, y=353)

    window.mainloop()

create_product_table_window(expired_items)