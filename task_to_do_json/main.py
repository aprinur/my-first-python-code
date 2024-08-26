import util
import operation

name = input('Input name: ').title()
filename = name + '_task.json'

while True:

    opsi = input('''\nWelcome to task to do app
1. Create task
2. Show task
3. Update task
4. Delete task
5. Exit program

Input your choice 1/2/3/4/5 : ''')
    match opsi:
        case '1':
            operation.Create(filename)
        case '2':
            operation.Read(filename)
        case '3':
            operation.Update(filename)
        case '4':
            operation.Delete(filename)
        case '5':
            util.close()
        case _:
            print('Number invalid')
