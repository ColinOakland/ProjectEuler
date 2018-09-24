listOfNumbers=[]

for x in range(0,1000):
    if x%3==0 or x%5==0:
        listOfNumbers.append(x)

print(listOfNumbers)

z=0
for y in listOfNumbers:
    z+=y

print(z)

