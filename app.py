import csv
import datetime
import pandas as pd
from models import (Base, session, Inventory, engine)
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
            price = int(row[1] * 100)
            quantity = row[2]
            date = datetime.datetime.strptime(row[3], "%B, %d, %Y")
            session.add
        session.commit()
        #print()

# def clean_date(data):
#     dateparse = datetime.datetime.strptime("date" "%B, %d, %Y")
#     df = pd.read_csv(parse_dates=['datetime'], date_parser=dateparse)
#     # months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
#     #           'November', 'December']
#     # for date in data:
#     #     split_date = date.split("/")
#     #     month = split_date[0]   # int(months.index(split_date[0]) + 1)
#     #     day = split_date[1]        # .split("/"))
#     #     year = split_date[2]
#     #     return datetime.date(year, month, day)

# def clean_price(price_str):
#

# def view_inventory(): #v
#     product_id = input("Enter the id of the product you want to view: ")
#     # if product_id not in product_id column:
#     #     print("Not a valid id")
#     #     product_id = input("Enter the id of the product you want to view: ")
#
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

if __name__ == "__main__":
    #menu()
    add_csv()
    # Base.metadata.create_all(engine)
#     # app()
#     # add_csv()
#     clean_price(1.25)

