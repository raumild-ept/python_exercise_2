from datetime import date
class product:  # product class:- contains product_info, product_creation methods.
    def __init__(self):
        self.product_dict = {'PRD1': {'product_name': 'pen', 'unit_price': '100', 'cost_price': '2', 'stock_type': 'Stockable', 'stock_amount': '1000'}, 'PRD2': {'product_name': 'book', 'unit_price': '20', 'cost_price': '2', 'stock_type': 'Stockable', 'stock_amount': '300'}}
  # main product_dictionary.
        self.prd_index = 2  # product_Code_indexer.
        self.stock_type = {1: 'Stockable',
                           2: 'Consumable',
                           3: 'Service'
                           }  # stock_type dictionary.

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
            if input_val in [1, 2, 3]:
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
        temp_dict.update({f"PRD{self.prd_index}": prepare_product_dict})
        return temp_dict

    def create_product(self):
        # Calls prepare_product attribute and catches new dictionary and adds it to main dictionary.
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
        # to display product_info
        if self.product_dict != {}:
            print("Product Code|Product Name|Product Stock|")
            for product_code, product_info in self.product_dict.items():
                p_code = product_code.ljust(12, ' ')
                p_name = product_info['product_name'].rjust(12, ' ')
                p_stock = str(product_info['stock_amount']).rjust(13, ' ')
                print(f"{p_code}|{p_name}|{p_stock}|")
            return 1
        else:
            print("You Have No Product.")
            return 0


