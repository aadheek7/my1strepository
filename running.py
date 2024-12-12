from tkinter import *
from tkinter import ttk
from tabulate import tabulate

headers = ["Date", "Particulars", "Receipts", "Issues", "Balance"]
receipt_headers = ["Qty", "Rate", "Amount"]
balance_headers = ["Qty", "Rate", "Amount"]

dates = []
particulars = []
balance_list = []
receipt_list = []
issue_list = []

stores_ledger_account = []

# GUI Setup
root = Tk()
root.title("Stores Ledger Account")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

status_label = Label(root, text="", font=("consolas", 16), fg="green")
status_label.pack()

# Opening Stock Widgets
opening_stock_frame = LabelFrame(main_frame, text="Opening Stock", font=("consolas", 16))
opening_stock_frame.pack(fill=X, padx=10, pady=5)

Label(opening_stock_frame, text="Date:", font=("consolas", 16)).grid(row=0, column=0, padx=5, pady=5)
opening_stock_date = Entry(opening_stock_frame, font=("consolas", 16), relief = "sunken", borderwidth = 6)
opening_stock_date.grid(row=0, column=1, padx=5, pady=5)

Label(opening_stock_frame, text="Qty:", font=("consolas", 16)).grid(row=0, column=2, padx=5, pady=5)
opening_stock_qty = Entry(opening_stock_frame, font=("consolas", 16), relief = "sunken", borderwidth = 6)
opening_stock_qty.grid(row=0, column=3, padx=5, pady=5)

Label(opening_stock_frame, text="Rate:", font=("consolas", 16)).grid(row=0, column=4, padx=5, pady=5)
opening_stock_rate = Entry(opening_stock_frame, font=("consolas", 16), relief = "sunken", borderwidth = 6)
opening_stock_rate.grid(row=0, column=5, padx=5, pady=5)

Button(opening_stock_frame, text="Add Opening Stock", font=("consolas", 16), command=lambda: add_opening_stock(), borderwidth = 4).grid(row=1, column=0, columnspan = 6, padx=5, pady=5)

# Receipt Widgets
receipt_frame = LabelFrame(main_frame, text="Goods Receipt", font=("consolas", 16))
receipt_frame.pack(fill=X, padx=10, pady=5)

Label(receipt_frame, text="Date:", font=("consolas", 16)).grid(row=0, column=0, padx=5, pady=5)
receipt_date = Entry(receipt_frame, font=("consolas", 16), relief = "sunken", borderwidth = 6)
receipt_date.grid(row=0, column=1, padx=5, pady=5)

Label(receipt_frame, text="Qty:", font=("consolas", 16)).grid(row=0, column=2, padx=5, pady=5)
receipt_qty = Entry(receipt_frame, font=("consolas", 16), relief = "sunken", borderwidth = 6)
receipt_qty.grid(row=0, column=3, padx=5, pady=5)

Label(receipt_frame, text="Rate:", font=("consolas", 16)).grid(row=0, column=4, padx=5, pady=5)
receipt_rate = Entry(receipt_frame, font=("consolas", 16), relief = "sunken", borderwidth = 6)
receipt_rate.grid(row=0, column=5, padx=5, pady=5)

Button(receipt_frame, text="Add Goods Receipt", font=("consolas", 16), command=lambda: add_receipt(), borderwidth = 4).grid(row=1, column=0, columnspan = 6, padx=5, pady=5)

# Issue Widgets
issue_frame = LabelFrame(main_frame, text="Goods Issue", font=("consolas", 16))
issue_frame.pack(fill=X, padx=10, pady=5)

Label(issue_frame, text="Date:", font=("consolas", 16)).grid(row=0, column=0, padx=5, pady=5)
issue_date = Entry(issue_frame, font=("consolas", 16), relief = "sunken", borderwidth = 6)
issue_date.grid(row=0, column=1, padx=5, pady=5)

Label(issue_frame, text="Qty:", font=("consolas", 16)).grid(row=0, column=2, padx=5, pady=5)
issue_qty = Entry(issue_frame, font=("consolas", 16), relief = "sunken", borderwidth = 6)
issue_qty.grid(row=0, column=3, padx=5, pady=5)

