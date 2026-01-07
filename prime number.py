def is_prime(num):
    if num>1:
        for i in range(2,num):
            if num % i == 0:
                print(num,"Is Not Prime Number")
                break
        else:
            print(num,"Is Prime Number")

    else:
        print(num,"Is Not Prime Number")

num=int(input("Enter a Number:"))
result=is_prime(num)
print(result)
    
