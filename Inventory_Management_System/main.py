import json
import jsonpickle
import os
import util


class Category:
    def __init__(self, name, description):
        self.name = name
        self.new_name = None
        self.description = description
        self.new_desc = None

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

    def remove_category(self, name):
        self.name = name
        try:
            with open('List_of_category.json', 'r') as file:
                remove = json.load(file)

            if name in remove:
                del remove[name]
                print(f'Category has been removed')
            else:
                print(f'Category {name} does not exist')
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

        # Mengubah deskripsi ( jika parameter 'description' tidak None )
        if description is not None:
            if description != udt_category[self.name]['Description']:
                udt_category[self.name]['Description'] = description
                print('Category description has been changed')
            else:
                print(f'The new description cannot be the same as the old description ')

        with open('List_of_category.json', 'w') as file:
            json.dump(udt_category, file, indent=4)

    def display_category_info(self, name):
        self.name = name
        try:
            with open('List_of_category.json', 'r') as file:
                display = jsonpickle.decode(file.read())

            if self.name in display:
                item = display[self.name]
                print(f'Category \t= {item["Name"]}\n'
                      f'Description \t= {item["Description"]}')
            else:
                print(f"{self.name} doesn't exist ")

        except json.JSONDecodeError:
            print('Corrupted file')

        except FileNotFoundError:
            print('File not found')

    @classmethod
    def display_all_category(cls):
        try:
            with open('List_of_category.json', 'r') as file:
                display_all = json.load(file)

            for value in display_all.values():
                print(f'Category \t= {value["Category"]}\n'
                      f'Description \t= {value["Description"]}')

        except FileNotFoundError:
            print('Corrupted file')
        except json.JSONDecodeError:
            print('File not found')


class Item:

    def __init__(self, name, category: Category, price, quantity, description, id_number=None):

        if id_number is None:
            self.id_number = util.random_id()
        else:
            self.id_number = id_number
        self.name = name
        self.category = category.to_dict()
        self.price = price
        self.quantity = quantity
        self.description = description

    def add_item(self):
        item_dict = {'Name': self.name, 'Category': self.category,
                     'Price': self.price, 'Quantity': self.quantity,
                     'Description': self.description}
        id_number = self.id_number

        if os.path.exists('Item.json'):
            with open('Item.json', 'r') as file:
                try:
                    item = json.load(file)
                except json.JSONDecodeError:
                    item = {}
        else:
            item = {}

        if id_number not in item:
            item[id_number] = item_dict

            if os.path.exists('Short_inv.json'):
                with open('Short_inv.json', 'r') as inv_file:
                    try:
                        short_inv = json.load(inv_file)
                    except json.JSONDecodeError:
                        short_inv = {}

            else:
                short_inv = {}

            short_inv[id_number] = item_dict['Name']

            with open('Item.json', 'w') as file:
                json.dump(item, file, indent=4)

            with open('Short_inv.json', 'w') as inv:
                json.dump(short_inv, inv, indent=4)
        else:
            print('Item already exist in Item.json')

    def remove_item(self, id_number=None, name=None):
        self.id_number = id_number
        self.name = name
        try:
            with open('Item.json', 'r') as file:
                del_file = json.load(file)

            if name in del_file:
                del del_file[self.name]
                print(f'Item {self.name} was deleted')
            elif id_number in del_file:
                del del_file[self.id_number]
                print(f'Item with id number {self.id_number} was deleted')
            else:
                print('Item not found')

            with open('Item.json', 'w') as file:
                json.dump(del_file, file, indent=4)

        except FileNotFoundError:
            print('File not found')
        except json.JSONDecodeError:
            print('File has corrupt')

    def update_item(self, id_number: int, name=None, category=None, price: int = None,
                    quantity: int = None, description=None):
        self.id_number = id_number
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.description = description

        try:
            with open('Item.json', 'r') as file:
                udt_file = json.load(file)

            if id_number in udt_file:
                if name is not None:
                    udt_file[self.id_number]['Name'] = self.name
                    print('Name has been changed')
                if category is not None:
                    udt_file[self.id_number]['Category'] = self.category
                    print('Category has been changed')
                if price is not None:
                    udt_file[self.id_number]['Price'] = self.price
                    print('Price has been changed')
                if quantity is not None:
                    udt_file[self.id_number]['Quantity'] = self.quantity
                    print('Quantity has been changed')
                if description is not None:
                    udt_file[self.id_number]['Description'] = self.description
                    print('Description has been changed')
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
                    category_data = item['Category']
                    print(f'\nId Number \t\t= {id_number}\n'
                          f'Name \t\t\t= {item['Name']}\n'
                          f'Category \t\t= {category_data}\n'
                          f'Price \t\t\t= {item['Price']:,}\n'
                          f'Quantity \t\t= {item['Quantity']}\n'
                          f'Description \t= {item['Description']}\n')
                else:
                    print(f"Id number {id_number} does not exist")

        except FileNotFoundError:
            print('Retrieve info failed, file not found')
        except json.JSONDecodeError:
            print('Retrieve info failed, file has corrupt')

    @classmethod
    def display_all_item(cls):
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
    def __init__(self, items=Item, category=Category):
        self.item = items
        self.category = category


# Creating instance category
ATK = Category('ATK', 'Office stationary')
FOOD = Category('Food', 'Something to eat')
TOOL = Category('Tools', 'Device to create or fix something')
IT = Category('IT', 'Internet & Technology')

# Creating instance item
pena = Item('Pena', ATK, 2000, 20, 'Alat untuk menulis')
nasi = Item('Nasi', FOOD, 3000, 10, 'Sesuatu untuk mengisi perut')
wrench = Item('Wrench', TOOL, 50000, 5, 'Kunci pas')


# nasi.add_item()
# wrench.add_item()
Item.display_all_item()
Item.display_item_info('5UKGD0L4')
IT.add_category()

