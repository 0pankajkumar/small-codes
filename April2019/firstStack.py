# Author Pankaj Kumar
# My first Stack on Python
myStack = []
print(f"Stack before pushing : {myStack}")

def push_on_stack(data):
    myStack.append(data)

def pop_from_stack():
    return myStack.pop()

push_on_stack(8)
push_on_stack(6)
push_on_stack(45)
push_on_stack(12)
push_on_stack(27)

print(f"Stack after pushing : {myStack}")

print("Now popping out")
print(f"Popped : {pop_from_stack()}")
print(f"Stack is now : {myStack} \n")
print(f"Popped : {pop_from_stack()}")
print(f"Stack is now : {myStack} \n")
print(f"Popped : {pop_from_stack()}")
print(f"Stack is now : {myStack} \n")
print(f"Popped : {pop_from_stack()}")
print(f"Stack is now : {myStack} \n")
print(f"Popped : {pop_from_stack()}")
print(f"Stack is now : {myStack} \n")
