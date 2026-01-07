n=int(input("Enter a four digit Number:"))
if n<1000:
    print(n,"is Not four digit")
elif n>9999:
    print(n,"is Not four digit")
elif 1000<=n<=9999:
    d1=(n//1000)
    d2=(n//100)%10
    d3=(n//10)%10
    d4=n%10
    s=d1+d2+d3+d4
    print("Sum of the digits =",s)
