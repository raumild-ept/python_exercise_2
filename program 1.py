class Manufacturing:
    #creating class
    def __init__(self):
        self.raw_name = 0
        self.raw_quantity = 0
        self.product_name = 0
        self.product_quantity = 0
        self.ratio = 0
        self.actual_product_created = 0
        #Creating required variables.
    def produce(self):
        self.product_quantity = int(input(f"How many {self.product_name} you want to produce."))
        if self.product_quantity * self.ratio <= self.raw_quantity:
            #Function to produce quantity.
            self.actual_product_created += self.product_quantity
            #product is increased.
            self.raw_quantity -= self.product_quantity * self.ratio
            #raw material used is decreased.
            print(f"You created {self.product_quantity} the products.")
        else:
            answer_temp = input(
                f"You can make {int(self.raw_quantity / self.ratio)}.Do you want to produce them?...Yes/no...?").lower()
                #asks uese that they can make lesser quantity than they asked. If they press yes , than conditions are proceeded.
            if answer_temp == "yes":
                self.actual_product_created = self.actual_product_created + int(self.raw_quantity / self.ratio)
                print(f"You created {int(self.raw_quantity / self.ratio)} products.")
                #products that can be created is created.
                #raw_material used is decreased.
            else:
                print(f"You need {(self.product_quantity * self.ratio) - self.raw_quantity} more {self.raw_name}.")

    def display_raw_material_stock(self):
        print(f"You have {self.raw_quantity} {self.raw_name}.")

    def display_final_product_stock(self):
        print(f"You have {self.actual_product_created} {self.product_name}.")

    def purchase_raw_material(self):
        self.raw_quantity += int(input("Enter raw material quantity."))

    def buy_menu(self):
        answer = True
        self.product_name = input("What you want to produce?")
        self.raw_name = input("Enter raw material.")
        self.ratio = int(input("Enter how much raw material you need per product."))
        while answer:
            print("""
            1.Purchase Raw Material Product
            2.Manufacture Actual Product
            3.Show Raw Material Quantity
            4.Show Actual Product Quantity
            5.Exit
            """)
            answer = input("What would you like to do?")
            if answer == "1":
                self.purchase_raw_material()
            elif answer == "2":
                self.produce()
            elif answer == "3":
                self.display_raw_material_stock()
            elif answer == "4":
                self.display_final_product_stock()
            elif answer == "5":
                answer = False
            else:
                print("Enter correct value.")


obj1 = Manufacturing()
obj1.buy_menu()


