class Manufacturing:
    def __init__(self):
        self.raw_name = 0
        self.raw_quantity = 0
        self.product_name = 0
        self.product_quantity = 0
        self.ratio = 0
        self.actual_product_created = 0
        #created required variables and initialized with zero.

    def produce(self):
        self.product_quantity = int(input(f"How many {self.product_name} you want to produce."))
        if self.product_quantity * self.ratio <= self.raw_quantity:#if material required to produce product isavailable.
            self.actual_product_created += self.product_quantity #create product.
            self.raw_quantity -= self.product_quantity * self.ratio #raw_material is decreased.
            print(f"You created {self.product_quantity} the products.")
        else:
            answer_temp = input(
                f"You can make {int(self.raw_quantity / self.ratio)}.Do you want to produce them?...Yes/no...?").lower()
                #asks user if they wamt to make product that can be made from material available, as required material is not there.
            if answer_temp == "yes":
                self.actual_product_created = self.actual_product_created + int(self.raw_quantity / self.ratio)#if yes than most product can be created is created.
                print(f"You created {int(self.raw_quantity / self.ratio)} products.")
                self.raw_quantity -= self.raw_quantity - (self.raw_quantity % self.ratio)#raw  product used is decreased.
            # print("You do not have enough raw material. Please purchase more raw material.")
            else:
                print(f"You need {(self.product_quantity * self.ratio) - self.raw_quantity} more {self.raw_name}.")

    def display_raw_material_stock(self):
        print(f"You have {self.raw_quantity} {self.raw_name}.")

    def display_final_product_stock(self):
        print(f"You have {self.actual_product_created} {self.product_name}.")

    def purchase_raw_material(self):
        self.raw_quantity += int(input("Enter raw material quantity."))


class Scrapper(Manufacturing):
    #class is extended.
    def __init__(self):
        Manufacturing.__init__(self)
        #

    def scrap(self, qty, total):
        return total - qty
    #scrap function.

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
            5.Scrap Raw Material
            6.Scrap Product
            7.Exit
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
                scrap_raw_material = int(input("How much material need to be scrapped?"))
                if scrap_raw_material <= self.raw_quantity:
                 self.raw_quantity = self.scrap(scrap_raw_material, self.raw_quantity)
                 print("Raw material scrapped.")
                else:
                 print("You can not scrap more than you have.")
            elif answer == "6":
                scrap_product = int(input("How many products need to be scrapped."))
                if scrap_product <= self.actual_product_created:
                 self.actual_product_created = self.scrap(scrap_product, self.actual_product_created)
                 print("Products scrapped.")
                else:
                 print("You can not scrap more than you have.")
            elif answer == "7":
                answer = False
            else:
                print("Enter correct value.")
obj1 = Scrapper()
obj1.buy_menu()
