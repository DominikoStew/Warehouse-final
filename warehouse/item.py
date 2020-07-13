
class Item:
    id = 0
    title = ''
    category = ''
    price = 0.0
    stock = 0

    # class constructor
    def __init__(self, id, title, cat, price, stock):
        self.id = id
        self.title = title
        self.category = cat
        self.price = price
        self.stock = stock
