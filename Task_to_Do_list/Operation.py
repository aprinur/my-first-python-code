import datetime
import string
import time
from Task_to_Do_list import main


task_to_do = []


def create():
    while True:
        while True:
            name = input('Input name of the task: ')
            name = name.title()
            if name == string.ascii_letters or string.whitespace or string.digits:
                break
            else:
                print('location must be an alfabet or a number or combination of both')

        while True:
            location = input('Input place of the task: ')
            location = location.title()
            if location == string.ascii_letters or string.whitespace or string.digits:
                break
            else:
                print('location must be an alfabet or a number or combination of both')

        while True:
            date = input('Input Date (1-31): ')
            if date.isdigit():
                date = int(date)
                if not (1 <= date <= 31):
                    print('Date must be 1 - 31')
                    continue
                else:
                    break
            else:
                print('Date must be a number')
                continue

        while True:
            month = input('Input month (1-12): ')
            if month.isdigit():
                month = int(month)
                if not (1 <= month <= 12):
                    print('Month must be 1 - 12 ')
                    continue
                else:
                    break
            else:
                print('Month must be a number')
                continue

        while True:
            year = input('Input Year (yyyy): ')
            if year.isdigit():
                if not year.startswith('0'):
                    if len(year) == 4:
                        year = int(year)
                        break
                    else:
                        print('year must be 4 digit')
                        continue
                else:
                    print('Year cannot start from 0 ')
                    continue
            else:
                print('Year must be a number')
                continue

        try:
            time_to_do = datetime.datetime(year, month, date)
            new_list = (name, location, time_to_do)
            task_to_do.append(new_list)
        except ValueError:
            print('There is a problem with the data you entered')

        seq = 'No'
        name = 'Name'
        location = 'Location'
        date = 'Date'

        print(f'''\nThese are current task to do: \n''')
        print('=' * 100)
        print(f'{seq:4} | {name:25} | {location:40} | {date:12}')
        print('-' * 100)

        for index, data in enumerate(task_to_do):
            Name = data[0]
            Location = data[1]
            Date = data[2]

            print(f'{index+1:<4} | {Name:25} | {Location:40} | {Date:%d-%m-%Y}')

        while True:
            confirm = input('\nContinue Input y/n: ')
            if confirm.isdigit():
                print('Input must be an alfabet')
                continue
            else:
                if confirm.lower() in ['y', 'n']:
                    if confirm.lower() == 'n':
                        return
                    else:
                        break
                else:
                    print("Choose only 'y' or 'n'")
                    continue


def read():
    while True:
        if len(task_to_do) != 0:
            no = 'No'
            task = 'Task'
            location = 'Location'
            date = 'Date'

            print(f'''\nThese are current task to do: \n''')
            print('=' * 100)
            print(f'{no:4} | {task:25} | {location:40} | {date:12}')
            print('-' * 100)

            for index, data in enumerate(task_to_do):
                Name = data[0]
                Location = data[1]
                Date = data[2]

                print(f'{index + 1:<4} | {Name:25} | {Location:40} | {Date:%d-%m-%Y}')

            while True:
                confirm = input('\nExit y/n: ')
                if confirm.isdigit():
                    print('Input must be an alfabet')
                    continue
                else:
                    if confirm.lower() in ['y', 'n']:
                        if confirm.lower() == 'y':
                            return
                        else:
                            break
                    else:
                        print("Choose only 'y' or 'n'")
                        continue

        else:
            print('Yout task is empty')
            print('You will redirect to main menu immediately')
            time.sleep(2)
            break


