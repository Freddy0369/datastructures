array = [5,4,7,8,2,9]
total = 0

for i in range(len(array)):
    print(array[len(array) - 1 - i])
    total += array[i]

print("Total: " + str(total))
average = total / len(array)
print("Average: " + str(average))


