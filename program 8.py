import csv
from openpyxl import Workbook#importing required library.

class CsvManipulation:
    def __init__(self):
        self.data_dict = {}
        self.country_dict = {'ES':'Espanol' ,
                             'DE':'Denmark',
                             'USA':'United States Of America' ,
                             'UK':'United Kingdom',
                             'AU': 'Australia',
                             'IT': 'Italy'
                             }#country code to country name provision.
        self.column_name_list = []
    def key_finder(self):#key of dictionary finder.
        list_keys = list(self.data_dict.keys())
        return list_keys

    def dictionary_updator(self,row):#dictionary row updater.
        self.data_dict.update({row[0]:{"Customer":{"Name":row[1] ,
                                                   "Add 1":row[5] ,
                                                   "Add 2":row[6] ,
                                                   "Zipcode":row[7],
                                                   "City":row[8],
                                                   "Country": self.country_dict[row[9]]
                                                   },
                                       "Products":[{"SKU": row[2],
                                                   "QTY":row[3],
                                                   "Price":row[4]
                                                   }]
                                       }
                               })

    def product_updator(self,order_no,row):#dictionary product appender.
        self.data_dict[order_no]["Products"].append({"SKU":row[2],"QTY":row[3],"Price":row[4]})


    def read_csv(self):#reader function.
        with open('data.csv') as customer_data:
            csv_reader = csv.reader(customer_data, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    self.column_name_list = ",".join(row)
                    line_count += 1
                else:

                    new_list = self.key_finder()
                    if row[0] not in new_list:#If order no is not in the dictionary than update whole row.
                        self.dictionary_updator(row)
                    elif row[0] in new_list:#if order no is in the dictionary than append only product.
                        self.product_updator(row[0],row)

    def write_xsl(self):#writer to xsl.
        wb = Workbook()#creating workbench object.
        sheet1 = wb.active#activating the excel sheet.

        for order_no, data in self.data_dict.items():
            for product in data["Products"]:
                sheet1.append([order_no,
                                     data["Customer"]["Name"],
                                     product["SKU"],
                                     product["QTY"],
                                     product["Price"],
                                     data["Customer"]["Add 1"],
                                     data["Customer"]["Add 2"],
                                     data["Customer"]["Zipcode"],
                                     data["Customer"]["City"],
                                     data["Customer"]["Country"]])
                #appending data to the sheet.
        wb.save("myexcel.xlsx")#saving sheet.
obj = CsvManipulation()
obj.read_csv()
obj.write_xsl()
