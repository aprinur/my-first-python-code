import json
import os


class MenuItem:

    def __init__(self, name, price, category, material_stock):
        self.name = name
        self.price = price
        self.category = category
        self.material = material_stock

    def display(self):
        try:
            # membuka file foodlist.json
            with open('foodlist.json') as foodlist:
                dish = json.load(foodlist)

            # mengecek apakah item ada di dalam data json
            if self.name in dish:

                # menampilkan informasi item dari file json
                item = dish[self.name]
                print(f"Name = {item['Name']}")
                print(f'Price = {item["Price"]}')
                print(f'Category = {item["Category"]}')
                print(f'Stock = {"Available" if item["Stock"] == "Available" else "Not available"}')

            else:
                print(f"Item '{self.name}' not found in the food list.")

        except FileNotFoundError:
            print('File not found')
        except json.JSONDecodeError:
            print('Error reading JSON file ')

    def add_menu(self):
        food_list = {
            'Name': self.name,
            'Price': self.price,
            'Category': self.category,
            'Stock': f'Available' if self.material else 'Not Available'
        }
        # mengecek keberadaan file
        if os.path.exists('foodlist.json'):
            with open('foodlist.json', 'r') as menu:

                try:
                    # membaca file JSON yang sudah ada
                    file = json.load(menu)
                except json.JSONDecodeError:
                    # jika file kosong atau tidak valid, membuat dictionary kosong
                    file = {}

            # menambahkan/update entry baru ke data yang ada dengan key sebagai nama menu
            file[self.name] = food_list

        else:
            # jika file tidak ada, membuat dictionary baru untuk data
            file = {self.name: food_list}

        # menyimpan dictionary ke dalam file
        with open('foodlist.json', 'w') as menu:
            json.dump(file, menu, indent=4)

    def update_stock(self, status: str):
        try:
            with open('foodlist.json', 'r') as update:
                new = json.load(update)

            if self.name in new:
                new[self.name]['Stock'] = status
            else:
                print(f"Item '{self.name}' not found in the menu")

            with open('foodlist.json', 'w') as update:
                json.dump(new, update, indent=4)
        except FileNotFoundError:
            print('File not found')
        except json.JSONDecodeError:
            print('Error reding JSON file')

    @staticmethod
    def delete_menu(self, name):
        try:
            if os.path.exists('foodlist.json'):
                with open('foodlist.json', 'r') as delete:
                    data = json.load(delete)

                if name in data:
                    del data[name]
                    print(f'{name} deleted')
                else:
                    print(f'{name} not found in the menu')

                with open('foodlist.json', 'w') as new_file:
                    json.dump(data, new_file)

        except FileNotFoundError:
            print('File not found')
        except json.JSONDecodeError:
            print('Error reding JSON file')


class Order:
    def __init__(self, menu, quantity, table_number):
        self.food = menu
        self.quantity = quantity
        self.table_number = table_number
        self.items = {}

    def add_item(self, item, quantity):
        with open('foodlist.json', 'r') as add:
            menu = json.load(add)

        if item in menu:
            if menu[item]['Stock'] == 'Available':
                self.items[item] = quantity
            else:
                print('Menu not available')
        else:
            print(f'Food name {item} not available in the menu')

    def remove_order(self, item):
        if item in self.items:
            del self.items[item]
            print('Order Deleted')
        else:
            print('Order name not available')

    def calculate_total(self,):
        total_price = 0

        with open('foodlist.json', 'r') as file:
            total = json.load(file)

        for item, quantity in self.items.items():
            if item in total:
                if total[item]['Stock'] == 'Available':
                    price = total[item]['Price']
                    total_price += price * quantity
                else:
                    print(f'Item "{item}" not available (out of stock)')
            else:
                print(f'Food name {item} not available in the menu')

        print(f'Total price for table number {self.table_number} is : {total_price}')
        return total_price


food1 = MenuItem('Nasi goreng', 15000, 'main dish', 'Available')
food1.add_menu()
food1.display()
food2 = MenuItem('Salad', 10000, 'Side dish', 'Available')
food2.add_menu()
food2.display()
food1.update_stock('Not Available')
food1.display()
food3 = MenuItem('Gado gado', 10000, 'main dish', 'Available')
food3.add_menu()
food3.display()
food1.update_stock('Available')
order1 = Order(menu=None, quantity=None, table_number=5)
order1.add_item('Nasi goreng', 2)
order1.add_item('Salad', 2)
order1.calculate_total()


