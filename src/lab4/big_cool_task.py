class Orders:
    def __init__(self):
        self.orders = []
        self.passed_1 = []
        self.failed_1 = []
        self.passed_2 = []
        self.failed_2 = []
        self.valid_orders = []
        self.sorted_orders = []
        self.valid_arr_for_tests = []
        self.non_valid_arr_for_tests = []
        with open("txtf/orders.txt", 'r', encoding="utf-8") as f:
            for i in f:
                line = i.strip().split(';')
                id = int(line[0])
                products = line[1].strip().split(',')
                fio = line[2].strip()
                address = line[3].strip()
                number = line[4]
                priority = line[5]

                self.orders.append({'ID': id, 'Products': products, 'FIO': fio, 'Address': address, 'Number': number,
                               'Priority': priority})


    def check_error_type_one(self):
        for i in self.orders:
            if i['Address'] == '':
                non_valid = str(i['ID']) + ';1;no data'
                self.failed_1.append(non_valid)
            elif len(i['Address'].strip().split('.')) < 4:
                non_valid = str(i['ID']) + ';1;' + str(i['Address'])
                self.failed_1.append(non_valid)
            else:
                self.passed_1.append(i)


    def check_error_type_two(self):
        for i in self.orders:
            if len(i['Number']) == 16:
                n = i['Number']
                if n[0] == '+'  and n[2] == '-' and n[6] == '-' and n[10] == '-' and n[13] == '-':
                    if n[1].isdigit() and n[3:5].isdigit() and n[7:9].isdigit() and n[11:12].isdigit() and n[14:16].isdigit():
                        self.passed_2.append(i)
                    else:
                        non_valid = str(i['ID']) + ';2;' + str(i['Number'])
                        self.failed_2.append(non_valid)
                else:
                    non_valid = str(i['ID']) + ';2;' + str(i['Number'])
                    self.failed_2.append(non_valid)
            else:
                non_valid = str(i['ID']) + ';2;' + str(i['Number'])
                self.failed_2.append(non_valid)


    def group_non_valid_orders(self):
        failed = []
        for i in self.failed_2:
            failed.append(i)
        for j in self.failed_1:
            failed.append(j)
        with open('txtf/non_valid_orders.txt', 'w', encoding='utf-8') as f:
            for i in failed:
                f.write(i + '\n')
                self.non_valid_arr_for_tests.append(i + '\n')
                print(i)



    def group_valid_orders(self):
        for i in self.passed_1:
            if i in self.passed_2:
                self.valid_orders.append(i)


    def products(self):
        for order in self.valid_orders:
            product_count = {}
            combined_products_arr = []
            for product in order['Products']:
                product = product.strip()
                if product in product_count:
                    product_count[product] += 1
                else:
                    product_count[product] = 1

            for product, count in product_count.items():
                if count > 1:
                    combined_products_arr.append(f"{product} x{count}")
                elif count <= 1:
                    combined_products_arr.append(product)
            combined_products = ', '.join(combined_products_arr)
            order['Products'] = combined_products


    def sort_orders(self):
        russian_orders = []
        foreign_orders = []

        for order in self.valid_orders:
            address_parts = order['Address'].strip().split('.')
            if 'Россия' in address_parts:
                russian_orders.append(order)
            else:
                foreign_orders.append(order)

        russian_orders.sort(key=lambda x: (x['Priority'], x['Address']))
        foreign_orders.sort(key=lambda x: x['Address'].split('.')[0])
        self.sorted_orders = russian_orders + foreign_orders

    def write_output(self):
        with open('txtf/order_country', 'w', encoding='utf-8') as f:
            for i in self.sorted_orders:
                a = str(i['ID'])+';'+str(i['Products'])+';'+str(i['FIO'])+';'+str(i['Address'])+';'+str(i['Number'])+';'+str(i['Priority'])
                f.write(a + '\n')
                self.valid_arr_for_tests.append(a + '\n')

    def result_function(self):
        self.check_error_type_one()
        self.check_error_type_two()
        self.group_valid_orders()
        self.products()
        self.group_non_valid_orders()
        self.sort_orders()
        self.write_output()


def main():
    ord = Orders()
    ord.result_function()

if __name__ == "__main__":
    main()