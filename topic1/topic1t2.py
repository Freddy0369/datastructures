name = ["Freddy", 123, "Mark", 153, "Jack", 765]

def search(searchTerm):
    for i in range(len(name)):
        if str(name[i]) == searchTerm:
            return str(name[i+1])
    
    return "Not found"

print(search(input()))