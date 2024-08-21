from Task_to_Do_list import Operation

task_to_do = []


def task():
    while True:
        try:
            opsi = int(input('''\nWelcome to task to do app
1. Create task
2. Show task
3. Update task
4. Delete task
5. Exit program

Input your choice 1/2/3/4/5 : '''))

            if opsi == 1:
                Operation.create()
            elif opsi == 2:
                Operation.read()
            elif opsi == 3:
                Operation.update()
            elif opsi == 4:
                Operation.delete()
            elif opsi == 5:
                print('Exit option choosen')
                exit()
            else:
                print('Number invalid')

        except ValueError:
            print('Number only')


if __name__ == '__main__':
    task()