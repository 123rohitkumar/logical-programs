#n=int(input("Enter the no of row:"))
#for i in range(1,n+1):
    #for j in range(1,i+1):
        #print(j,end="")
   # print()



#n=int(input("Enter the no of row:"))
#for i in range(1,n+1):
    #for j in range(1,i+1):
        #print(i,end="")
    #print()

#n=int(input("Enter the no of row:"))
#for row in range(n):
    #for col in range(n):
       #if col==0 or row==n-1 or row==col:
            #print("*",end="")
        #else:
            #print(end=" ")
    #print()

#n=int(input("Enter no:"))
#for row in range(n):
    #for col in range(n):
        #if row==0 or col==n-1 or row==col:
            #print("*",end="")
        #else:
           # print(end=" ")
    #print()

#n=int(input("Enter no:"))
#num=1
#for row in range(1,n+1):
    #for col in range(1,row+1):
        #print(num,end="")
        #num=num+1
    #print()

  
#for row in range(1,5):
    #for col in range(1,8):
        #if row==4 or row+col==5 or col-row==3:
            #print("*",end="")
        #else:
            #print(end=" ")
    #print()

        
#n=int(input("Enter no:"))
#for row in range(1,n+1):
    #for col in range(1,n*2):
        #if row==n or row+col==n+1 or col-row==n-1:
            #print("*",end="")
        #else:
            #print(end=" ")
    #print()

num=int(input("Enter no:"))
sum=0
for i in range(1,num):
    if (num%i) == 0:
        sum = sum + i
        
if sum==num:
    print("num is perfect number")

else:
    print("num  is not perfect number")
    






















    
        
    
