import json
import jsonpickle
import os
import util
import csv
from tkinter.messagebox import showinfo


class Category:
    def __init__(self, name, description):
        self.name = name
        self.new_name = None
        self.description = description
        self.new_desc = None
        Category.add_category(self)

    def to_dict(self):
        name = self.name
        return name

    @classmethod
    def from_dict(cls, data):
        if isinstance(data, dict):
            return cls(
                name=data.get('name'),
                description=data.get('description')

            )

    def add_category(self):

        category_dict = {'Name': self.name, 'Description': self.description}

        if os.path.exists('List_of_category.json'):
            with open('List_of_category.json', 'r') as file:
                category = json.load(file)

            if self.name not in category:
                category[self.name] = category_dict

                with open('List_of_category.json', 'w') as file:
                    json.dump(category, file, indent=4)
                print('\nCategory successfully added')
            else:
                print('\nCategory already exist')

        else:
            category = {self.name: category_dict}
            with open('List_of_category.json', 'w') as file:
                file.write(jsonpickle.encode(category))
                print('Category successfully added')

    @classmethod
    def remove_category(cls, name):

        try:
            with open('List_of_category.json', 'r') as file:
                remove = json.load(file)

            if name in remove:
                del remove[name]
                print(f'\nCategory has been removed')
            else:
                print(f'\nCategory {name} does not exist')

            with open('List_of_category.json', 'w') as file:
                json.dump(remove, file, indent=4)

        except FileNotFoundError:
            print('File not found')
        except json.JSONDecodeError:
            print('Corrupted file')

    def update_category(self, name=None, description=None):

        # Mengecek keberadaan file 'List_of_category.json'
        if os.path.exists('List_of_category.json'):
            with open('List_of_category.json', 'r') as file:
                udt_category = json.load(file)
        else:
            print('\nFile not found')
            return

        # Memeriksa apakah kategori ada di dalam file
        if self.name not in udt_category:
            print(f'\nCategory {self.name} does not exist')
            return

        # Mengubah nama kategory ( jika parameter 'name' tidak None )
        if name is not None:
            if name != [i for i in udt_category.values()]:
                udt_category[self.name] = name
                self.name = name
                print('\nName has been changed')
            else:
                print(f"\nCategory {name} already exist")

        # Mengubah deskripsi ( jika parameter 'description' tidak None )
        if description is not None:
            if description != [d for d in udt_category.values()]:
                udt_category[self.name]['Description'] = description
                print('\nCategory description has been changed')
            else:
                print(f'\nThe new description cannot be the same as the old description ')

        with open('List_of_category.json', 'w') as file:
            json.dump(udt_category, file, indent=4)

    @classmethod
    def display_category_info(cls, name):

        try:
            with open('List_of_category.json', 'r') as file:
                display = jsonpickle.decode(file.read())

            if name in display:
                item = display[name]
                print(f'\nCategory \t\t= {item["Name"]}\n'
                      f'Description \t= {item["Description"]}')
            else:
                print(f"{name} doesn't exist ")

        except json.JSONDecodeError:
            print('Corrupted file')

        except FileNotFoundError:
            print('File not found')

    @classmethod
    def display_all_category(cls):
        try:
            with open('List_of_category.json', 'r') as file:
                display_all = json.load(file)

            for index, key in enumerate(display_all.keys()):
                print(f'{index + 1}. {key}')

        except FileNotFoundError:
            print('Corrupted file')
        except json.JSONDecodeError:
            print('File not found')


