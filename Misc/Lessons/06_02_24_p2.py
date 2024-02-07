cur_pointer = 0
maximum = 6
cur_size = 4
array = [["Jake",2],[None, None],["Sam",3],["Bob",5],[None, None], ["Mike",1]]

def traverse(array_):
    if len(array_) == 0:
        return
    
    global cur_pointer
    cur_pointer = 0
    
    #Print current item being pointed to, and then
    #check if it points to null, if it does then
    #end the loop, otherwise, increase the pointer
    #and loop again.
    while True:
        if array_[cur_pointer][0] == None:
            break
        else:
            #If the item is the last one, also break
            if array_[cur_pointer][1] == None:
                break

            print(array_[cur_pointer][0])
            cur_pointer = array_[cur_pointer][1]

def get_last_item_index(array_):
    #Check if empty
    if len(array_) == 0:
        return
    
    global cur_pointer
    cur_pointer = 0
    
    #Run through array until an item pointing to null is found.
    #Meaning that that item is the last in the array.
    #Then return it's position
    while True:
        if array_[cur_pointer][1] == None:
            return cur_pointer
        else:
            cur_pointer = array_[cur_pointer][1]

def find_empty_slot(array_):
    #Locate a null value by running linear searach
    for i in range(len(array_) - 1):
        if array_[i][0] == None:
            return i
    
    #If none found
    return -1

def add_item(array_, data):
    global cur_size,maximum,cur_pointer

    #Check if list is full
    if cur_size == maximum:
        print("ERROR! ARRAY IS FULL")
        return

    #Traverse and find last item
    get_last_item_index(array_)

    #Set data
    array_[cur_pointer][0] = data
    #Get null value to set pointer to
    next_pos = find_empty_slot(array_)

    #Check that it is valid
    if next_pos == -1:
        print("There are no more empty slots after this, array full!")
    else:
        array_[cur_pointer][1] = next_pos

    #Increase size
    cur_size += 1

def remove_item(array_, data):
    #Check if empty
    if len(array_) == 0:
        return
    
    global cur_pointer,cur_size
    cur_pointer = 0

    #Traverse through array until a match is found.
    #Collect it's position, as well as the previous item in the array.
    while True:

        if array_[cur_pointer][0] == data:
            break
        else:
            prev_item_position = cur_pointer
            cur_pointer = array_[cur_pointer][1]
    
    #Then, set the previous item's pointer to the item
    #after, clear the data so that it is now detected as
    #an empty slot.
    array_[prev_item_position][1] = array_[cur_pointer][1]
    array_[cur_pointer][0] = None
    array_[cur_pointer][1] = None

    #Decrease cur_size
    cur_size -= 1

#Issue with array becoming full!!!
traverse(array)
add_item(array, "Jim")
print("-------")
add_item(array, "Alex")
traverse(array)
print("-------")
add_item(array, "Jack")
traverse(array)
print("-------")
print(array)