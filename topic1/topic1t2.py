name = ["Freddy", "Mark", "Jack"]

def search(searchTerm):
    for i in name:
        if name[i] == searchTerm:
            return i
    
    return "Not found"

print(search(input()))