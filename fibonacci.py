k=int(input())
i=1
#initializations
a=0
b=1
print("the fibonaccci series upto the given number k is \n")
print(a)
print(b)
c=0
#running the loop
while(i<=k-2):
    c=a+b
    a=b
    b=c
    print(c)
    i=i+1
