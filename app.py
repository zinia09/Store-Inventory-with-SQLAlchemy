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
    if choice == "v":  # View product inventory
        pass
    elif choice == "a":  # add product
        pass
    elif choice == "b":  # backup
        pass
def add_csv():
    with open ("inventory.csv") as csvfile:
        data = csv.reader(csvfile)        #reader only?
        next(data)
        for row in data:
            product = row[0]
            price = int(float(row[1].strip('$')) * 100)
            quantity = int(row[2])
            date = datetime.datetime.strptime(row[3], "%m/%d/%Y")
            session.add
            #print(price)
        session.commit()

def view_inventory(): #v
    product_to_view = input("Enter the id of the product you want to view: ")
    if product_to_view == models.Inventory.product_id:
        for product in models.session.query(models.Inventory.product_id):
            print(product)
    else:
        print("Not a valid id")

view_inventory()

# def add_product(): #a
#     try:
#         add_product_name = input("Name: ")
#         add_product_price = input("Price: ")
#         price = clean_price()
#         add_product_quantity = input("Quantity: ")
#         add_date_updated = input("Date updated: ")
#         date = clean_date()
#         print("Product added!")
#     except ValueError:
#         input("Please enter date as mm/dd/yyyy and price as 55.55")
#         return

# def backup():    #b
#     pass
#
#

# if __name__ == "__main__":
#     Base.metadata.create_all(engine)
#     add_csv()
#     view_inventory()
#     # app()
#     # add_csv()

