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

while True:
    OpeningStock = input("""Press (y) to Enter Opening Stock's details
                                            (or) 
Press (n) to continue
----------------------------------------------> """)
    if OpeningStock.lower() == "y":
        dates.append(input("Enter the date for entering Opening Stock's Details in (dd-mm-yy) format:--> "))
        particulars.append("Balance B/d")
        qty = int(input("Enter qty:--> "))
        rate = float(input("Enter rate:--> "))
        amount = qty * rate
        balance_list.append([qty, rate, qty * rate])
        balance_table = tabulate(balance_list, headers = balance_headers, tablefmt = "fancy_grid")
        stores_ledger_account.append([dates[-1], particulars[-1], "", "", balance_table])
        break

    elif OpeningStock.lower() == "n":
        break

    else:
        print("Invalid Entry!")

while True:
    choice = input("""Press (g) for recording the received goods
Press (i) for issuing goods(in FIFO Method)
Press (d) to see the stores ledger account
Press (e) to exit
-------------------------------------------->>> """)

    if choice.lower() == "g":
        date = input("Enter date(dd-mm-yyyy):--> ")
        qty = int(input("Enter qty:--> "))
        rate = float(input("Enter rate:--> "))
        amount = qty * rate

        dates.append(date)
        particulars.append("G.R.N. No.")
        receipt_list.append([qty, rate, qty * rate])
        balance_list.append([qty, rate, qty * rate])

        current_receipt = [receipt_list[-1]]

        receipt_table = tabulate(current_receipt, headers = receipt_headers, tablefmt = "fancy_grid")
        balance_table = tabulate(balance_list, headers = balance_headers, tablefmt = "fancy_grid")

        stores_ledger_account.append([dates[-1], particulars[-1], receipt_table, "", balance_table])

    elif choice.lower() == "i":
        issue_list.clear()
        dates.append(input("Enter date(dd-mm-yyyy):--> "))
        particulars.append("M.R. No.")
        units_to_be_issued = int(input("Units to be issued:--> "))
        total_available_qty = sum(item[0] for item in balance_list)

        if units_to_be_issued > total_available_qty:
            print("Insufficient Stock: Rs. ", units_to_be_issued - total_available_qty)
            
        i = 0
        while i < len(balance_list):
            if units_to_be_issued >= balance_list[i][0]:
                units_to_be_issued -= balance_list[i][0]
                issue_list.append(balance_list[i])
                balance_list.pop(i)
            else:
                balance_list[i][0] -= units_to_be_issued
                balance_list[i][2] = balance_list[i][0] * balance_list[i][1]
                issue_list.append([units_to_be_issued, balance_list[i][1], units_to_be_issued * balance_list[i][1]])
                break

        issue_table = tabulate(issue_list, headers = receipt_headers, tablefmt = "fancy_grid")
        balance_table = tabulate(balance_list, headers = balance_headers, tablefmt = "fancy_grid")

        stores_ledger_account.append([dates[-1], particulars[-1], "", issue_table, balance_table])

    elif choice.lower() == "d":
        stores_ledger_account_table = tabulate(stores_ledger_account, headers = headers, tablefmt = "fancy_grid")
        print(stores_ledger_account_table)

    elif choice.lower() == "e":
        break

    else:
        print("Invalid Entry!")
