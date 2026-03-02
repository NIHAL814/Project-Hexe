def fact(i):
    factorial=1
    for x in range(1,i+1):
        factorial=factorial*x
    return factorial

i=int(input("Enter a Number:"))
r=fact(i)
print("factorial of",i,"=",r)
