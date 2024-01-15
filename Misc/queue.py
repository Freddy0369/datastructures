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
    front += 1
    rear -= 1
    return queue[rear]



en_queue("spongebob")
en_queue("spongebob")
en_queue("q")
en_queue("w")
print(queue)