#oop stacks
class item():
    def _init_(self, data_, prev_pointer_, pointer_):
        self.data = data_
        self.prev_pointer = prev_pointer_
        self.pointer = pointer_
    
    def set_prev_pointer(self, prev_pointer_):
        self.prev_pointer = prev_pointer_
    
    def set_pointer(self, pointer_):
        self.pointer = pointer_
    

class stack():
    def _init_(self):
        self.list = []
        self.pointer = 0
    
    def is_empty(self):
        if self.pointer == 0:
            return True
        else:
            return False
    
    def push(self, data):
        new_item = item._init_(data, None, None)

        if self.pointer == 0:
            new_item.set_prev_pointer = None
            new_item.set_pointer = None
        else:
            new_item.set_prev_pointer = self.pointer
            new_item.set_pointer = None
        
        self.list.append(new_item)
        pointer = len(self.list) - 1
    