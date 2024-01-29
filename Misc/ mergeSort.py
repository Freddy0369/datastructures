l1 = [1,3,5,6,9,13]
l2 = [3,5,7,9,10,12,14]

ind1 = 0
ind2 = 0
sl = []

len1 = len(l1) - 1
len2 = len(l2) - 1

while (len1 > ind1) or (len2 > ind2):
    if l1[ind1] < l2[ind2]:
        sl.append(l1[ind1])
        ind1 += 1
    else:
        sl.append(l2[ind2])
        ind2 += 1

print(ind1)
print(ind2)

if (len1 == ind1):
    if len2 != ind2:
        for i in range(len2):
            i += ind2
            sl.append(l2[i])
else:
    for i in range(len1):
        i += ind1
        sl.append(l1[i])

print(sl)