class customer:
    # class customer contains information about customer info, customer creation methods.
    def __init__(self):
        self.customer_info = {'CUST_1': {'customer_name': 'raumil', 'customer_mobile_no': '8787', 'customer_email': '@rd'}, 'CUST_2': {'customer_name': 'kish', 'customer_mobile_no': '9898', 'customer_email': '@ks'}}
 # customer info dictionary.
        self.customer_address = {'CUST_1': {'address_1': 'ad1', 'address_2': 'ad2', 'city': 'raj', 'zipcode': '360', 'state': 'guj', 'country': 'ind'}, 'CUST_2': {'address_1': 'sq1', 'address_2': 'sq2', 'city': 'ejk', 'zipcode': 'skd', 'state': 'sdsa', 'country': 'asd'}}  # customer address dictionary.
        self.customer_index = 2  # customer code indexer.

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
        temp_cust_info.update({unique_cust_code: prepare_cust_info})  # customer info is generated.
        temp_cust_add.update({unique_cust_code: prepare_cust_address})
        return temp_cust_add, temp_cust_info

    def create_customer(self):
        cust_info_tuple = self.prepare_customer()
        self.customer_info.update(cust_info_tuple[1])
        self.customer_address.update(cust_info_tuple[0])
        print(self.customer_info, self.customer_address)

    def display_customer(self):
        # to display customer info.
        if self.customer_info != {}:
            print("Customer Code|Customer Name|Customer Mobile No.|Customer Email|")
            for cust_code, cust_info in self.customer_info.items():
                cust_codep = cust_code.ljust(13, ' ')
                cust_name = cust_info['customer_name'].rjust(13, ' ')
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
        self.sales_order = {'SO1': {'customer_code': 'CUST_1', 'date': (2021, 1, 30), 'order_lines': [{'product_code': 'PRD1', 'product_name': 'pen', 'product_qty': 30, 'product_unit_price': '100', 'subtotal': 3000, 'state': 'Draft'}, {'product_code': 'PRD2', 'product_name': 'book', 'product_qty': 25, 'product_unit_price': '20', 'subtotal': 500, 'state': 'Draft'}], 'total': 3500, 'state': 'Draft'}, 'SO2': {'customer_code': 'CUST_2', 'date': (2021, 1, 30), 'order_lines': [{'product_code': 'PRD1', 'product_name': 'pen', 'product_qty': 10, 'product_unit_price': '100', 'subtotal': 1000, 'state': 'Draft'}, {'product_code': 'PRD2', 'product_name': 'book', 'product_qty': 5, 'product_unit_price': '20', 'subtotal': 100, 'state': 'Draft'}], 'total': 1100, 'state': 'Draft'}}
  # main sales order dictionary.
        self.sales_order_index = 2  # sales order indexer.

    def select_products(self):
        # product_select attribute is used to select product among all products.
        # it is coded to give user menu driven experience to add products as many times user need.
        while True:
            if self.display_product() == 1:
                # asks for product id.
                product_id = input(
                    "Enter Product id you want to add in salesorder. Enter 'exit' if you want to discontinue.")
                # if product_id exists than it is evaluated further else it will print error and will ask for correct id.
                if product_id in self.product_dict.keys():
                    sales_add_amount = int(input("Enter Amount to Buy: "))
                    return product_id, sales_add_amount
                elif product_id.lower() == 'exit':
                    return 0
                else:
                    print("Enter Correct ProductID")
                # if product id is incorrect than error will be generated.
            else:
                return -1

    #takes product_data tuple as argument.
    #product_data[0] is product SKU.
    #product_data[1] is product quantity to be bought.
    def prepare_orderline(self, product_data):
        order_line = dict()#empty order line dict.
        order_line.update({"product_code": product_data[0],
                           "product_name": self.product_dict[product_data[0]]["product_name"],
                           "product_qty": product_data[1],
                           "product_unit_price": self.product_dict[product_data[0]]["unit_price"],
                           "subtotal": int(product_data[1]) * int(
                               self.product_dict[product_data[0]]["unit_price"]),
                           "state": "Draft"
                           })
        return order_line

    def prepare_sales(self):
        temp_sales_order = dict()#temp sales_order_dict
        order_line = list()#order_line empty list.
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
                        #will call product selector.
                        product_data = self.select_products()
                        #if product data is not error notifier integer than proceed further.
                        if product_data != 0 and product_data != -1:
                            #create order_line.
                            order_l = self.prepare_orderline(product_data)
                            for order_lin in order_line:
                                id_list.append(order_lin['product_code'])
                            #if product sku is not in order line than orderline is simply appended to orderlines list.
                            if product_data[0] not in id_list:
                                order_line.append(order_l)
                            # order line is appended.


                            #is product sku exists in one of the order lines than update values of that orderline.
                            elif product_data[0] in id_list:
                                for order_lin in order_line:
                                    if order_lin['product_code'] == product_data[0]:
                                        order_lin.update(
                                            {'product_qty': int(order_lin['product_qty']) + int(product_data[1])})
                                        order_lin.update({'subtotal': int(order_lin['product_qty']) * int(
                                            order_lin['product_unit_price'])})

                        elif product_data == -1:
                            return 0

                    elif choice == '2':
                        #if orderline is not empty than sales_order dict is prepared.
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

    # will return sum.
    #will take orderlines as input argument.
    def sum_finder(self, list_of_product_dictionaries):
        # will find sum of subtotal in sales dictionary.
        sum = 0
        for product_dictionary in list_of_product_dictionaries:
            sum += int(product_dictionary["subtotal"])
        return sum

    def create_sales_order(self):
        updator = self.prepare_sales()
        #if updator is 0 it means that no products were added to the sales_order.
        if updator and updator != 0 and updator != {}:
            self.sales_order.update(updator)
            print(self.sales_order)
        elif updator == 0 or updator == {}:
            print("You have not created sale order.")

    #function to change sales_order_state to 'Confirm'. Takes sales_order unique code as serial.
    def change_to_confirm(self, serial):
        if self.sales_order[serial]['state'] == 'Confirm':
            print("Order already Confirmed.")
        elif self.sales_order[serial]['state'] == 'Done':
            print("Order is Done already.")
        elif self.sales_order[serial]['state'] == 'Cancel':
            print("First Change Into Draft.")
        #if state is Draft and state is neither Confirm nor Cancel than proceed further.
        elif self.sales_order[serial]['state'] == 'Draft':
            index = 0#orderline counter which counts orderline which will be confirmed.
            for order_line in self.sales_order[serial]['order_lines']:
                #if quantity input from user is available in product dictionary than proceed further.
                if int(order_line['product_qty']) <= int(self.product_dict[order_line['product_code']]['stock_amount']):
                    order_line.update({'state': 'Confirm'})
                    #index is incremented for counting.
                    index += 1
            #if number of lines in orderlines are same as index than all orderlines are confirmed
            #than the state of whole order is Confirm.
            if len(self.sales_order[serial]['order_lines']) == index:
                self.sales_order[serial].update({'state': 'Confirm'})
                print("Sales Order Confirmed.")
                 #if all products in orderlines are available than serial is returned.
            else:
                print("State cant be confirmed as some products are not available in stock.")
        return serial

    #function to change sales_order state to 'Draft'
    def change_to_draft(self):
        for key, value in self.sales_order.items():
            print(f"{key}")
        serial = input("Enter Sale Order Number.")
        if self.sales_order[serial]['state'] == 'Draft':
            print("Order already Draft.")
        elif self.sales_order[serial]['state']=='Confirm':
            print("Cancel Order First.")
        elif self.sales_order[serial]['state'] == 'Done':
            print("Order cant be Drafted as it is Done.")
        else:
            for order_line in self.sales_order[serial]['order_lines']:
                order_line.update({'state': 'Draft'})
            self.sales_order[serial].update({'state': 'Draft'})
            print("Changed to draft.")

    #function to change state of sales_order to 'Cancel'
    def change_to_cancel(self):
        for key, value in self.sales_order.items():
            print(f"{key}")
        serial = input("Enter Sale Order Number.")
        if self.sales_order[serial]['state'] == 'Cancel':
            print("Order already Cancel.")
        else:
            for order_line in self.sales_order[serial]['order_lines']:
                order_line.update({'state': 'Cancel'})
        self.sales_order[serial].update({'state': 'Cancel'})

    def display(self):
        # sales order display function.
        if self.sales_order != {}:
            for key, value in self.sales_order.items():
                print(f"{key}")
            key_to_print = input("ENTER KEY OF SALE ORDER YOU WANT TO PRINT: ")
            for key, value in self.sales_order.items():
                if key == key_to_print:
                    total = f"Order Total: {str(value['total'])}"
                    total = total.rjust(67, ' ')
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
                        unit_price = str(order_line['product_unit_price']).rjust(13, ' ')
                        qty = str(order_line['product_qty']).rjust(22, ' ')
                        amount = str(order_line['subtotal']).rjust(14, ' ')
                        print(
                            f"\t\t\t{pro_name}{unit_price}{qty}{amount}")
                    print(f"\t\t\t{total}")
                    print(f"""\t\t\tStatus:{value['state']}""")
        else:
            print("You have NO Sales Orders.")

