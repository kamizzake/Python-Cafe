import json
import os


class Item:
    def __init__(self, name, cat, price, stock):
        self.name = name
        self.cat = cat
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "name": self.name,
            "cat": self.cat,
            "price": self.price,
            "stock": self.stock,
        }


class Manager:
    def __init__(self):
        self.menu = []
        self.orders = []
        self.ensure_data()
        self.load()

    def ensure_data(self):
        if not os.path.exists("data"):
            os.makedirs("data")

        for f in ["data/menu.json", "data/orders.json"]:
            if not os.path.exists(f):
                with open(f, "w") as file:
                    json.dump([], file)

    def load(self):
        if os.path.exists("data/menu.json"):
            try:
                with open("data/menu.json", "r") as f:
                    content = f.read().strip()
                    if content:
                        f.seek(0)
                        data = json.load(f)
                        self.menu = [
                            Item(d["name"], d["cat"], d["price"], d["stock"])
                            for d in data
                        ]
                    else:
                        self.menu = []
            except json.JSONDecodeError:
                self.menu = []

        if os.path.exists("data/orders.json"):
            try:
                with open("data/orders.json", "r") as f:
                    content = f.read().strip()
                    if content:
                        f.seek(0)
                        self.orders = json.load(f)
                    else:
                        self.orders = []
            except json.JSONDecodeError:
                self.orders = []

    def save(self):
        menu_data = [i.to_dict() for i in self.menu]

        with open("data/menu.json", "w") as f:
            json.dump(menu_data, f, indent=4)

        with open("data/orders.json", "w") as f:
            json.dump(self.orders, f, indent=4)

    def add(self, name, cat, price, stock):
        new_item = Item(name, cat, price, stock)
        self.menu.append(new_item)
        self.save()

    def find(self, query):
        results = []
        for i in self.menu:
            if query.lower() in i.name.lower():
                results.append(i)
        return results
