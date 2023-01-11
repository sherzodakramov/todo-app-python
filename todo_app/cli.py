import functions
import time

now = time.strftime("%b %d, %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):

        todo = user_action[4:]

        # Mavjud "todos.txt" fayl ichini ochib, o'qiymiz va "file" nomli o'zgaruvchiga yuklaymiz.
        # file = open("files/todos.txt", 'r')

        # O'zgaruvchi ichidagi ma'lumotlarni "todos" nomli list sifatida saqlaymiz.
        # todos = file.readlines()
        # file.close()

        # todos.append(todo)

        todos = functions.get_todos()

        todos.append(todo + '\n')

        # "todos.txt" nomli qayta fayl ustidan yozib, unga "todos" deb saqlagan listimizni yozamiz.
        # file = open("files/todos.txt", 'w')
        # file.writelines(todos)
        # file.close()

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        # file = open("files/todos.txt", 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()

        # Solution number 1 to strip '\n' from items by using for loop.
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
        # print(todos)

        # Solution number 2 to strip '\n' from items by using list comprehensions.
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
print('Thanks, bye!')
