n1 = input("Enter first integer:")
n2 = input("Enter second integer:")
n1 = int(n1)
n2 = int(n2)

if n1 > n2:
    print(n1, "is biggest")
elif n2 > n1:
    print(n2, "is biggest") 
else:
    print("Both are equal")