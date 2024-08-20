import datetime
import json
import util
import os
import time
from util import is_valid_date


def Create(filename):
    n = 1

    while True:
        data = util.template.copy()
        # input user
        data['task'] = input('\nInput your task: ').title()
        data['place'] = input('Input place: ').title()
        while True:
            year = input('Input year (yyyy): ')
            if len(year) == 4:
                if year.isdigit():
                    year = int(year)
                    break
                else:
                    print('year must be a number')
            else:
                print('Year must be 4 digit!')

        while True:
            month = input('Input month (1-12): ')
            if month.isdigit():
                month = int(month)
                if not 1 <= month <= 12:
                    print('Input only 1 - 12')
                    continue
                else:
                    break
            else:
                print('Month must be a number!')
                continue

        while True:
            day = input('Input date 1 - 30: ')
            if day.isdigit():
                day = int(day)
                if not 1 <= day <= 30:
                    print('Input only 1 - 30')
                    continue
                else:
                    break
            else:
                print('Day must be a number')
                continue

        date = datetime.datetime(year, month, day)
        data['date'] = date.strftime('%d-%m-%Y')

        content = {f'task_to_do_{n}': {'task': data['task'], 'place': data['place'],
                                       'date': data['date']}}

        if os.path.exists(filename):
            try:
                with open(filename, 'r') as file_read:
                    open_data = json.load(file_read)

            except TypeError:
                print('Opening file error')

            try:
                open_data.update(content)
                with open(filename, 'w') as add_data:
                    json.dump(open_data, add_data, indent=4)
                n += 1
            except TypeError:
                print('Enter data error')

        else:

            try:
                with open(filename, 'w', encoding='utf-8') as json_file:
                    json.dump(content, json_file, indent=4)
                    n += 1

            except TypeError:
                print('Error')

        index = 'No'
        task = 'Task'
        place = 'Place'
        date = 'Date'

        print('Your current task to do')
        print('\n' + '=' * 100)
        print(f'{index:4} | {task:30} | {place:30} | {date:12}')
        print('-' * 100)

        try:
            with open(filename, 'r') as json_file:
                loaded_data = json.load(json_file)

            n = 1
            for index, (key, value) in enumerate(loaded_data.items()):
                data = f"task_to_do_{n}"

                task = loaded_data[data]['task']
                place = loaded_data[data]['place']
                date = loaded_data[data]['date']

                print(f'{index + 1:<4} | {task:30} | {place:30} | {date:12}')
                n += 1

        except TypeError:
            print('Reading file filed')
        print('=' * 100 + '\n')

        while True:
            verif = input('Finish create? y/n: ')

            if verif.lower() in ['y', 'n']:
                if verif == 'y':
                    return
                else:
                    break
            else:
                print('Input only y or n')
                continue


def Read(filename):
    while True:

        if os.path.exists(filename):
            index = 'No'
            task = 'Task'
            place = 'Place'
            date = 'Date'

            print('Your current task to do')
            print('\n' + '=' * 100)
            print(f'{index:4} | {task:30} | {place:30} | {date:12}')
            print('-' * 100)

            try:
                with open(filename, 'r') as json_file:
                    loaded_data = json.load(json_file)

                n = 1
                for index, (key, value) in enumerate(loaded_data.items()):
                    data = f"task_to_do_{n}"

                    task = loaded_data[data]['task']
                    place = loaded_data[data]['place']
                    date = loaded_data[data]['date']

                    print(f'{index+1:<4} | {task:30} | {place:30} | {date:12}')
                    n += 1

            except TypeError:
                print('Reading file filed')
            print('=' * 100 + '\n')
            confirm = input('Exit (y/n): \n').lower()
            match confirm:
                case 'y':
                    break
                case _:
                    print('Input only y/n')

        else:
            print('No task to show, you will redirect to main menu immediately')
            time.sleep(2)
            break


