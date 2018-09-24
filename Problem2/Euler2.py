
#computes the xth fibbinocci number
def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1;
    else:
        return fib(x-1)+fib(x-2)

#determine where the fib sequence exceeds 4 million

y=1
z=1

while y<4000000:
    y=fib(z)
    z+=1

#Accounts for numbers being too high
z=z-1
fibList=[]
for c in range(0,z):
    fibList.append(fib(c))

print(fibList)

q=0
for t in fibList:
    if t%2==0:
        q=q+t
print(q)