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

my_list = LinkedList()

