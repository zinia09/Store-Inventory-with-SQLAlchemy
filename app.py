import csv
import datetime
from models import (Base, session, Inventory, engine)
import models


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
    elif choice == "b":  # backup
        pass

def add_csv():
    with open ("inventory.csv") as csvfile:
        data = csv.reader(csvfile)
        next(data)
        for row in data:
            product = row[0]
            price = int(float(row[1].strip('$')) * 100)
            quantity = int(row[2])
            date = datetime.datetime.strptime(row[3], "%m/%d/%Y")

            new_inventory = Inventory(
                product_name=product, product_quantity=quantity, product_price=price, date_updated=date)
        #     session.add(new_inventory)
        # session.commit()


def view_inventory():
    product_to_view = input("Enter the id of the product you want to view: ")
    for instance in session.query(Inventory):
        try:
            if product_to_view == instance.product_id:
                print(f"{instance.product_name}, Quantity: {instance.product_quantity}, Price: {instance.product_price}")
        except product_to_view not in instance.product_id:
            product_to_view = input("Enter the id of the product you want to view: ")


def add_product(): #a
     with open ("inventory.csv") as csvfile:
        data = csv.writer(csvfile)
        try:
            add_product_name = input("Name: ")
            add_product_price = input("Price: ")
            add_product_quantity = input("Quantity: ")
            add_date_updated = input("Date updated: ") # datetime.today
            add_product = Inventory(product_name=add_product_name,
                                    product_quantity=add_product_quantity,
                                    product_price=add_product_price,        # assign an id somehow?
                                    date_updated=add_date_updated)
            session.add(add_product)
            session.commit()
            print("Product added!")
        except ValueError:
            input("Please enter date as mm/dd/yyyy and price as 55.55")
            return

def backup():    #b
    pass



if __name__ == "__main__":
    # Base.metadata.create_all(engine)
    menu()
