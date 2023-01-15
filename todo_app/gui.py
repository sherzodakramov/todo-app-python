import functions
import PySimpleGUI as sg
import time

sg.theme("DarkPurple4")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button]],
                   font=("Helvetica", 15))

while True:
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    event, values = window.read(timeout=200)
    """ window.read() in this case provide the tuple, 
    and we stored elements of this tuple into two 
    variables which named as 'event' and 'values' """
    # print(1, event)
    # print(2, values)
    # print(3, values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                """Getting the todo that the user selected"""
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()

                """Update todos by replacing the existing todo with the new todo"""
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                """Update list-box and display todos with the new todo"""
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.",
                         font=("Helvetica", 15))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.",
                         font=("Helvetica", 15))
        case 'Exit':
            break
        case 'todos':
            """Display selected todo in the input box"""
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()


"""
The event is getting a value in the input box and pressing the button

('Add', {'todo': 'Hi'})

'Add' - label of the button
'todo' - input box, input text instance ('todo' - that input box's key)
'Hi' - value of that instance.

Event gets the value of add the first item of that tuple and values.
Get the the value of this dictionary because actually.
The press of a button is an event.
So event is getting the label of the button which was pressed.
And the values variable is getting the values that were filled by the user.

window['todos'] - instance of list box
window['todo'] - instance of input box
"""
