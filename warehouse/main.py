"""
    Warehouse program
    functionality:
        - Repeated menu
        1: Register items to a catalog
            id (auto generated)
            title (str)
            category (str)
            price (float)
            stock (int)

        2: List the items on the catalog

        3: Update the stock manually
            - display the list of items
            - ask user tot choose an id
            - read the id
            - travel the catalog array and find the item with id = id
            - ask for new stock value 
            - update stock

        4. How much money in inventory
            get each item, price * stock add it tototal variable

        5. Remove an item from the catalog
            -display list of items
            -ask user for an id
            -read id
            -travel array to find id
            -if found remove item from catalog
            -else show an error to the user
        
        6. Register a sale
            -display list of items
            -ask user for an id
            -read id
            -travel array to find id
            -if found
                -ask for amount sold
                -show total sale price
                -decrease amount sold
"""

from menu import clear, print_menu, print_header
from item import Item
import pickle

# global variables
catalog = []  # list
data_file = 'warehouse.data'
# functions


def save_catalog():
    global data_file  # must import global variables into the funtion
    writer = open(data_file, 'wb')  # open or create a file and write binary
    pickle.dump(catalog, writer)
    writer.close()  # close the file
    print('** Saved **')


def read_catalog():
    global data_file
    try:
        reader = open(data_file, 'rb')  # reads binary file
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        print('** Data Loaded ** ' + str(len(catalog)) + ' Items loaded....')

    except:
        print('** ERROR ** - Could not load data from data file')


def register_item():
    print_header('Register new Item')

    try:
        title = input("Item Title:  ")
        cat = input("Item Category: ")
        price = float(input("Item Price: "))
        stock = int(input("Items in Stock: "))

        # create an instance of Item (an object)
        id = 1
        if(len(catalog) > 0):
            last = catalog[-1]
            id = last.id + 1
        new_item = Item(1, title, cat, price, stock)
        catalog.append(new_item)

        print("Item created ")

    except ValueError:
        print("** Error: incorrect value, try again")
    except:
        print("** Error, try again")


def display_catalog():
    print_header("Items in your catalog")
    print('Id'.rjust(2) + '   ' + 'Title'.ljust(25) + '   ' +
          'Category'.ljust(15) + '   ' + 'Price'.rjust(15) + '   ' + 'Stock'.rjust(5))

    for item in catalog:
        print(str(item.id).rjust(2)
              + " | " + item.title.ljust(25)
              + " | " + item.category.ljust(10)
              + " | " + str(item.price).rjust(15)
              + " | " + str(item.stock).rjust(5))
        print('-' * 75)


def update_stock():
    display_catalog()
    update_id = input('Choose an item id: ')

    found = False
    for item in catalog:
        if(str(item.id) == update_id):
            found = True
            new_stock = input("Please provide new stock number: ")
            item.stock = int(new_stock)

    if(not found):
        print('** ERROR ** - Selected id does not exist')


def remove_item():
    display_catalog()
    remove_id = input('Choose an item id: ')

    found = False
    for item in catalog:
        if(str(item.id) == remove_id):
            found = True
            catalog.remove(item)

    if(not found):
        print('** ERROR ** - Selected id does not exist')


def checkout_sale():
    display_catalog()
    sale_id = input('Choose an item id: ')

    found = False
    for item in catalog:
        if(str(item.id) == sale_id):
            found = True
            qty_sold = int(input('Number of items sold: '))
            item.stock = item.stock - qty_sold
            total = qty_sold * item.price
            print('Checkout total: $' + str(total))

    if(not found):
        print('** ERROR ** - Selected id does not exist')


def stock_value():
    total = 0.0
    for item in catalog:
        total += (item.price * item.stock)
    print('Stock value: $' + str(total))


# instuctions
opc = ''
while(opc is not 'x'):
    clear()
    print_menu()

    opc = input('Please select an option: ')

    if(opc == '1'):
        register_item()
    elif(opc is '2'):
        display_catalog()

    input('Press Enter to continue')