class SalesOrderExtender(SaleOrder):#DeliveryOrder class defined.
    def __init__(self):
        SaleOrder.__init__(self)
        self.index = 0
        self.dilevery_order_dict = dict()#delivery order dict initiated.

    #change state of sales order to confirm state. Here serial is sales_order unique code.
    def change_to_confirm(self, serial):
        #calling super method to change the state to confirm.
        so_id = super().change_to_confirm(serial)
        #if state is confirmed than call create_delivery_order method.
        if so_id and self.sales_order[so_id]['state']=='Confirm':
            self.create_delivery_order(so_id)

    #stock_moves line creator. Here seraial is sales_order unique code.
    def prepare_delivery_order_line(self,serial):
        orderline = []#empty temp list.
        #required info is fetched from orderlines/
        for orderlin in self.sales_order[serial]['order_lines']:
            orderline.append({'product_code':orderlin['product_code'],
                              'product_qty':orderlin['product_qty'],
                              'product_state':orderlin['state']})
        return orderline

    #takes sales_order unique code from caller as serial.
    def prepare_delivery_order(self,serial):
            #index is incremented per creation.
            self.index += 1
            #temp dict for value storage.
            prp_dict=dict()
            #delivery dict unique code.
            delivery_code = "DO"+str(self.index)
            temp = self.prepare_delivery_order_line(serial)
            prp_dict.update({delivery_code:{
                'sales_code':serial,
                'stock_moves':temp,
                'state': 'Draft'
            }})
            return prp_dict

    #takes sales_order unique code from user input as serial.
    def create_delivery_order(self,serial):
        #if sale order is confirm than prepare delivery order.
        if self.sales_order[serial]['state'] == 'Confirm':
            self.dilevery_order_dict.update(self.prepare_delivery_order(serial))
            print(self.dilevery_order_dict)
        #if sale order is not confirmed it will ask to confirm it first.
        else:
            print("Confirm Sales Order First.")

    # here serial is unique code of delivery order.
    def validate_delivery_order(self,serial):
        product_dict_reseter = self.product_dict
        #getting sale_order code.
        sales_code = self.dilevery_order_dict[serial]['sales_code']
        #if sale_order state is 'Confirm' than proceed.
        if self.sales_order[sales_code]['state']=='Confirm':
            #in every orderline ...
            for order_line in self.dilevery_order_dict[serial]['stock_moves']:
                #if quantity from orderline is available in product dict than reduce the amount.
                if int(order_line['product_qty']) <= int(self.product_dict[order_line['product_code']]['stock_amount']):
                    self.product_dict[order_line['product_code']].update({'stock_amount': (
                    int(self.product_dict[order_line['product_code']]['stock_amount']) - int(order_line['product_qty']))})
                    order_line.update({'product_state':'Done'})
                else:
                    #if enough  quantity is not available in product dict than error is printed and order is not validated.
                    print("Delivery Order Cant be validated as you have not enough stock.")
                    #as whole order is not validated quantity from orderlines are reset.
                    self.product_dict = product_dict_reseter
                    return 0
            #whole sale order quantity is available so order is validated.
            self.dilevery_order_dict[serial].update({'state':'Done'})
            #sales order is transfered to done state
            for orderline in self.sales_order[self.dilevery_order_dict[serial]['sales_code']]['order_lines']:
                orderline.update({'state': 'Done'})
            self.sales_order[self.dilevery_order_dict[serial]['sales_code']].update({'state': "Done"})
            print("Delivery Order is validated and done.")
            print(self.dilevery_order_dict)

        #if sales_order is in Draft than it will ask to confirm it first.
        elif self.sales_order[sales_code]['state'] == "Draft":
            print("Confirm Sale Order First.")

        # if sales_order is in Cancel than it will ask to confirm it first.
        elif self.sales_order[sales_code]['state'] == "Cancel":
            print("Confirm Sale Order First.")

        elif self.sales_order[sales_code]['state'] == 'Done':
            print("Order is Already Done...")

    # here serial is unique code of delivery order.
    def cancel_delivery_order(self,serial):
        #getting sale_order code.
        sales_code = self.dilevery_order_dict[serial]['sales_code']
        #if delivery order is not done than proceed.
        if self.dilevery_order_dict[serial]['state'] != "Done":
                for order_line in self.dilevery_order_dict[serial]['stock_moves']:
                    order_line.update({'product_state':'Cancel'})
                self.dilevery_order_dict[serial].update({'state':'Cancel'})
                print("Delivery Order Canceled.")
                print(self.dilevery_order_dict)
        #else print error.
        else:
            print("You cant cancel done order.")

    def cancel_sales_order(self,serial):
        #if provided sales code(serial) is true, than proceed.
        if serial in self.sales_order.keys() :
            serial_sales = []
            for values in self.dilevery_order_dict.values():
                serial_sales.append(values['sales_code'])
            #if sales code(serial) is in delivery order dictionary than proceed.
            if serial in serial_sales:
                for values in self.dilevery_order_dict.values():
                    if values['sales_code'] == serial:
                        #if delivery order is in 'Cancel' state than cancel the sales order.
                        if values['state']=='Cancel':
                                for orderlin in self.sales_order[serial]['order_lines']:
                                    orderlin.update({'state':'Cancel'})
                                    self.sales_order[serial].update({'state':'Cancel'})
                        #if delivery order is in draft of confirm state, than print message that cancel D.O. first.
                        elif values['state']=='Confirm' or values['state']=='Draft':
                                print("Warning !!! Cancel Delivery Order First.")
                                return 0
                        #if order if delivered or it is in 'Done' state, cant cancel sales order now.
                        elif values['state'] == 'Done':
                            print("Your Order Is Delivered. Cant Cancel Now.")
                            return 0
                print("Sales Order canceled. ")
                return 0
            #if delivery order is not created for given sales order, than cancel it.
            else:
                self.sales_order[serial].update({'state': 'Cancel'})
                print("Sales Order canceled.")
                return 0
        #if wrong sales order provided, print error.
        else:
            print("Wrong Key")