def Update(filename):
    while True:
        if os.path.exists(filename):
            try:

                no = 'No'
                task = 'Task'
                location = 'Location'
                date = 'Date'

                print(f'''\nThese are current task to do: \n''')
                print('=' * 100)
                print(f'{no:4} | {task:25} | {location:40} | {date:12}')
                print('-' * 100)

                # membuka file
                with open(filename, 'r') as update_file:
                    update_file = json.load(update_file)
                    # menampilkan file yang telah dibuka
                for index, (key, value) in enumerate(update_file.items()):

                    Task = value['task']
                    Place = value['place']
                    Date = value['date']

                    print(f'{index + 1:<4} | {Task:25} | {Place:40} | {Date:12}')

                print('=' * 100 + '\n')

                # meminta input nomer file
                while True:
                    no_task = int(input('Input number you want to update: '))

                    file_task = f'task_to_do_{no_task}'
                    # mengecek jika nomor file ada di daftar
                    if file_task in update_file:
                        break
                    else:
                        print('Invalid number')

                Task = update_file[file_task]['task']
                Place = update_file[file_task]['place']
                Date = update_file[file_task]['date']

                while True:
                    print('\n' + '=' * 100)
                    print(f'1. Task\t\t: {Task:40}')
                    print(f'2. Place\t: {Place:40}')
                    print(f'3. Date\t\t: {Date:12}')

                    user_option = int(input('Choose data you want to update 1/2/3: '))
                    print('\n' + '=' * 100)
                    match user_option:
                        case 1: Task = input('New task\t: ').title()
                        case 2: Place = input('New Place\t: ').title()
                        case 3:
                            while True:
                                while True:
                                    day = input('New Date\t: ')
                                    if day.isdigit():
                                        day = int(day)
                                        if 1 <= day <= 31:
                                            break
                                        else:
                                            print('Day must be between 1 - 31')
                                            continue
                                    else:
                                        print('Day must be a digit')

                                while True:
                                    month = input('New Month\t: ')
                                    if month.isdigit():
                                        month = int(month)
                                        if 1 <= month <= 12:
                                            break
                                        else:
                                            print('Month must be between 1-12')
                                            continue
                                    else:
                                        print('Month must be a digit')

                                while True:
                                    year = input('New Year\t: ')
                                    if len(year) == 4:
                                        if year.isdigit():
                                            if not year.startswith('0'):
                                                year = int(year)
                                                break
                                            else:
                                                print('Year cannot start from 0')
                                                continue
                                        else:
                                            print('Year must be a digit')
                                            continue
                                    else:
                                        print('Year must be 4 digit')
                                    continue

                                if is_valid_date(year, month, day):
                                    Date = datetime.datetime(year, month, day)
                                    Date = Date.strftime('%d-%m-%Y')
                                else:
                                    print('Incorrect input')
                                    continue

                    print('Your new data:')
                    print(f'1. Task\t\t: {Task}')
                    print(f'2. Place\t: {Place}')
                    print(f'3. Date\t\t: {Date}')

                    while True:
                        done = input('Is the data correct ? y/n: ').lower()
                        if done in ['y', 'n']:
                            if done == 'y':
                                break
                        else:
                            print('Choose only y or n')

                    with open(filename, 'r') as update_data:
                        data = json.load(update_data)

                    data[file_task]['task'] = Task
                    data[file_task]['place'] = Place
                    data[file_task]['date'] = Date

                    with open(filename, 'w') as file:
                        json.dump(data, file, indent=4)
                        print('Data has been updated')

                    while True:
                        finish_update = input('Finish? y/n : ').lower()

                        if not finish_update.isdigit():
                            if finish_update in ['y', 'n']:
                                if finish_update == 'y':
                                    return
                                else:
                                    break
                            else:
                                print('Choose only y or n')
                                continue
                        else:
                            print('Choose only y or n')
                            continue

            except TypeError:
                print('Failed')

        else:
            print('No task to update, you will redirect to main menu immediately')
            time.sleep(2)
            break