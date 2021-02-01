class Manufacturing:
    def __init__(self,product_name,raw_name,ratio):
        self.raw_name = raw_name
        self.raw_quantity = 0
        self.product_name = product_name
        self.product_quantity = 0
        self.ratio = ratio
        self.actual_product_created = 0

    def produce(self):
        self.product_quantity = int(input(f"How many {self.product_name} you want to produce."))
        if self.product_quantity * self.ratio <= self.raw_quantity:
            self.actual_product_created += self.product_quantity
            self.raw_quantity -= self.product_quantity * self.ratio
            print(f"You created {self.product_quantity} the products.")
        else:
            answer_temp = input(
                f"You can make {int(self.raw_quantity / self.ratio)}.Do you want to produce them?...Yes/no...?").lower()
            if answer_temp == "yes":
                self.actual_product_created = self.actual_product_created + int(self.raw_quantity / self.ratio)
                print(f"You created {int(self.raw_quantity / self.ratio)} products.")
                self.raw_quantity -= self.raw_quantity - (self.raw_quantity % self.ratio)
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
    def __init__(self,product_name,raw_name,ratio):
        Manufacturing.__init__(self,product_name,raw_name,ratio)

    def scrap(self, qty, total):
        return total - qty

answer = True
product_name = input("What you want to produce?")
raw_name = input("Enter raw material.")
ratio = int(input("Enter how much raw material you need per product."))
obj1 = Scrapper(product_name,raw_name,ratio)
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
            obj1.purchase_raw_material()
        elif answer == "2":
            obj1.produce()
        elif answer == "3":
            obj1.display_raw_material_stock()
        elif answer == "4":
            obj1.display_final_product_stock()
        elif answer == "5":
            scrap_raw_material = int(input("How much material need to be scrapped?"))
            if scrap_raw_material <= obj1.raw_quantity:
                obj1.raw_quantity = obj1.scrap(scrap_raw_material, obj1.raw_quantity)
                print("Raw material scrapped.")
            else:
                print("You can not scrap more than you have.")
        elif answer == "6":
            scrap_product = int(input("How many products need to be scrapped."))
            if scrap_product <= obj1.actual_product_created:
                obj1.actual_product_created = obj1.scrap(scrap_product, obj1.actual_product_created)
                print("Products scrapped.")
            else:
                print("You can not scrap more than you have.")
        elif answer == "7":
            answer = False
        else:
            print("Enter correct value.")
