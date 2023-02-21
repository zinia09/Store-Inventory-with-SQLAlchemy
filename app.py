import csv
import datetime
from models import (Base, session, Inventory, engine)
import models
from sqlalchemy import delete
import sqlite3

def menu():
    print("STORE INVENTORY")
    print("""\rv) View product inventory
             \ra) Add product 
             \rb) Make a backup of the inventory""")
    menu = ['v', 'b', 'a']
    choice = input("Enter the letter 'v', 'b', or 'a': ")
    while choice not in menu:
        choice = input("Enter the letter 'v', 'b', or 'a': ")
    if choice == "v":
        view_inventory()
    elif choice == "a":
        add_product()
    elif choice == "b":
        backup()

def add_csv():
    with open("inventory.csv") as csvfile:
        data = csv.reader(csvfile)
        next(data)
        for row in data:
            product = row[0]
            price = int(float(row[1].strip('$')) * 100)
            quantity = int(row[2])
            date = datetime.datetime.strptime(row[3], "%m/%d/%Y").date()
            new_inventory = Inventory(product_name=product, product_quantity=quantity, product_price=price, date_updated=date.isoformat())
            session.add(new_inventory)
        session.commit()


def view_inventory():
    view_id = input("Enter the id of the product you wish to view: ")
    result = session.query(Inventory).get(view_id)
    print(result)


def add_product():   # a
    with open("inventory.csv") as csvfile:
        data = csv.writer(csvfile)

        try:
            add_product_name = input("Name: ")
            add_product_price = int(input("Price (format: 55.55): "))
            add_product_quantity = int(input("Quantity: "))
            add_date_updated = datetime.strptime(input("Date updated (format: mm/dd/yyyy): "), "%m/%d/%Y").date()
            add_product = Inventory(product_name=add_product_name,
                                    product_quantity=add_product_quantity,
                                    product_price=add_product_price,
                                    date_updated=add_date_updated)
            session.add(add_product)
            session.commit()
            print("Product added!")
            # print(data)
        except ValueError:
            input("Please enter date as mm/dd/yyyy and price as 55.55")
            return

        # obj = session.query(Inventory).filter_by(product_id=28).first()     # to delete a product
        # session.delete(obj)
        # session.commit()

        # for instance in session.query(Inventory):                          # to check if it's been deleted
        #     print(instance)


def backup():
    with open("backup.csv", "w", newline="") as csvfile:
        fieldnames = ["product_name", "product_price", "product_quantity", "date_updated"]
        backup_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        backup_writer.writeheader()
        for product in session.query(Inventory):
            backup_writer.writerow({
                "product_name": product.product_name,
                "product_price": int(float(str(product.product_price).strip('$')) * 100),
                "product_quantity": product.product_quantity,
                "date_updated": datetime.strptime(product.date_updated.strip("%m/%d/%Y"), "%m/%d/%Y").date()
            })


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    add_csv()
    menu()
