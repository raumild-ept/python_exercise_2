import csv #importing csv module.
class CsvManipulation:
    def __init__(self):
        self.data_dict = {} #creating empty data dictionary.
        self.country_dict = {'ES':'Espanol' ,
                             'DE':'Denmark',
                             'USA':'United States Of America' ,
                             'UK':'United Kingdom', 'AU': 'Australia',
                             'IT': 'Italy'} #dictionary to get name of country by country code.
        self.country_Set = {"USA"}
        self.column_name_list = []#column name list defined.

    def key_finder(self):#finds keys of dictionary.
        list_keys = list(self.data_dict.keys())
        return list_keys

    def dictionary_updator(self,row): #updates whole dataset.Takes one row as input and its slices are divided to dictionary as data.
        self.data_dict.update({row[0]:{"Customer":{"Name":row[1] ,
                                                   "Add 1":row[5] ,
                                                   "Add 2":row[6] ,
                                                   "Zipcode":row[7],
                                                   "City":row[8],
                                                   "Country": self.country_dict[row[9]]
                                                   },
                                       "Products":[{"SKU": row[2],
                                                   "QTY":row[3] ,
                                                   "Price":row[4]
                                                   }]
                                       }
                               })

    def product_updator(self,order_no,row):#prodduct appender where order_no is already present.
        self.data_dict[order_no]["Products"].append({"SKU":row[2],"QTY":row[3],"Price":row[4]})


    def read_csv(self):#csv reader function.
        with open('data.csv') as customer_data:#opening csv file.
            csv_reader = csv.reader(customer_data, delimiter=',')#creating reader and setting delimiter = ','
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    self.column_name_list = ",".join(row)#creating columnname list.
                    line_count += 1
                else:
                    self.country_Set.add(row[9])#creating country set.
                    order_numbers = self.key_finder()#getting order_no from dictionary.
                    if row[0] not in order_numbers:#If order no is not in the dictionary than add all data.
                        self.dictionary_updator(row)
                    elif row[0] in order_numbers:#if order number is already in dictionary than append only product.
                        self.product_updator(row[0],row)

            print(self.data_dict)

                        # if column_name_list[1] in self.key_finder(self.key_finder[row[0]]):#if customer is in dictionary
                        #     self.data_dict[row[0]]["Customer"].update
obj = CsvManipulation()
obj.read_csv()