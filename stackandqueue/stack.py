def create(stack):
    print("Create a stack eg: 1 2 3 4")
    stack = [item for item in input().split(' ')]
    return stack

def push(stack):
    print("Enter a Element to add in stack")
    item = input()
    stack.append(item)
    return stack

def pop(stack):
    print(f'The element popped is {stack.pop()}')
    return stack

if __name__ == "__main__":
    stack = []
    while True:
        print('''1 - Create a stack\n2 - Push a element\n3 - Pop a element from stack\n''')

        try:
            option = int(input())

        except ValueError:
            print("Options are only Integers")

        if option == 1:
            stack = create(stack)
            operation = 'create'

        elif option == 2:
            stack = push(stack)
            operation = 'push'

        elif option == 3:
            stack = pop(stack)
            operation = 'pop'

        else:
            break

        stack_out = ' '.join(stack)
        print(f"stack {operation} operation performed and the elements are {stack_out}")
