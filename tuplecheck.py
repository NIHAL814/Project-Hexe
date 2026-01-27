fruits=("mango","orange","apple","grape","banana")
x=input("Enter a fruit Name to check it contain in the tuple:").lower()
if x in fruits:
    print(x,"Present in the tuple")
else:
    print(x,"Not present")