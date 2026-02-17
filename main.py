import utils
import models
import admin
import waiter
import sys


def view_menu(mgr):
    utils.clear()
    utils.header(">>> Our Menu <<<")

    cats = {}
    for item in mgr.menu:
        if item.cat not in cats:
            cats[item.cat] = []
        cats[item.cat].append(item)

    if not cats:
        print("\nMenu Empty! Pleaes Add Items...")
    else:
        for cat, items in cats.items():
            print(f"\n--- {cat} ---")
            for item in items:
                print(f"{item.name:<25} ${item.price} (Stock: {item.stock})")

    utils.pause()


def about():
    utils.clear()
    utils.header(">>> About My Project <<<")
    print("\nPython Cafe System")
    print("By: Mueed Baloch")
    print("\nFeatures:")
    print("- Admin & Waiter Roles")
    print("- Secure Order Handling")
    print("- JSON Data Handling")
    utils.pause()


def main():
    mgr = models.Manager()

    while True:
        try:
            utils.clear()
            utils.header("Main Menu")
            utils.logo()

            print("1) Admin Panel (Login Required)")
            print("2) Waiter Menu (Take Orders)")
            print("3) View Full Menu")
            print("4) About Cafe")
            print("5) Exit")

            choice = input("\nInput Choice: ")

            if choice == "1":
                admin.run(mgr)

            elif choice == "2":
                waiter.run(mgr)

            elif choice == "3":
                view_menu(mgr)

            elif choice == "4":
                about()

            elif choice == "5":
                print("\nSaving Data...")
                mgr.save()
                print("Thank You And Ciao Ciao!")
                sys.exit()

            else:
                print("\nInvalid Choice, Please Input 1-5 Only...")
                utils.pause()

        except ValueError:
            print("\nError: Invalid Input Format...")
            utils.pause()
        except KeyboardInterrupt:
            print("\n\nForce Exit Detected. Saving data...")
            mgr.save()
            sys.exit()
        except Exception as e:
            print(f"\nAn Error Occurred: {e}")
            utils.pause()


if __name__ == "__main__":
    main()