class Item:

    def __init__(self, name, price, quantity, description, id_number=None):

        self.id_number = id_number or util.random_id()
        self.name = name.title()
        self.price = price
        self.quantity = quantity
        self.description = description.title()
        Item.add_item(self)

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'description': self.description
        }

    @classmethod
    def from_dict(cls, data):
        if isinstance(data, dict):
            return cls(
                name=data.get('name'),
                price=data.get('price'),
                quantity=data.get('quantity'),
                description=data.get('description')
            )

    def add_item(self):

        item_dict = {'name': self.name,
                     'price': self.price,
                     'quantity': self.quantity,
                     'description': self.description}
        id_number = self.id_number

        if os.path.exists('Item.json'):
            with open('Item.json', 'r') as file:
                try:
                    item = json.load(file)
                except json.JSONDecodeError:
                    item = {}
        else:
            item = {}

        name = self.name

        if name not in [v['name'] for v in item.values()]:
            item[id_number] = item_dict

        else:
            print('\nItem already exist')

        if os.path.exists('Short_inv.json'):
            with open('Short_inv.json', 'r') as inv_file:
                try:
                    short_inv = json.load(inv_file)
                except json.JSONDecodeError:
                    short_inv = {}

        else:
            short_inv = {}

        if name not in [i for i in short_inv.values()]:
            short_inv[id_number] = item_dict['name']

        with open('Item.json', 'w') as file:
            json.dump(item, file, indent=4)

        with open('Short_inv.json', 'w') as inv:
            json.dump(short_inv, inv, indent=4)

    @classmethod
    def remove_item(cls, id_number=None):

        try:
            with open('Item.json', 'r') as file:
                del_file = json.load(file)

            with open('Short_inv.json', 'r') as item:
                new_item = json.load(item)

            if id_number in del_file:
                del del_file[id_number]
            else:
                print(f'\nItem with id number {id_number} not found in Item.json')

            if id_number in new_item:
                del new_item[id_number]
            else:
                print(f'\nItem with id number {id_number} not found in Short_inv.json')

            print(f'\nItem with id number {id_number} has been removed')
            with open('Item.json', 'w') as file:
                json.dump(del_file, file, indent=4)
            with open('Short_inv.json', 'w') as item:
                json.dump(new_item, item, indent=4)

        except FileNotFoundError:
            print('File not found')
        except json.JSONDecodeError:
            print('File has corrupt')

    @classmethod
    def update_item(cls, id_number, name=None, price: int = None,
                    quantity: int = None, description=None):

        try:
            with open('Item.json', 'r') as file:
                udt_file = json.load(file)

            if id_number in udt_file:
                if name is not None:
                    if name != udt_file[id_number]['name']:
                        udt_file[id_number]['name'] = name.title()
                        print(f"\n{'Name has been changed'}")
                    else:
                        print('\nName cannot be the same as before')

                if price is not None:
                    if price != udt_file[id_number]['price']:
                        udt_file[id_number]['price'] = price
                        print('\nPrice has been changed')
                    else:
                        print('\nPrice cannot be the same as before')

                if quantity is not None:
                    if quantity != udt_file[id_number]['quantity']:
                        udt_file[id_number]['quantity'] = quantity
                        print('\nQuantity has been changed')
                    else:
                        print('\nQuantity cannot be the same as before')

                if description is not None:
                    if description != udt_file[id_number]['description']:
                        udt_file[id_number]['description'] = description.title()
                        print('\nDescription has been changed')
                    else:
                        print('\nDescription cannot be the same as before')
            else:
                print(f'\nItem with id number {id_number} not found')

            with open('Item.json', 'w') as file:
                json.dump(udt_file, file, indent=4)

        except FileNotFoundError:
            print('\nUpdate failed, file not found')
        except json.JSONDecodeError:
            print('\nUpdate failed, file has corrupt')

    @classmethod
    def display_item_info(cls, id_number):
        try:
            if os.path.exists('Item.json'):
                with open('Item.json', 'r') as file:
                    display = json.load(file)

                if id_number in display:
                    item = display[id_number]
                    print(f'\nId Number \t\t= {id_number}\n'
                          f'Name \t\t\t= {item['name']}\n'
                          f'Price \t\t\t= {item['price']:,}\n'
                          f'Quantity \t\t= {item['quantity']}\n'
                          f'Description \t= {item['description']}\n')
                else:
                    print(f"\nId number {id_number} does not exist")

        except FileNotFoundError:
            print('Retrieve info failed, file not found')
        except json.JSONDecodeError:
            print('Retrieve info failed, file has corrupt')

    @classmethod
    def display_all_items(cls):
        try:
            if os.path.exists('Short_inv.json'):
                with open('Short_inv.json', 'r') as short_inv:
                    file = json.load(short_inv)
                for key, value in file.items():
                    print(f'\nId Number \t= {key}\n'
                          f'Name \t\t= {value}')

            else:
                print("File 'Short_inv.json' does not exist")
        except FileNotFoundError:
            print('File "Short_inv.json" not found')


