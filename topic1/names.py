#An array is a list of one specific data type, e.g. an array of strings

names = ["George", "Xander", "Yeah", "Name", "Other name"]
i = 0
for i in range(5):
    names.append(input(str(f"Enter name [{i+1}]: ")))

for i in range(len(names)):
    print(names[i])
