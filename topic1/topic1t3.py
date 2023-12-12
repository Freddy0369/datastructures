outlet1Sales = [10,12,15,10]
outlet2Sales = [5,8,3,6]
outlet3Sales = [10,12,15,10]

tq = [0,0,0,0]

#Get quarters of each outlet and add them to seperate int
#contained within the tq array.
#Then print each one within the loop

#for i=0 to 3 do
#   tq[i] += outlet1Sales[i] + outlet2Sales[i] + outlet3Sales[i]
#   output("Total for quarter " + str(i+1) + " " + "tq[i]")
#next i

for i in range(4):
    tq[i] += outlet1Sales[i] + outlet2Sales[i] + outlet3Sales[i]
    print(f"Total for quarter {i+1}: {tq[i]}")