class Inventory:
    def __init__(self, item: Item, category: Category):
        self.item = item
        self.category = category
        Inventory.add_item_to_inventory(self)

    def add_item_to_inventory(self):
        try:
            if os.path.exists('Inventory.json'):
                with open('Inventory.json', 'r') as file:
                    new_inv = json.load(file)
            else:
                new_inv = {}

            if os.path.exists('Item.json'):
                with open('Item.json', 'r') as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        print('Item.json has corrupt')
                        data = {}
            else:
                data = {}

            name = self.item.name
            id_number = util.find_key_by_value(data, name)

            item_data = {'name': self.item.to_dict()['name'],
                         'price': self.item.to_dict()['price'],
                         'quantity': self.item.to_dict()['quantity'],
                         'description': self.item.to_dict()['description']}

            category_name = self.category.name
            new_key = f'{category_name}_{id_number}'

            if new_key not in new_inv:
                new_inv[new_key] = item_data

                with open('Inventory.json', 'w') as file:
                    json.dump(new_inv, file, indent=4)
                    print('\nItem successfully added to inventory')
            else:
                print('\nItem already exist in the inventory')

        except FileNotFoundError:
            print('File not found')
        except json.JSONDecodeError:
            print('File has corrupt')

    @classmethod
    def remove_item_from_inventory(cls, name):
        try:
            if os.path.exists('Inventory.json'):
                with open('Inventory.json', 'r') as file:
                    del_item = json.load(file)

                del_name = util.find_key_by_value(del_item, name)

                if del_name in del_item:
                    del del_item[del_name]
                    print('Item deleted')
                else:
                    print(f"{name} doesn't exist in the inventory")

                with open('Inventory.json', 'w') as file:
                    json.dump(del_item, file, indent=4)
        except FileNotFoundError:
            print('File has missing')
        except json.JSONDecodeError:
            print('File has corrupt')

    @classmethod
    def generate_report(cls):
        try:
            if os.path.exists('Inventory.json'):
                with open('Inventory.json', 'r') as file:
                    report = json.load(file)

                header = ['Id Number', 'Category', 'Name', 'Price', 'Quantity', 'Description']
                with open(f'Inventory.csv', 'w', encoding='UTF-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)

                    for key, value in report.items():
                        data = [key[-8:-1], key[:-9], value['name'], value['price'],
                                value['quantity'], value['description']]
                        writer.writerow(data)

        except TypeError:
            print('Type error')
        except json.JSONDecodeError:
            print('File has corrupt')
        except FileNotFoundError:
            print('File has missing')

    @staticmethod
    def notify_stock_level(name, qty):
        message = f'Only {qty} {name} left or less in iventory'
        showinfo(title='Notification', message=message)

    @classmethod
    def track_stock_level(cls):
        try:
            with open('Inventory.json', 'r') as file:
                data = json.load(file)

            for key, value in data.items():
                if isinstance(value.get('quantity'), int) and value.get('quantity') <= 5:
                    name = value.get('name')
                    qty = value.get('quantity')
                    cls.notify_stock_level(name, qty)

        except json.JSONDecodeError:
            print('File corrupt')
        except FileNotFoundError:
            print('File has missing')


# # Creating instance category
# ATK = Category('ATK', 'Office stationary')
# FOOD = Category('Food', 'Something to eat')
# TOOL = Category('Tools', 'Device to create or fix something')
# ELECTRONIC = Category('Electronic',
#                       'A device that need electricity to activate')

# Category.remove_category('Electronic')
# ELECTRONIC.update_category(description='A device that require electricity to use')
# Category.display_category_info('Electronic')
# Category.display_all_category()

# # # Creating instance item
# pena = Item('pena', 2000, 20, 'Alat untuk menulis')
# nasi = Item('Nasi', 3000, 10, 'Sesuatu untuk mengisi perut')
# wrench = Item('Wrench', 50000, 5, 'Kunci pas')
# screw_driver = Item('Screw_driver', 20000, 20,
#                     'A device to loosen or tightent screw')
# paper = Item('Paper', 1000, 30, 'An object to write on')
# mie = Item('Mie', 15000, 23, 'Food made by flour')

# Item.update_item('QPNHEL9F', description='A device to loosen or tightent bolt')
# Item.update_item('QPNHEL9F', name='kunci pas')
# Item.remove_item('L33SIJY6')
# Item.display_all_items()
# Item.display_item_info('QPNHEL9F')
#
# obeng = Inventory(screw_driver, TOOL)
# nasi = Inventory(nasi, FOOD)
# pen = Inventory(pena, ATK)
# paper = Inventory(paper, ATK)
# mie = Inventory(mie, FOOD)
# wrench = Inventory(wrench, TOOL)

# Inventory.remove_item_from_inventory('Wrench')
# Inventory.generate_report()
Inventory.track_stock_level()
# Inventory.
""" pr =
1.  lanjut buat class inventory """
