import json
import jsonpickle
import os
import util
import csv


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
                print('Category successfully added')
            else:
                print('Category already exist')

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
                print(f'Category has been removed')
            else:
                print(f'Category {name} does not exist')

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
            print('File not found')
            return

        # Memeriksa apakah kategori ada di dalam file
        if self.name not in udt_category:
            print(f'Category {self.name} does not exist')
            return

        # Mengubah nama kategory ( jika parameter 'name' tidak None )
        if name is not None:
            if name not in udt_category:
                udt_category[name] = udt_category.pop(self.name)
                self.name = name
                print('Name has been changed')
            else:
                print(f"Category {name} already exist")
        else:
            print('Updating category canceled')

        # Mengubah deskripsi ( jika parameter 'description' tidak None )
        if description is not None:
            if description != udt_category[self.name]['Description']:
                udt_category[self.name]['Description'] = description
                print('Category description has been changed')
            else:
                print(f'The new description cannot be the same as the old description ')

        else:
            print('Updating category canceled')

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
            print('Item already exist in Item.json')

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
                print(f'Item with id number {id_number} not found in Item.json')

            if id_number in new_item:
                del new_item[id_number]
            else:
                print(f'Item with id number {id_number} not found in Short_inv.json')

            print(f'Item with id number {id_number} has been removed')
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
                        print(f"{'Name has been changed'}")
                    else:
                        print('Name cannot be the same as before')

                if price is not None:
                    if price != udt_file[id_number]['price']:
                        udt_file[id_number]['price'] = price
                        print('Price has been changed')
                    else:
                        print('Price cannot be the same as before')

                if quantity is not None:
                    if quantity != udt_file[id_number]['quantity']:
                        udt_file[id_number]['quantity'] = quantity
                        print('Quantity has been changed')
                    else:
                        print('Quantity cannot be the same as before')

                if description is not None:
                    if description != udt_file[id_number]['description']:
                        udt_file[id_number]['description'] = description.title()
                        print('Description has been changed')
                    else:
                        print('Description cannot be the same as before')
            else:
                print(f'Item with id number {id_number} not found')

            with open('Item.json', 'w') as file:
                json.dump(udt_file, file, indent=4)

        except FileNotFoundError:
            print('Update failed, file not found')
        except json.JSONDecodeError:
            print('Update failed, file has corrupt')

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
                    print(f"Id number {id_number} does not exist")

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

    def add_item_to_inventory(self):
        try:
            if os.path.exists('Inventory.json'):
                with open('Inventory.json', 'r') as file:
                    new_inv = json.load(file)
            else:
                new_inv = {}

            item_data = self.item.to_dict()
            category_name = self.category.name

            if item_data not in new_inv[category_name]:
                new_inv[category_name].append(item_data)
            else:
                print('Item already exist in the inventory')

            with open('Inventory.json', 'w') as file:
                json.dump(new_inv, file, indent=4)
                print('Item successfully added to inventory')

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

                del_item = del_item.from_dict()

                if name in del_item:
                    del del_item[name]
                else:
                    print(f"Name {name} doesn't exist ")

                with open('Inventory.json', 'w') as file:
                    json.dump(del_item, file, indent=4)
        except FileNotFoundError:
            print('File has missing')
        except json.JSONDecodeError:
            print('File has corrupt')

    @classmethod
    def generate_report(cls, instance):
        try:
            if os.path.exists('Inventory.json'):
                with open('Inventory.json', 'r') as file:
                    report = json.load(file)

                header = ['Id Number', 'Name', 'Price', 'Quantity', 'Description']
                with open(f'Inventory_{instance.category}.csv', 'w', encoding='UTF-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)

                for key, value in report.items():
                    with open(f'Inventory_{instance.category}.csv', 'a') as file:
                        writer = csv.writer(file)
                        data = [key, value['Name'], value['Price'], value['Quantity'], value['Description']]
                        writer.writerow(data)

        except TypeError:
            print('Type error')
        except json.JSONDecodeError:
            print('File has corrupt')
        except FileNotFoundError:
            print('File has missing')


# Creating instance category
# ATK = Category('ATK', 'Office stationary')
# FOOD = Category('Food', 'Something to eat')
# TOOL = Category('Tools', 'Device to create or fix something')

# # Creating instance item
# pena = Item('pena', 2000, 20, 'Alat untuk menulis')
# nasi = Item('Nasi', 3000, 10, 'Sesuatu untuk mengisi perut')
# wrench = Item('Wrench', 50000, 5, 'Kunci pas')
# screw_driver = Item('Screw_driver', 20000, 20,
#                     'A device to loosen or tightent screw')

# Item.update_item('QPNHEL9F', description='A device to loosen or tightent bolt')

# Item.remove_item('L33SIJY6')
# Item.display_all_items()
Item.display_item_info('QPNHEL9F')
# pena1 = Inventory(pena, ATK)
# pena1.add_item_to_inventory()

""" pr =
1. Tes hasil kode sebelum lanjut buat class inventory """
