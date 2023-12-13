import random

outletSales = [[],[],[],[]]
total = [0,0,0,0]

#Add random data to outletSales to simulate finance
for i in range(4):
    for j in range(50):
        outletSales[i].append(random.randrange(0,50))

for quarter in range(4):
    for outlet in range(50):
        total[quarter] += outletSales[quarter][outlet]

    print("Total of quarter", str(quarter+1), str(total[quarter]))
