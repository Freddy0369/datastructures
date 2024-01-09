class record():
    def __init__(self, newID, newLN, newFN, newDept):
        self.ID = newID
        self.lastName = newLN
        self.firstName = newFN
        self.dept = newDept

records = []
record1 = record(2468, "Jones", "John", 243)
records.append(record1) 
print(records[0].lastName)