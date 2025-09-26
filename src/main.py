class Task:
    def __init__(self, title) -> None:
        self.title = title
        self.status = False
    
    def toggle(self) -> None:
        self.status = not self.status
    def __str__(self) -> str:
        return f"{self.title} :: {'Done' if self.status else 'Not Done'}"

def mainLoop():
    todo_list = []
    while True:
        print('\n========Todo List========')
        print('1. Display todo list.')
        print('2. Enter a new task.')
        print('3. Edit the list.')
        print('4. Exit')
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
        else:
            break

if __name__ == '__main__':
    mainLoop()
