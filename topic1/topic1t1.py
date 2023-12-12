# declare array - array numbers[5]

numbers = [5,4,7,8,2,9]
total = 0

#for i=0 to (numbers.length-1) do
# output(numbers[numbers.length-1] - i)
# total += numbers[i]
#next i

for i in range(len(numbers)):
    print(numbers[len(numbers) - 1 - i])
    total += numbers[i]

print("Total: " + str(total))
average = total / len(numbers)
print("Average: " + str(average))