Button(issue_frame, text="Issue Materials", font=("consolas", 16), command=lambda: add_issue(), borderwidth = 4).grid(row=1, column=0, columnspan = 6, padx=5, pady=5)

# Finalize Button
Button(main_frame, text="Display Stores Ledger Account", font=("consolas", 16), command=lambda: display_ledger(), borderwidth = 10).pack(pady=10)

# Functions
def add_opening_stock():
    date = opening_stock_date.get()
    qty = int(opening_stock_qty.get())
    rate = float(opening_stock_rate.get())
    amount = qty * rate
    dates.append(date)
    particulars.append("Balance B/d")
    balance_list.append([qty, rate, amount])
    balance_table = tabulate(balance_list, headers=balance_headers, tablefmt="fancy_grid")
    stores_ledger_account.append([date, "Balance B/d", "", "", balance_table])

    # Clear the entries
    opening_stock_date.delete(0, END)
    opening_stock_qty.delete(0, END)
    opening_stock_rate.delete(0, END)

    status_label.config(text="Opening stock recorded!")

def add_receipt():
    date = receipt_date.get()
    qty = int(receipt_qty.get())
    rate = float(receipt_rate.get())
    amount = qty * rate
    dates.append(date)
    particulars.append("G.R.N. No.")
    receipt_list.append([qty, rate, amount])
    balance_list.append([qty, rate, amount])
    receipt_table = tabulate([receipt_list[-1]], headers=receipt_headers, tablefmt="fancy_grid")
    balance_table = tabulate(balance_list, headers=balance_headers, tablefmt="fancy_grid")
    stores_ledger_account.append([date, "G.R.N. No.", receipt_table, "", balance_table])

    # Clear the entries
    receipt_date.delete(0, END)
    receipt_qty.delete(0, END)
    receipt_rate.delete(0, END)

    status_label.config(text="Goods receipt recorded!")

def add_issue():
    date = issue_date.get()
    units_to_be_issued = int(issue_qty.get())
    dates.append(date)
    particulars.append("M.R. No.")
    issue_list.clear()
    total_available_qty = sum(item[0] for item in balance_list)

    if units_to_be_issued > total_available_qty:
        status_label.config(text="Insufficient stock!")
        return

    i = 0
    while i < len(balance_list):
        if units_to_be_issued >= balance_list[i][0]:
            units_to_be_issued -= balance_list[i][0]
            issue_list.append(balance_list[i])
            balance_list.pop(i)
        else:
            balance_list[i][0] -= units_to_be_issued
            balance_list[i][2] = balance_list[i][0] * balance_list[i][1]
            if units_to_be_issued != 0:
                issue_list.append([units_to_be_issued, balance_list[i][1], units_to_be_issued * balance_list[i][1]])
            break

    issue_table = tabulate(issue_list, headers=receipt_headers, tablefmt="fancy_grid")
    balance_table = tabulate(balance_list, headers=balance_headers, tablefmt="fancy_grid")
    stores_ledger_account.append([date, "M.R. No.", "", issue_table, balance_table])

    # Clear the entries
    issue_date.delete(0, END)
    issue_qty.delete(0, END)

    status_label.config(text="Materials Issued!")

def display_ledger():
    stores_ledger_account_table = tabulate(stores_ledger_account, headers=headers, tablefmt="fancy_grid")

    root = Tk()
    root.title("Stores Ledger Account")

    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=True)

    canvas = Canvas(main_frame)
    canvas.pack(fill=BOTH, side=LEFT, expand=True)

    v_scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    v_scroll.pack(side=RIGHT, fill=Y)

    h_scroll = ttk.Scrollbar(root, orient=HORIZONTAL, command=canvas.xview)
    h_scroll.pack(side=BOTTOM, fill=X)

    canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

    project_frame = Frame(canvas)
    project_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=project_frame, anchor="nw")

    Label(project_frame, text=stores_ledger_account_table, font=("consolas", 16), relief = "sunken", borderwidth = 6).pack()
    balance_amount = 0
    tot_units = 0
    for i in balance_list:
        balance_amount += i[2]
        tot_units += i[0]
    Label(project_frame, text="Closing Stock = "+str(tot_units)+" units, valued at Rs. "+str(balance_amount), font = ("consolas", 16), borderwidth = 0).pack()

    root.mainloop()

root.mainloop()
