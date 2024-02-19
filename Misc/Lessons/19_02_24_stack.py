#DEFs and VARs
def push_(stack_, data):
    global top
    top += 1
    stack_.append(data)

def pop_(stack_):
    global top
    stack_.pop(top)
    top -= 1

def is_empty(stack_):
    global top
    if top == 0:
        return True
    else:
        return False
#START
    
top = -1
stack = []

push_(stack, "Mondeo")
push_(stack, "Golf")
is_empty(stack)
push_(stack, "Fiesta")
push_(stack, "Punto")
pop_(stack)
push_(stack, "Civic")
push_(stack, "Porsche")
#is full
pop_(stack)
pop_(stack)
print(stack)
print(top)