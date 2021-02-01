class InventoryManagement:
    #Class InventoryManagement takes one argument from constructor.
    #product_name is name of our product.
    def check_nulls(self, key_list):
        if self.product_dict[key_list]["Quantity"] == 0:
            return True

    def __init__(self, product_name):
        self.product_name = product_name
        self.product_dict = {}
        self.total_qty = 0
        self.index = 0
        #Defined dictionary and other attributes required.
    def sell_product(self):
        #Function to sell product.
        qty_of_product = int(input("Enter quantity of product you want to sell."))
        #input.
        if qty_of_product < self.total_qty:
            for index, value in self.product_dict.items():

                unit_price = int(self.product_dict[index]["Sub_Total"]) / int(
                    self.product_dict[index]["Quantity"])
                quant_exists = int(self.product_dict[index]["Quantity"])
                if value["Quantity"] >= qty_of_product:
                    #if quantity to sell is less than or equal to quantity available.
                    value.update({"Sub_Total":(unit_price*(quant_exists-qty_of_product)),"Quantity":(quant_exists-qty_of_product)})
                    #updates the dictionary at each key. Updating subtotal and quantity with new value,
                    self.total_qty -= qty_of_product
                    #total_available quant is increased.
                    #qty_of_product = 0
                    # if value["Quantity"] == 0:
                    #     #delete key where its quantity value is 0.
                    #  del self.product_dict[index]
                    #  break
                        #break the function as it has equated.
                elif value["Quantity"] < qty_of_product and qty_of_product < self.total_qty:
                    #elif will be executed if qty_to_sell is less than total quantity but is more than available in one place.
                    value["Sub_Total"] = 0
                    qty_of_product = qty_of_product - value["Quantity"]
                    #Quantity_to_Sell is decremented with amount that has been sold. It is iterated again till Quantity_to_sell is null.
                    value["Quantity"] = 0
                    #value is set to 0 as all quantity is sold from that place.
            # for index,value in self.product_dict.items():
            #     if self.product_dict[index]["Quantity"] == 0:
            #         del self.product_dict[index]
            #         break
            #loop to delete key from dictionary where value of quantity is zero.
        elif qty_of_product == self.total_qty:
            self.product_dict.clear()
        else:
            print("You can not sell more than you have.")
           #if quantity to e sold is more than available than error message will be printed

        key_list = list(self.product_dict.keys())
        filterd_list = filter((lambda a:self.product_dict[a]["Quantity"]==0),key_list)
        for x in filterd_list:
                del self.product_dict[x]


    def print_dict(self):
        print(f"Dic is {self.product_dict}.")
    #dictionary printing.

    def count(self, value_name_in_dict):
        sum_total = 0
        for index, value in self.product_dict.items():
            sum_total += int(self.product_dict[index][value_name_in_dict])
        return sum_total
    #function to count values from dictionary. Returns sum of values.

    def purchase_product(self):
        unit_price, quantity = input("Enter UNIT PRICE and QUANTITY.").split()
        self.index += 1
        self.product_dict.update({self.index:{"Sub_Total":int(unit_price)*int(quantity),"Quantity": int(quantity)}})
        self.total_qty += int(quantity)
        #will add key and values : subtotal, quantity to the dictionary.

pro_name = input("Enter product name.")
obj = InventoryManagement(pro_name)
ans = True
choice = 0
while ans == True:
    print("""
    1.Purchase Product.
    2.Sell Product.
    3.Show Dictionary.
    4.Show total stock.
    5.Exit.
    """)
    choice = int(input("Enter choice for buy menu."))
    if choice == 1:
        obj.purchase_product()
    elif choice == 2:
        obj.sell_product()
    elif choice == 3:
        obj.print_dict()
    elif choice == 4:
        print(f"Total total is {obj.count('Sub_Total')}")
        print(f"Total quantity is {obj.count('Quantity')}")
        if obj.count('Quantity') == 0:
            print("You have no valuation.")
        else:
            print(f"Valuation is {obj.count('Sub_Total')/obj.count('Quantity'):.2f}.")
        #printing valuation.
    elif choice == 5:
        print("Exiting...")
        ans = False
    else:
        print("Enter again")

