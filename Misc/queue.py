queue = ["", "", ""]
front = 0
rear = -1
size = 0
max_size = len(queue)

def en_queue(new):
    #If rear is max, reset, rear acts as the pointer
    #Change all variables accordingly

    global size, max_size, front, rear

    if rear == max_size - 1:
        rear = 0
    else:
        rear += 1
    
    queue[rear] = new
    size = size + 1

def de_queue():
    global size, max_size, front, rear

    if is_empty() == True:
        return "Queue is empty!"

    front += 1
    if rear == max_size - 1:
        rear = 0
        return queue[max_size - 1]
    else:
        rear += 1
        return queue[rear - 1]


def is_full():
    if rear == max_size - 1:
        return True
    else:
        return False
    
def is_empty():
    if rear == -1:
        return True
    else:
        return False
    



en_queue("spongebob")
en_queue("spongebob")
print(de_queue())
en_queue("q")
print(queue)
en_queue("w")
en_queue("spongebob")
print(de_queue())
print(queue)