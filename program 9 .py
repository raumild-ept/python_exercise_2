from datetime import date
class product:  # product class:- contains product_info, product_creation methods.
    def __init__(self):
        self.product_dict = dict()      #main product_dictionary.
        self.prd_index = 0        # product_Code_indexer.
        self.stock_type = {1: 'Stockable',
                           2: 'Consumable',
                           3: 'Service'
                           }        # stock_type dictionary.
    def prepare_product(self):
        temp_dict = dict()
        prepare_product_dict = dict()
        # Asks user the information of the products.
        product_name = input("Enter Product name.")
        product_unit_price = input("Enter product unit price: ")
        product_cost_price = input("Enter product cost price: ")
        product_stock_amount = input("Enter Stock amount: ")
        while True:
            input_val = int(input("""What is your stock type?
        
                1.Stockable.
                2.Consumable.
                3.Service.
                """))
            if input_val in [1,2,3]:
                break
            else:
                print("Enter Correct Value")
        # creates product_dictionary and returns to the product create function.
        prepare_product_dict.update({
            "product_name": product_name,
            "unit_price": product_unit_price,
            "cost_price": product_cost_price,
            "stock_type": self.stock_type[input_val],
            "stock_amount": product_stock_amount
        })
        self.prd_index += 1
        temp_dict.update({f"PRD{self.prd_index}":prepare_product_dict})
        return temp_dict

    def create_product(self):
        #Calls prepare_product attribute and catches new dictionary and adds it to main dictionary.
        self.product_dict.update(self.prepare_product())
        print(self.product_dict)

    def update_stock(self):
        # updates value of products.
        while True:
            print("""
                   1.Update Stock.
                   2.Exit
                   """)
            choice = int(input("Enter choice: "))
            if choice == 1:
                if self.display_product() == 1:
                    stock_to_update = input("Enter product code you want to update.")
                    new_stock_amount = int(input("Enter new stock amount"))
                    dict_to_update = self.product_dict[stock_to_update]
                    dict_to_update.update({"stock_amount": new_stock_amount})  # stock is updated with update method.
                    self.product_dict.update({stock_to_update: dict_to_update})
                    self.display_product()

            else:
                break

    def display_product(self):
        #to display product_info
        if self.product_dict != {}:
            print("Product Code|Product Name|Product Stock|")
            for product_code , product_info in self.product_dict.items():
                p_code = product_code.ljust(12,' ')
                p_name = product_info['product_name'].rjust(12,' ')
                p_stock = str(product_info['stock_amount']).rjust(13,' ')
                print(f"{p_code}|{p_name}|{p_stock}|")
            return 1
        else:
            print("You Have No Product.")
            return 0
class customer:
    # class customer contains information about customer info, customer creation methods.
    def __init__(self):
        self.customer_info = dict()  # customer info dictionary.
        self.customer_address = dict()  # customer address dictionary.
        self.customer_index = 0  # customer code indexer.

    def prepare_customer(self):
        temp_cust_info = dict()
        temp_cust_add = dict()
        cust_name = input("Enter Customer name: ")
        cust_no = input("Enter Customer mobile number:")
        cust_email = input("Enter Customer Email: ")
        cust_add1 = input("Enter Address 1")
        cust_add2 = input("Enter Address 2")
        cust_city = input("Enter City")
        cust_zipcode = input("Enter Zipcode")
        cust_state = input("Enter State")
        cust_country = input("Enter Country")
        # asks user for customer information.
        prepare_cust_info = {
            "customer_name": cust_name,
            "customer_mobile_no": cust_no,
            "customer_email": cust_email
        }
        prepare_cust_address = {
            "address_1": cust_add1,
            "address_2": cust_add2,
            "city": cust_city,
            "zipcode": cust_zipcode,
            "state": cust_state,
            "country": cust_country
        }
        # prepares and returns customer information dict and customer address dict.
        self.customer_index += 1
        unique_cust_code = "CUST_" + str(self.customer_index)  # unique customer code is generated.
        temp_cust_info.update({unique_cust_code:prepare_cust_info} )  # customer info is generated.
        temp_cust_add.update({unique_cust_code: prepare_cust_address})
        return temp_cust_add,temp_cust_info

    def create_customer(self):
        cust_info_tuple = self.prepare_customer()
        self.customer_info.update(cust_info_tuple[1])
        self.customer_address.update(cust_info_tuple[0])
        print(self.customer_info, self.customer_address)

    def display_customer(self):
        #to display customer info.
        if self.customer_info!={}:
            print("Customer Code|Customer Name|Customer Mobile No.|Customer Email|")
            for cust_code , cust_info in self.customer_info.items():
                cust_codep = cust_code.ljust(13, ' ')
                cust_name= cust_info['customer_name'].rjust(13, ' ')
                phno = cust_info['customer_mobile_no'].rjust(19, ' ')
                email = cust_info['customer_email'].rjust(14, ' ')
                print(f"{cust_codep}|{cust_name}|{phno}|{email}|")
            return 1
        else:
            print("You have no Customers.")
            return 0

