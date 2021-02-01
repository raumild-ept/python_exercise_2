class InventoryManagement:
#Creating class.
    def __init__(self, product_name, product_quantity):
        #Initializing class.
        #prouct_name is name of the product.
        #product_quantity is initial quantity of product.
        self.product_name = product_name
        self.product_quantity = int(product_quantity)
    def purchase(self,qty):
        #Fnction expects one argument.
        #Takes quantity as qty
        self.product_quantity += qty
        print(f"{qty} {self.product_name} Purchased.")
    def sell(self, qty):
        self.product_quantity -= qty
        print(f"{qty} {self.product_name} Sold.")
        #decreasing qty.
    def product_data(self):
        print(f"Current stock is {self.product_quantity} {self.product_name}s.")
    #product_Data is printed.
name_product = input("Enter Product Name: ")
quantity_product = input("Enter Quantity")
obj1 = InventoryManagement(name_product,quantity_product)
#passing name_product and quantity_product as parameter
answer = True
while answer:
    print("""
    1.Purchase product.
    2.Sell Product.
    3.View Quantity.
    4.Exit.
    """)
    answer = int(input("What do you want to use?"))
    if answer == 1:
        qty = int(input("How much product you want to purchase?"))
        obj1.purchase(qty)
        print("Product Purchased.")
    elif answer == 2:
        qty = int(input("How much product you want to sell?"))
        if qty <= obj1.product_quantity:#if quantity to sell is lesser or equal to available quantity.
            obj1.sell(qty)
            print("Product Sold.")
        else:
            print("You can not sell more than you have.")
    elif answer == 3:
        print(f"You have {obj1.product_quantity} {obj1.product_name}s. ")
    elif answer == 4:
        answer = False
    else:
        print("Enter correct input.")