if __name__ == "__main__":
    d1 = SalesOrderExtender()
    # object of CLASS DeliveryOrder.
    while True:
        print("""
        1.Create Product.
        2.Update Stock.
        3.Create Customer.
        4.Create SalesOrder.
        5.Display SalesOrder.
        6.Confirm Sales Order.
        7.Cancel Sales Order.
        8.Draft Sales Order.
        9.Show All Products.
        10.Show All Customers.
        11.Cancel Delivery Order.
        12.Validate Delivery Order.
        13.Print delivery Dict.
        14.Print Sales Dict
        21.Exit
        """)
        ans = input("Enter Your Choice")
        if ans == '1':
            d1.create_product()
        elif ans == '3':
            d1.create_customer()
        elif ans == '2':
            d1.update_stock()
        elif ans == '4':
            key1 = True
            while key1 == True:
                print("""
                                    1.Create SalesOrder.
                                    2.Exit
                                """)
                choice = input("Enter Your Choice: ")
                if choice == '1':
                    d1.create_sales_order()
                elif choice == '2':
                    key1 = False
                else:
                    print("Enter Correct Value.")
        elif ans == '5':
            d1.display()
        elif ans == '6':
            for key, value in d1.sales_order.items():
                print(f"{key}")
            serial = input("Enter Sale Order Number.")
            d1.change_to_confirm(serial)
        elif ans == '7':
            if d1.sales_order != {}:
                print(list(d1.sales_order.keys()))
                serial = input("Sale Order To Cancel.")
                d1.cancel_sales_order(serial)
            else:
                print("No Sales Order.")
        elif ans == '8':
            d1.change_to_draft()
        elif ans == '9':
            d1.display_product()
        elif ans == '10':
            d1.display_customer()
        elif ans == 'none':
            if list(d1.sales_order.keys()) != []:
                print(list(d1.sales_order.keys()))
                serial = input("Enter Sale Order To Make Delivery Order.")
                d1.create_delivery_order(serial)
            else :
                print("There are no sales orders.")
        elif ans == 'none2':
            if list(d1.sales_order.keys()) != []:
                print(d1.sales_order.keys())
                serial = input("Enter Sale order You want to Cancel.")
                d1.cancel_sales_order(serial)
            else :
                print("There are no sales orders.")
        elif ans == '11':
            if list(d1.dilevery_order_dict.keys()) != []:
                print(d1.dilevery_order_dict.keys())
                serial = input("Enter delivery order You want to Cancel.")
                d1.cancel_delivery_order(serial)
            else:
                print("No delivery Order Created.")
        elif ans == '12':
            if d1.dilevery_order_dict != {}:
                print(list(d1.dilevery_order_dict.keys()))
                serial = input("Enter delivery order dict.")
                d1.validate_delivery_order(serial)
            else:
                print("You have no delivery order.")
        elif ans == '13':
            print(d1.dilevery_order_dict)
        elif ans == '14':
            print(d1.sales_order)
        elif ans == '21':
            break
        else:
            print("Enter Correct Value.")