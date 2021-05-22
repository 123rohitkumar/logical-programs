"""Cheack whether no is armstrong or not"""

def armstrong(number):
    res = [int(x) for x in str(number)]
    print(res)
    sum=0
    for i in range(len(res)):
        sum = sum + res[i]**3
    if number == sum:
        print(str(number) + "  is armstrong no")
        
    else:
        print(str(number) + "  is not armstrong number")

armstrong(151)










        

        
        