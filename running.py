from tkinter import *
from tkinter import ttk
from tabulate import tabulate

headers = ["Date", "Particulars", "Receipts", "Issues", "Balance"]
sub_headers = ["Qty", "Rate", "Amount"]

balance_list = []
balance_dict = {}

issue_list = []
issue_dict = {}

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

# Purchase return Widgets
pr_frame = LabelFrame(main_frame, text="Purchase Return", font=("consolas", 16))
pr_frame.pack(fill=X, padx=10, pady=5)

Label(pr_frame, text="Date:", font=("consolas", 16)).grid(row=0, column=0, padx=5, pady=5)
pr_date = Entry(pr_frame, font=("consolas", 16), relief = "sunken", borderwidth = 6)
pr_date.grid(row=0, column=1, padx=5, pady=5)

Label(pr_frame, text="Date of Purchase:", font=("consolas", 16)).grid(row=0, column=2, padx=5, pady=5)
pr_dateofp = Entry(pr_frame, font=("consolas", 16), relief = "sunken", borderwidth = 6)
pr_dateofp.grid(row=0, column=3, padx=5, pady=5)

Label(pr_frame, text="Qty:", font=("consolas", 16)).grid(row=0, column=4, padx=5, pady=5)
pr_qty = Entry(pr_frame, font=("consolas", 16), relief = "sunken", borderwidth = 6)
pr_qty.grid(row=0, column=5, padx=5, pady=5)

Button(pr_frame, text="Return Materials", font=("consolas", 16), command=lambda: add_pr(), borderwidth = 4).grid(row=1, column=0, columnspan = 6, padx=5, pady=5)


# Finalize Button
Button(main_frame, text="Display Stores Ledger Account", font=("consolas", 16), command=lambda: display_ledger(), borderwidth = 10).pack(pady=10)

# Functions
def add_opening_stock():
    date = opening_stock_date.get()
    qty = int(opening_stock_qty.get())
    rate = float(opening_stock_rate.get())
    amount = qty * rate
    balance_list.append([qty, rate, amount])
    balance_dict[date] = [qty, rate, qty * rate]
    formatted_balance_list = []
    formatted_balance_list.append([f"{qty:,.0f}", rate, f"{amount:,.2f}"])
    balance_table = tabulate(formatted_balance_list, headers=sub_headers, tablefmt="fancy_grid")
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
    balance_list.append([qty, rate, amount])
    balance_dict[date] = [qty, rate, qty * rate]
    formatted_balance_list = []
    for i in balance_list:
        formatted_balance_list.append([f"{i[0]:,.0f}", i[1], f"{i[2]:,.2f}"])
    receipt_table = tabulate([[f"{qty:,.0f}", rate, f"{amount:,.2f}"]], headers=sub_headers, tablefmt="fancy_grid")
    balance_table = tabulate(formatted_balance_list, headers=sub_headers, tablefmt="fancy_grid")
    stores_ledger_account.append([date, "Goods Received", receipt_table, "", balance_table])

    # Clear the entries
    receipt_date.delete(0, END)
    receipt_qty.delete(0, END)
    receipt_rate.delete(0, END)

    status_label.config(text="Goods receipt recorded!")

def add_issue():
    date = issue_date.get()
    units_to_be_issued = int(issue_qty.get())
    total_available_qty = sum(item[0] for item in balance_list)

    if units_to_be_issued > total_available_qty:
        status_label.config(text="Insufficient stock!")
        return

    i = 0
    key_mapping = list(balance_dict.keys())
    while i < len(balance_list):
        if units_to_be_issued >= balance_list[i][0]:
            units_to_be_issued -= balance_list[i][0]
            issue_list.append(balance_list[i])

            # Also remove the corresponding entry from the balance_dict
            key_to_remove = key_mapping[i]
            balance_dict.pop(key_to_remove)

            # Remove the entry from balance_list and key_mapping
            balance_list.pop(i)
            key_mapping.pop(i)
        else:
            balance_list[i][0] -= units_to_be_issued
            balance_list[i][2] = balance_list[i][0] * balance_list[i][1]
            key_to_update = key_mapping[i]
            balance_dict[key_to_update][0] = balance_list[i][0]
            balance_dict[key_to_update][2] = balance_list[i][2]
            if units_to_be_issued != 0:
                issue_list.append([units_to_be_issued, balance_list[i][1], units_to_be_issued * balance_list[i][1]])
            break

    formatted_issue_list = []
    for i in issue_list:
        formatted_issue_list.append([f"{i[0]:,.0f}", i[1], f"{i[2]:,.2f}"])
    formatted_balance_list = []
    for i in balance_list:
        formatted_balance_list.append([f"{i[0]:,.0f}", i[1], f"{i[2]:,.2f}"])

    issue_table = tabulate(formatted_issue_list, headers=sub_headers, tablefmt="fancy_grid")
    balance_table = tabulate(formatted_balance_list, headers=sub_headers, tablefmt="fancy_grid")
    stores_ledger_account.append([date, f"Materials Issued\n({units_to_be_issued:,.0f}) units", "", issue_table, balance_table])

    issue_date.delete(0, END)
    issue_qty.delete(0, END)

    status_label.config(text="Materials Issued!")

def add_pr():
    issue_list.clear()
    date = pr_date.get()
    dateofp = pr_dateofp.get()
    qty = int(pr_qty.get())

    if balance_dict[dateofp][0] >= qty:
        balance_dict[dateofp][0] -= qty 
        balance_dict[dateofp][2] = balance_dict[dateofp][0] * balance_dict[dateofp][1]

        issue_list.append([qty, balance_dict[dateofp][1], qty * balance_dict[dateofp][1]])

        balance_list.clear()
        if balance_dict[dateofp][0] != 0:
            for i in balance_dict.values():
                balance_list.append(i)
        else:
            balance_dict.pop(dateofp)
            for i in balance_dict.values():
                balance_list.append(i)


        formatted_issue_list = []
        for i in issue_list:
            formatted_issue_list.append([f"{i[0]:,.0f}", i[1], f"{i[2]:,.2f}"])
        formatted_balance_list = []
        for i in balance_list:
            formatted_balance_list.append([f"{i[0]:,.0f}", i[1], f"{i[2]:,.2f}"])

        issue_table = tabulate(formatted_issue_list, headers = sub_headers, tablefmt = "fancy_grid")
        balance_table = tabulate(formatted_balance_list, headers = sub_headers, tablefmt = "fancy_grid")

        stores_ledger_account.append([date, f"Materials Returned\n(or)\nShortage\n({qty:,.0f}) units\nof the goods received on {dateofp}", "", issue_table, balance_table])

        pr_date.delete(0, END)
        pr_dateofp.delete(0, END)
        pr_qty.delete(0, END)

        status_label.config(text="Materials Returned!")

    else:
        status_label.config(text="Quantity of materials to be returned exceeds the Quantity of materials Purchased on that date! ")
        return

def add_sr():
    pass

def display_ledger():
    stores_ledger_account_table = tabulate(stores_ledger_account, headers=headers, tablefmt="fancy_grid")
    print(issue_list)

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
    Label(project_frame, text="Closing Stock = "+f"{tot_units:,.0f}"+" units, valued at Rs. "+f"{balance_amount:,.2f}", font = ("consolas", 16), borderwidth = 0).pack()

    root.mainloop()

root.mainloop()
