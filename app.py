import csv
import datetime
from datetime import date
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
        choice = input("Invalid option. Please enter 'v', 'b', or 'a' from the menu:  ")
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
            new_inventory = Inventory(product_name=product, product_quantity=quantity, product_price=price, date_updated=date)
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
            add_product_quantity = int(input("Quantity: "))
            add_product_price = int(input("Price (Input in cents ex. 555): "))
            add_product_date = date.today()
            add_product = Inventory(product_name=add_product_name,
                                    product_quantity=add_product_quantity,
                                    product_price=add_product_price,
                                    product_date=add_product_date)
            session.add(add_product)
            session.commit()
            print("Product added!")
        except ValueError:
            print("Blimey! you entered the wrong format, rerun to try again")
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
            if product.date_updated is not None:
                backup_writer.writerow({
                    "product_name": product.product_name,
                    "product_price": int(float(str(product.product_price).strip('$')) * 100),
                    "product_quantity": product.product_quantity,
                    "date_updated": product.date_updated.strftime("%m/%d/%Y")
                })
            else:
                " "
        print("Backup complete!")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    add_csv()
    menu()
