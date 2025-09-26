import json
from pathlib import Path

class Task:
    def __init__(self, title, status=False) -> None:
        self.title = title
        self.status = status
    
    def toggle(self) -> None:
        self.status = not self.status

    def json_encoder(obj):
        return obj.__dict__

    def __str__(self) -> str:
        return f"{self.title} :: {'Done' if self.status else 'Not Done'}"

def mainLoop():
    todo_list = []
    sav_file = Path("todo.json")
    if sav_file.is_file():
        print('Loaded task file successfully')
        with open("todo.json", 'r') as f:
            dat = json.load(f)
            for item in dat:
                todo_list.append(Task(dict['title'], status=dict['status']))

    while True:
        print('\n========Todo List========')
        print('1. Display todo list.')
        print('2. Enter a new task.')
        print('3. Edit the list.')
        print('4. Save and Exit.')
        print('5. Exit Discarding Changes.')
        op = int(input('>> '))
        if op == 1:
            for i,j  in enumerate(todo_list, start=1):
                print(f"{i}. {j}")
        elif op == 2:
            title = input('Title: ')
            todo = Task(title)
            todo_list.append(todo)
        elif op == 3:
            for i,j  in enumerate(todo_list, start=1):
                print(f"{i}. {j}")
            num = int(input('Enter the todo you want to alter: '))
            print('1. Toggle Status')
            print('2. Delete Task')
            num1 = int(input(">> "))
            if num1 == 1:
                todo_list[num-1].toggle()
            if num1 == 2:
                del todo_list[num-1]
        elif op == 4:
            save_dat = json.dumps(todo_list, default=Task.json_encoder, indent=2) 
            with open("todo.json", "w") as f:
                f.write(save_dat)
            break
        elif op == 5:
            break

if __name__ == '__main__':
    mainLoop()
