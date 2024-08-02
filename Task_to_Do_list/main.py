from Task_to_Do_list import Operation
import time

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
                print('program will be exit in')
                print('3')
                time.sleep(1)
                print('2')
                time.sleep(1)
                print('1')
                time.sleep(1)
                print('Program finish')
                time.sleep(1)

                exit()
            else:
                print('Number invalid')

        except ValueError:
            print('Number only')


if __name__ == '__main__':
    task()