def update():
    if len(task_to_do) == 0:
        print('Yout task is empty')
        print('You will be redirect to main menu immediately')
        time.sleep(2)
        main.task()

    else:
        no = 'No'
        task = 'Task'
        location = 'Location'
        date = 'Date'

        print(f'''\nThese are current task to do: \n''')
        print('=' * 100)
        print(f'{no:4} | {task:25} | {location:40} | {date:12}')
        print('-' * 100)

        for index, data in enumerate(task_to_do):
            Name = data[0]
            Location = data[1]
            Date = data[2]

            print(f'{index + 1:<4} | {Name:25} | {Location:40} | {Date:%d-%m-%Y}')

        while True:
            no_task = int(input('\nInput number of task you want to update: '))

            if no_task:
                break
            else:
                print('Invalid input')

        task_name = task_to_do[no_task-1][0]
        task_location = task_to_do[no_task-1][1]
        task_date_of_month = task_to_do[no_task-1][2]

        while True:
            print('\n'+'='*100)
            print(f'1. Name\t: {task_name}')
            print(f'2. Location: {task_location}')
            print(f'3. Date\t: {task_date_of_month:%d-%m-%Y}')

            user_option = input('Choose field you want to update 1/2/3: ')
            print('\n'+'='*100)
            match user_option:
                case '1': task_name = input('Update task\t: ')
                case '2': task_location = input('Update location\t: ')
                case '3':

                    while True:
                        task_date = input('Input Date (1-31): ')
                        if task_date.isdigit():
                            task_date = int(task_date)
                            if not (1 <= task_date <= 31):
                                print('Date must be 1 - 31')
                                continue
                            else:
                                break
                        else:
                            print('Date must be a number')
                            continue

                    while True:
                        task_month = input('Input month (1-12): ')
                        if task_month.isdigit():
                            task_month = int(task_month)
                            if not (1 <= task_month <= 12):
                                print('Month must be 1 - 12 ')
                                continue
                            else:
                                break
                        else:
                            print('Month must be a number')
                            continue

                    while True:
                        task_year = input('Input Year (yyyy): ')
                        if task_year.isdigit():
                            if not task_year.startswith('0'):
                                if len(task_year) == 4:
                                    task_year = int(task_year)
                                    break
                                else:
                                    print('year must be 4 digit')
                                    continue
                            else:
                                print('Year cannot start from 0 ')
                                continue
                        else:
                            print('Year must be a number')
                            continue

                    new_date = datetime.datetime(task_year, task_month, task_date)
                    task_date_of_month = new_date

                case _:
                    print('Number not available')

            task_to_do[no_task-1] = (task_name.title(), task_location.title(), task_date_of_month)

            print('Your updated task:')
            print(f'1. Task\t: {task_to_do[no_task-1][0]}')
            print(f'2. Location\t: {task_to_do[no_task-1][1]}')
            print(f'3. Date\t: {task_to_do[no_task-1][2]:%d-%m-%Y}')

            no = 'No'
            task = 'Task'
            location = 'Location'
            date = 'Date'

            print(f'''\nThese are all task after updated: \n''')
            print('=' * 100)
            print(f'{no:4} | {task:25} | {location:40} | {date:12}')
            print('-' * 100)

            for index, data in enumerate(task_to_do):
                Name = data[0]
                Location = data[1]
                Date = data[2]

                print(f'{index + 1:<4} | {Name:25} | {Location:40} | {Date:%d-%m-%Y}')

            while True:
                confirm = input('\nContinue updating data? y/n: ')
                if confirm.isdigit():
                    print('Input must be an alfabet')
                    continue
                else:
                    if confirm.lower() in ['y', 'n']:
                        if confirm.lower() == 'n':
                            return
                        else:
                            break
                    else:
                        print("Choose only 'y' or 'n'")
                        continue


def delete():
    while True:
        if len(task_to_do) == 0:
            print('Yout task is empty')
            print('You will be redirect to main menu immediately')
            time.sleep(2)
            main.task()

        else:
            no = 'No'
            task = 'Task'
            location = 'Location'
            date = 'Date'

            print(f'''\nThese are current task to do: \n''')
            print('=' * 100)
            print(f'{no:4} | {task:25} | {location:40} | {date:12}')
            print('-' * 100)

            for index, data in enumerate(task_to_do):
                Name = data[0]
                Location = data[1]
                Date = data[2]

                print(f'{index + 1:<4} | {Name:25} | {Location:40} | {Date:%d-%m-%Y}')

            while True:
                no_task = int(input('\nInput number of task you want to delete: '))

                if no_task:
                    break
                else:
                    print('Invalid number')

            print(f'1. Task\t: {task_to_do[no_task - 1][0]}')
            print(f'2. Location\t: {task_to_do[no_task - 1][1]}')
            print(f'3. Date\t: {task_to_do[no_task - 1][2]:%d-%m-%Y}')

            while True:
                confirm = input('Are you sure want to delete the task y/n: ')

                if confirm.isdigit():
                    print('Input must be an alfabet')
                    continue
                else:
                    if confirm.lower() in ['y', 'n']:
                        if confirm.lower() == 'y':
                            del task_to_do[no_task - 1]
                            print('Task deleted')
                            break
                        else:
                            break
                    else:
                        print("Choose only 'y' or 'n'")
                        continue
            while True:
                if len(task_to_do) != 0:
                    no = 'No'
                    task = 'Task'
                    location = 'Location'
                    date = 'Date'

                    print(f'''\nThese are task to do after deletion: \n''')
                    print('=' * 100)
                    print(f'{no:4} | {task:25} | {location:40} | {date:12}')
                    print('-' * 100)

                    for index, data in enumerate(task_to_do):
                        Name = data[0]
                        Location = data[1]
                        Date = data[2]

                        print(f'{index + 1:<4} | {Name:25} | {Location:40} | {Date:%d-%m-%Y}')

                    while True:
                        isdone = input('\nContinue deleting task y/n: ')
                        if isdone.isdigit():
                            print('Input must be an alfabet')
                            continue
                        else:
                            if isdone.lower() in ['y', 'n']:
                                if isdone.lower() == 'n':
                                    return
                                else:
                                    break
                            else:
                                print("Choose only 'y' or 'n'")
                                continue

                else:
                    break



