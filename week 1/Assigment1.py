n=int(input("Enter the no."))
print("::Upper triangle::")
for i in range(1,n+1):
    print("*"*i)
print("::LOWER triangle::")
for i in range(n+1):
    print("*"*(n-i))
print(":Pyramid triangle::")
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)
