"""find fabonacci series for entered no"""

# def fabonacci(n):
#     if n==0:
#         fib=[0]
#     elif n==1:
#         fib=[0,1]
#     else:
#         fib=[0,1]
#         for i in range(2,n):
#             fib.append(fib[i-1]+fib[i-2])
#     print(fib)
     
# n = int(input("Enter sequence:"))
# fabonacci(n)

def fabonacci(n):
    if n==0:
        fab = [0]

    elif n ==1:
        fab = [0,1]

    else:
        fab = [0,1]
        for i in range(2,n):
            fab.append(fab[i-1]+fab[i-2])
    return fab

res = fabonacci(0)
print(res)
