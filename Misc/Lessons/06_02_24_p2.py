cur_pointer = 0
array = [["Jake",2],[None, None],["Sam",3],["Bob",1],[None, None]]

def traverse(array_):
    if len(array_) == 0:
        return
    
    global cur_pointer
    
    while True:
        if array_[cur_pointer][1] == None:
            break
        else:
            print(array_[cur_pointer][0])
            cur_pointer = array_[cur_pointer][1]

def add_item(array_, data):
    #!
    pass


traverse(array)