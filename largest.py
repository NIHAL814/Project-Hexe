def large(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3
n1=int(input("Enter the first Number:"))
n2=int(input("Enter the second Number:"))
n3=int(input("Enter the third Number:"))
result=large(n1,n2,n3)
print("Largest Number is ",result)
    