class SaleOrder(product, customer, ):
    # sales order class contains methods to create sales orders, and saves sales orders.
    def __init__(self):  # class customer and product are inherited.
        product.__init__(self)
        customer.__init__(self)
        self.sales_order = dict()  # main sales order dictionary.
        self.sales_order_index = 0  # sales order indexer.

    def select_products(self):
        # product_select attribute is used to select product among all products.
        # it is coded to give user menu driven experience to add products as many times user need.
        while True:
            if self.display_product() == 1:
                # asks for product id.
                product_id = input("Enter Product id you want to add in salesorder. Enter 'exit' if you want to discontinue.")
                # if product_id exists than it is evaluated further else it will print error and will ask for correct id.
                if product_id in self.product_dict.keys():
                    sales_add_amount = int(input("Enter Amount to Buy: "))
                    if sales_add_amount <= int(self.product_dict.get(product_id, {}).get("stock_amount")):
                        # if user asks qty less than or equal to available qty than further evaluation is proceeded.
                         remaining_qty = int(self.product_dict.get(product_id, {}).get("stock_amount")) - int(sales_add_amount)
                        # # quantity is reduced.
                         self.product_dict.get(product_id, {}).update({"stock_amount": remaining_qty})
                         return product_id, sales_add_amount
                        # product_id and qty is returned.
                        #return product_id, sales_add_amount
                    else:
                        print("Stock not available.")
                        # if enough qty is not there, error will be printed.
                elif product_id.lower() == 'exit':
                    return 0
                else:
                    print("Enter Correct ProductID")
                # if product id is incorrect than error will be generated.
            else:
                return -1
    def prepare_orderline(self,product_data):
        order_line = dict()
        order_line.update({"product_code": product_data[0],
                                   "product_name": self.product_dict[product_data[0]]["product_name"],
                                   "product_qty": product_data[1],
                                   "product_unit_price": self.product_dict[product_data[0]]["unit_price"],
                                   "subtotal": int(product_data[1]) * int(
                                       self.product_dict[product_data[0]]["unit_price"]),
                                   "state" : "Draft"
                           })
        return order_line


    def prepare_sales(self):
        temp_sales_order = dict()
        order_line = list()
        id_list = list()
        # prints customer data for user reference.
        if self.display_customer() == 1:
            cust_id = input("Select customer Unique Code. Enter 'exit' if you want to discontinue.")
            if cust_id in self.customer_info.keys():
                # if cust_id exits than further evaluation is done further.
                date_of_purchase = date.today()
                sales_dict = {"customer_code": cust_id,
                              "date": date_of_purchase
                              }
                while True:
                    print("""
                                        1.Add product.
                                        2.Exit""")
                    choice = input("Enter Choice: ")
                    if choice == '1':

                        product_data = self.select_products()

                        if product_data != 0 and product_data != -1:
                            order_l = self.prepare_orderline(product_data)

                            for order_lin in order_line:
                                id_list.append(order_lin['product_code'])

                            if product_data[0] not in id_list:
                                order_line.append(order_l)
                            # order line is appended.
                            elif product_data[0] in id_list:
                                for order_lin in order_line:
                                    if order_lin['product_code'] == product_data[0]:
                                        order_lin.update({'product_qty': int(order_lin['product_qty']) + int(product_data[1])})
                                        order_lin.update({'subtotal': int(order_lin['product_qty']) * int(
                                            order_lin['product_unit_price'])})
                        elif product_data == -1:
                            return 0
                    elif choice == '2':
                        if order_line != []:
                            sales_order_code = 'SO'
                            self.sales_order_index += 1  # sales code indexer.
                            temp_sales_order.update({
                                sales_order_code + str(self.sales_order_index): {
                                    "customer_code": sales_dict["customer_code"],
                                    "date": sales_dict["date"],
                                    "order_lines": order_line,
                                    "total": self.sum_finder(order_line),
                                    "state": "Draft"}})
                        return temp_sales_order
                    else:
                        print("Enter Correct Value.")
            elif cust_id.lower() == 'exit':
                return 0
            else:
                print("Enter Correct Cust_Code")

        # if wrong cust_code is sent by customer than error will be printed.

    def sum_finder(self, list_of_product_dictionaries):
        # will find sum of subtotal in sales dictionary.
        sum = 0
        for product_dictionary in list_of_product_dictionaries:
            sum += int(product_dictionary["subtotal"])
        return sum
    # will return sum.
    def create_sales_order(self):
        updator = self.prepare_sales()
        if updator and updator != 0 and updator != {}:
            self.sales_order.update(updator)
            print(self.sales_order)
        elif updator == 0 or updator == {}:
            print("You have not created sale order.")

    def change_to_confirm(self):
        for key, value in self.sales_order.items():
            print(f"{key}")
        serial = input("Enter Sale Order Number.")
        if self.sales_order[serial]['state'] == 'Confirm':
            print("Order already Confirmed.")
        else :
            index = 0
            for order_line in self.sales_order[serial]['order_line'].value():
                if order_line['product_qty'] >=self.product_dict[order_line['product_code']]['stock_amount']:
                    order_line.update({'state': 'Done'})
                    index +=1
            if len(self.sales_order[serial]['order_line']) == index:
                self.sales_order[serial].update({'state':'Confirm'})
                print("Order is Validated.")
            else:
                print("State cant be confirmed as some products are not available in stock.")

    def change_to_draft(self):
        for key, value in self.sales_order.items():
            print(f"{key}")
        serial = input("Enter Sale Order Number.")
        if self.sales_order[serial]['state'] == 'Draft':
            print("Order already Draft.")
        else :
            for order_line in self.sales_order[serial]['order_line'].value():
                order_line.update({'state':'Draft'})
        self.sales_order[serial].update({'state':'Draft'})

    def change_to_cancel(self):
        for key, value in self.sales_order.items():
            print(f"{key}")
        serial = input("Enter Sale Order Number.")
        if self.sales_order[serial]['state'] == 'Cancel':
            print("Order already Cancel.")
        else :
            for order_line in self.sales_order[serial]['order_line'].value():
                order_line.update({'state':'Cancel'})
        self.sales_order[serial].update({'state':'Cancel'})

    def display(self):
        # sales order display function.
        if self.sales_order != {}:
            for key, value in self.sales_order.items():
                print(f"{key}")
            key_to_print = input("ENTER KEY OF SALE ORDER YOU WANT TO PRINT: ")
            for key, value in self.sales_order.items():
                if key == key_to_print:
                    total = f"Order Total: {str(value['total'])}"
                    total = total.rjust(67,' ')
                    date1 = value["date"]
                    print(f"""
            Order No:  {key}                                     Date: {date1}
            Cust Code:   {value['customer_code']}
            Name:        {self.customer_info[value['customer_code']]['customer_name']}
            Address 1:   {self.customer_address[value['customer_code']]['address_1']}
            Address 2:   {self.customer_address[value['customer_code']]['address_2']}
            Zipcode:     {self.customer_address[value['customer_code']]['zipcode']}
            City, State: {self.customer_address[value['customer_code']]['city']},{self.customer_address[value['customer_code']]['state']}
            Country:     {self.customer_address[value['customer_code']]['country']}
            Ph no.:      {self.customer_info[value['customer_code']]['customer_mobile_no']}
            Email:       {self.customer_info[value['customer_code']]['customer_email']}

            Product Name      Product Price      Product Quantity      Subtotal
            -------------------------------------------------------------------
            -------------------------------------------------------------------""")
                    for order_line in value['order_lines']:
                        pro_name = order_line['product_name'].ljust(18, ' ')
                        unit_price = str(order_line['product_unit_price']).rjust(13,' ')
                        qty = str(order_line['product_qty']).rjust(22, ' ')
                        amount = str(order_line['subtotal']).rjust(14, ' ')
                        print(
                    f"\t\t\t{pro_name}{unit_price}{qty}{amount}")
                    print(f"\t\t\t{total}")
                    print(f"""\t\t\tStatus:{value['state']}""")
        else:
            print("You have NO Sales Orders.")

