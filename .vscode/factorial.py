"""Find facroial of Entered number"""

#n=int(input("Enter number:"))
#fact=0
#for i in range(n,0,-1):
    #fact = fact + n*n-1
#print(fact)



def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)


n =int(input("Enter number"))
result =fact(n)
print(result)

