pointer = 0
array = [["Jake",2], ["Sam",3], ["Bob",1], [None, None], [None, None]]

def add_item(array_, data):
    global pointer

    #Until we hit a null value, cycle through array
    while True:
        if array_[pointer][0] == None:
            array_[pointer][0] == data
            print("New item added at position", pointer, "containing data:", data + "!")
            break
        else:
            pass


def traverse(array_):
    global pointer

    #Until we hit a null value, cycle through array
    while True:
        if array_[pointer][0] != None:
            #Print array item name and set pointer equal to the items pointer value
            print(array_[pointer][0])
            pointer = array_[pointer][1]
        else:
            #Item is equal to null, break
            pointer = 0
            break

traverse(array)
add_item(array, "Simon")
traverse(array)