n=int(input("Enter the no."))
print("\n::Upper triangle::")
for i in range(1,n+1):
    print(" * "*i)
print("\n::LOWER triangle::")
for i in range(n+1):
    print(" * "*(n-i))
print("\n::Pyramid triangle::")
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)
