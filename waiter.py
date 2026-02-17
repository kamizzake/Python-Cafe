import utils


def run(mgr):
    while True:
        utils.clear()
        utils.header("Waiter Menu")
        print("1) New Order")
        print("2) Find Item")
        print("3) Prev Menu")

        opt = input("\nPick Option: ")

        if opt == "1":
            new_order(mgr)
        elif opt == "2":
            find_item(mgr)
        elif opt == "3":
            break
        else:
            print("Invalid Option...")
            utils.pause()


def new_order(mgr):
    utils.clear()
    utils.header("New Order")

    if not mgr.menu:
        print("\nMenu Empty! Add Items...")
        utils.pause()
        return

    cart = []
    total = 0

    while True:
        utils.clear()
        utils.header("Taking Order")

        total = sum(i["price"] * i["qty"] for i in cart)
        print(f"Cart Total = ${total}\n")

        cats = []
        for i in mgr.menu:
            if i.cat not in cats:
                cats.append(i.cat)

        print("Categories:")
        for idx, c in enumerate(cats, 1):
            print(f"{idx}. {c}")
        print("\nC. Checkout / Finish")
        print("X. Cancel Order")

        choice = input("\nSelect: ").upper()

        if choice == "X":
            if cart:
                print("\nRestoring Stock...")
                for item in cart:
                    for org in mgr.menu:
                        if org.name == item["name"]:
                            org.stock += item["qty"]
                            break
            print("Order Cancelled :c")
            utils.pause()
            return

        if choice == "C":
            if not cart:
                print("Cart Empty!")
                utils.pause()
                continue

            utils.header("Finalize Order")
            while True:
                phone = input("Customer Phone (11 Digits): ")
                if utils.valid(r"^\d{11}$", phone):
                    break
                print("Invalid! Must Be 11 digits (e.g 03001234567)")

            order = {"phone": phone, "items": cart, "total": total}
            mgr.orders.append(order)

            mgr.save()

            print("\nOrder Placed Successfully!")
            print(f"Final Total = ${total}")
            utils.pause()
            return

        try:
            c_idx = int(choice) - 1
            if 0 <= c_idx < len(cats):
                selected_cat = cats[c_idx]
                add_item_to_cart(mgr, selected_cat, cart)
            else:
                print("Invalid Category...")
                utils.pause()
        except ValueError:
            print("Invalid Input...")
            utils.pause()


def add_item_to_cart(mgr, cat, cart):
    utils.clear()
    utils.header(f"{cat} Menu")

    items = [i for i in mgr.menu if i.cat == cat]

    for idx, item in enumerate(items, 1):
        print(f"{idx}. {item.name} (${item.price}) [Stock: {item.stock}]")

    try:
        sel = int(input("\nSelect Item ID: "))
        if sel == 0:
            return

        target = items[sel - 1]

        if target.stock <= 0:
            print("Out of Stock!")
            utils.pause()
            return

        qty = int(input(f"How Many {target.name} ? "))

        if qty <= 0:
            print("Quantity Must Be > 0")
            utils.pause()
            return

        if qty > target.stock:
            print(f"Not Enough Stock! Only {target.stock} Available")
            utils.pause()
        else:
            target.stock -= qty

            cart.append({"name": target.name, "price": target.price, "qty": qty})
            print("Added To Cart.")

    except (ValueError, IndexError):
        print("Invalid Selection...")
        utils.pause()


def find_item(mgr):
    utils.clear()
    utils.header("Search Item")

    query = input("Enter Item Name: ")
    res = mgr.find(query)

    print(f"\nFound {len(res)} Items:")
    for item in res:
        print(f"- {item.name} | {item.cat} | ${item.price} | Stock: {item.stock}")

    utils.pause()
