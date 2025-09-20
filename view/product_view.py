import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.title("Expired product report")
window.iconbitmap("")
window.geometry("800x400")

columns = ("product_id", "title", "brand", "price", "expiry_date")
tree = ttk.Treeview(window, columns=columns, show="headings")

Label(window, text="id", font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=11, height=2,
          bg="light green", fg="dark blue").place(x=20, y=9)
tree.column("product_id", width=3, anchor=tk.CENTER)

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
    tree.insert("", tk.END,values=(product["product_id"], product["title"], product["brand"], product["price"], product["expiry_date"]))
    tree.pack(pady=55, padx=20, fill=tk.BOTH, expand=True)

    total_price = tk.Label(window, text=total_price, width=33,bg="white",anchor=tk.W).place(x=210, y=363)
    Button(window, text="Total Expired Price:",font=("Arial", 12, "bold"),bg="light green",fg="dark blue",padx=10, pady=5).place(x=20, y=353)

window.mainloop()
