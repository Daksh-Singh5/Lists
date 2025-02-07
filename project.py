startingnum=int(input("Enter a number: "))
endingnum=int(input("Enter a number: "))
numList = []
powerList = []
#make list
for num in range(startingnum,endingnum+1):
    numList.append(startingnum)
    startingnum+=1

for i in numList:
    powerList.append(i**2)

print(powerList)