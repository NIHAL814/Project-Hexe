set1 = set()
set2 = set()

n1 = int(input("Enter number of elements in set 1: "))
print("Enter elements of set 1:")
for i in range(n1):
    set1.add(input())

n2 = int(input("\nEnter number of elements in set 2: "))
print("Enter elements of set 2:")
for i in range(n2):
    set2.add(input())

print("Set 1:", set1)
print("Set 2:", set2)

print("\nUnion:", set1 | set2)
print("Intersection:", set1 & set2)
print("Set Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)
