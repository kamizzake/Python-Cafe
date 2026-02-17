import utils


def run(mgr):

    utils.clear()
    utils.header("Admin Login")

    pwd = input("Input Password: ")
    if pwd != "ciao123":
        print("\nAccess Denied!")
        utils.pause()
        return

    while True:
        utils.clear()
        utils.header("Admin Panel")
        print("1) Add New Item")
        print("2) Update Stock")
        print("3) View Sales")
        print("4) Prev Menu")

        opt = input("\nPick Option: ")

        if opt == "1":
            utils.header("Add Item")
            try:
                name = input("Item Name: ").title()
                cat = input("Category: ").title()
                price = int(input("Price: "))
                stock = int(input("Stock Qty: "))

                mgr.add(name, cat, price, stock)
                print("\nItem Added Successfully!")
            except ValueError:
                print("\nError: Price/Stock Must Be In Numbers...")
            utils.pause()

        elif opt == "2":
            utils.header("Update Stock")
            name = input("Input Item Name: ")
            found = mgr.find(name)

            if not found:
                print("\nItem Not Found.")
            else:
                for item in found:
                    print(f"Found: {item.name} | Stock: {item.stock}")
                    try:
                        new = int(input(f"New Stock For {item.name}: "))
                        item.stock = new
                        mgr.save()
                        print("Stock Updated!")
                    except ValueError:
                        print("Invalid Number...")
            utils.pause()

        elif opt == "3":
            utils.clear()
            utils.header("Sales Report")
            rev = 0
            count = 0

            for order in mgr.orders:
                rev += order["total"]
                count += 1

            print(f"Total Orders = {count}")
            print(f"Total Revenue = ${rev}")
            utils.pause()

        elif opt == "4":
            break

        else:
            print("\nInvalid Option...")
            utils.pause()
