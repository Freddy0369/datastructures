class queue():
    def __init__(self):
        self.top = None

    #enQueue will check if this is the first node in the stack. If it is, it will set
    #prev_ and next_ to None, else, it will set prev_ = top. Regardless, top will then be set to
    #the new node.
    
    def enQueue(self, name):
        #Get locations of nodes
        if self.top == None:
            prev_ = None
        else:
            prev_ = self.top
        
        next_ = None

        #Apply locations and name
        new_node = node(name, prev_, next_)
        self.top = new_node

    #deQueue will check if the stack is empty, if it isn't, it will store the current top,
    #and then it will set top = to top.get_prev. Finally, the old top will be returned.
    #The name of the old top is printed as well.
        
    def deQueue(self):
        #Check if stack is empty, if not deQueue as normal...
        if self.top == None:
            print("ERROR: CANNOT DEQUEUE FROM AN EMPTY STACK!")
            return(None)
        else:
            #Store old top item and set new top = to top.get_prev()
            cur_top = self.top
            self.top = self.top.get_prev()
            print(cur_top.get_name(),"was deQueued!")
            
            #Check if deQueue has emptied list and return name of new top item
            if self.top == None:
                print("STACK IS NOW EMPTY!")
            else:
                print("New top is",self.top.get_name())

            return(cur_top)
    
    #traverse will check if the stack if empty, if not,it will cycle through the stack from top to bottom.
    #It does this by creating a new temporary pointer, and setting it to the pointer. Then, it will get
    #the prev node name, until it reaches the bottom of the stack.
        
    def traverse(self):
        if self.top == None:
            print("ERROR: CANNOT TRAVERSE FROM AN EMPTY STACK!")
            return

        print("From top to bottom, the stack is as follows:")
        traverse_top = self.top
        while True:
            print(traverse_top.get_name())
            if traverse_top.get_prev() != None:
                traverse_top = traverse_top.get_prev()
            else:
                print("END")
                break

    def return_top(self):
        return self.top

class node():
    def __init__(self, new_name, new_prev, new_next):
        self.name = new_name
        self.prev = new_prev
        self.next = new_next
        print("New node named",self.name,"created!")
        
        #Check prev and next, and return them to the user
        if self.prev == None and self.next == None:
            print("prev and next are Null")
        elif self.prev != None:
            print("Prev:",self.prev.get_name())
            if self.next != None:
                print("Prev:",self.next.get_name())
        
    def get_prev(self):
        return self.prev
    
    def get_next(self):
        return self.next
    
    def get_name(self):
        return self.name

new_queue = queue()
new_queue.enQueue("Bob")
new_queue.enQueue("Sam")
new_queue.enQueue("Mike")
new_queue.deQueue()
new_queue.enQueue("Fred")
new_queue.traverse()


