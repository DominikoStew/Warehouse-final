import os


def print_menu():
    print("-" * 30)
    print("Warehouse control system")
    print("-" * 30)

    print('[1] Register new Items')
    print('[2] Show Catalog')
    print('[3] Update Stock')
    print('[4] Stock Value')
    print('[5] Remove Item')
    print('[6] Sale')
    print('[x] Close')


def print_header(title):
    clear()
    print('-' * 50)
    print('' + title)
    print('-' * 50)


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')
