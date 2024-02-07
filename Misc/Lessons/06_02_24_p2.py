cur_pointer = 0
maximum = 0
array = [["Jake",2],[None, None],["Sam",3],["Bob",5],[None, None], ["Mike",1]]

def traverse(array_):
    if len(array_) == 0:
        return
    
    global cur_pointer
    cur_pointer = 0
    
    while True:
        if array_[cur_pointer][1] == None:
            break
        else:
            print(array_[cur_pointer][0])
            cur_pointer = array_[cur_pointer][1]

def get_last_item_index(array_):
    if len(array_) == 0:
        return
    
    global cur_pointer
    cur_pointer = 0
    
    while True:
        if array_[cur_pointer][1] == None:
            return cur_pointer
            break
        else:
            cur_pointer = array_[cur_pointer][1]

def add_item(array_, data):
    #Traverse and find last item
    get_last_item_index(array_)

    #Set data
    array_[cur_pointer][0] = data
    #Locate a null value
    for i in range(len(array_)):
        if array_[i][1] == None:
            array_[][]
    pass


traverse(array)