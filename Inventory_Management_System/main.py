import json
import os
import util


class Category:
    def __init__(self, name, description):
        self.name = name
        self.new_name = None
        self.description = description
        self.new_desc = None

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
                json.dump(category, file, indent=4)
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
        self.new_name = name
        self.new_desc = description
        if os.path.exists('List_of_category.json'):
            with open('List_of_category.json', 'r') as file:
                udt_category = json.load(file)
        else:
            print('File not found')
            return

        if self.name not in udt_category:
            print(f'Category {self.name} does not exist')
            return

        if name is not None:
            if name not in udt_category:
                udt_category[self.name]['Name'] = self.new_name
                self.name = name
                print('Name has been changed')
            else:
                print(f"Category {self.new_name} already exist")

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
                display = json.load(file)

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
    list_of_items = []

    def __init__(self, name, category: Category, price, quantity, description):
        self.id_number = util.random_id()
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.description = description
        Item.list_of_items.append(self)

    def add_item(self):
        item_dict = {'Name': self.name, 'Category': self.category,
                     'Price': self.price, 'Quantity': self.quantity,
                     'Description': self.description}

        if os.path.exists('Inventory.json'):
            with open('Inventory.json', 'r') as file:
                opened = json.load(file)

            if self.id_number not in opened:
                opened[self.id_number] = item_dict
                with open('Inventory', 'w') as file:
                    json.dump(opened, file, indent=4)

            else:
                print('Item already exist')

        else:
            with open('Inventory.json', 'w') as file:
                json.dump({self.id_number: item_dict}, file, indent=4)

    def remove_item(self, id_number=None, name=None):
        self.id_number = id_number
        self.name = name
        try:
            with open('Inventory.json', 'r') as file:
                del_file = json.load(file)

            if name in del_file:
                del del_file[self.name]
                print(f'Item {self.name} was deleted')
            elif id_number in del_file:
                del del_file[self.id_number]
                print(f'Item with id number {self.id_number} was deleted')
            else:
                print('Item not found')

            with open('Inventory.json', 'w') as file:
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
            with open('Inventory.json', 'r') as file:
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

            with open('Inventory.json', 'w') as file:
                json.dump(udt_file, file, indent=4)

        except FileNotFoundError:
            print('Update failed, file not found')
        except json.JSONDecodeError:
            print('Update failed, file has corrupt')

    def display_item_info(self, id_number):
        self.id_number = id_number
        try:
            if os.path.exists('Inventory.json'):
                with open('Inventory.json', 'r') as file:
                    display = json.load(file)

                if self.id_number in display:
                    item = display[self.id_number]
                    print(f'Id Number \t= {self.id_number}\n '
                          f'Name \t= {item['Name']}\n'
                          f'Category \t= {item['Category']}\n'
                          f'Price \t= {item['Price']}'
                          f'Quantity \t= {item['Quantity']}'
                          f'Description \t= {item['Description']}')
                else:
                    print(f"Id number {self.id_number} does not exist")

        except FileNotFoundError:
            print('Retrieve info failed, file not found')
        except json.JSONDecodeError:
            print('Retrieve info failed, file has corrupt')

    @classmethod
    def display_all_item(cls):
        for item in cls.list_of_items:
            print(f'Id Number \t= {item.id_number}\n'
                  f'Name \t= {item.name}')


class Inventory:
    def __init__(self, items=Item, category=Category):
        self.item = items
        self.category = category
