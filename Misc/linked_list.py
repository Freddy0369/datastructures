class Node():
    def __init__(self, given_data):
        #Constructor method
        self.data = given_data
        self.next = None

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, given_next):
        self.next = given_next
    


class LinkedList():
    def __init__(self):
        #Constructor method
        self.head = None

    def traverse(self):
        #Set current node head, and run through nodes
        current = self.head

        while current != None:
            print(current.get_data())
            current = current.get_next()

    def delete(self, data):

        #Start at the head of the list
        current = self.head

        #Check if the head node is to be deleted
        if current.data == data:
            #Update the head pointer
            self.head = current.get_next()
        else:
            #Repeat until the node has been found
            while current.next.get_data() != data:
                current = current.get_next()
        
            current.set_next(current.get_next().get_next())

    
    def insert_at_front(self, data):

        #Create a new node
        new_node = Node(data)

        #Check if the head exists
        if self.head == None:
            self.head = new_node
        else:
            #Update the pointers so that the node is the head
            new_node.set_next(self.head)
            self.head = new_node

        #FINAL STATEMENT -- ORDERING LISTS
            
    def insert_in_order(self, data):
        #Create new node + start at head
        new_node = Node(data)
        current = self.head

        #Confirm order
        if current is None:
            self.head = new_node

        elif new_node.get_data() < current.get_data():
            #Set new node as head
            new_node.set_next(self.head)
            self.head = new_node
        
        #Otherwise find where the new node should be positioned
        else:
            #Repeat until the point of intersection is found
            while (current.get_next().get_data() is not None
                   and current.get_next().get_data() < new_node.get_data()):
                #Get next node
                current - current.get_next()
            
            #Update pointers on new and current nodes
            new_node.set_next(current.get_next())
            current.set_next(new_node)

my_list = LinkedList()
my_list.insert_at_front("a persons name")
my_list.insert_at_front("someone else's name")