if __name__ == "__main__":
    s1 = SaleOrder()
    #object of CLASS SaleOrder.
    key = True
    while key == True:
        print("""
        1.Create Product.
        2.Update Stock.
        3.Create Customer.
        4.Create SalesOrder.
        5.Display SalesOrder.
        6.Validate/Confirm Delivery Order.
        7.Cancel Delivery Order.
        8.Set To Draft.
        9.Set To Done.
        10.Show All Products.
        11.Show All Customers.
        12.Exit
        """)
        ans = input("Enter Your Choice")
        if ans == '1':
            s1.create_product()
        elif ans == '3':
            s1.create_customer()
        elif ans == '2':
            s1.update_stock()
        elif ans == '4':
            key1 = True
            while key1 == True:
                print("""
                                    1.Create SalesOrder.
                                    2.Exit
                                """)
                choice = input("Enter Your Choice: ")
                if choice == '1':
                    s1.create_sales_order()
                elif choice == '2':
                    key1 = False
                else:
                    print("Enter Correct Value.")
        elif ans == '5':
            s1.display()
        elif ans == '6':
            s1.change_to_confirm()
        elif ans == '7':
            s1.change_to_cancel()
        elif ans == '8':
            s1.change_to_draft()
        elif ans == '10':
            s1.display_product()
        elif ans == '11':
            s1.display_customer()
        elif ans == '12':
            key = False
        else:
            print("Enter Correct Value.")