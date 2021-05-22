"""creation of list object.."""
# list = []

# list = eval(input("Enter value"))
# print(type(list))

# l = list(range(0,10,2))
#print(l)

# s = "Learning python is very very easy"
# s= s.split()
#print(s)

"""Accessing element of list.."""

list = [10,20,30,40,39,39,45,67,78,89,10]
# print(list[0])
# print(list[-1])
# print(4)
# print(list[::-1])
#print(list[8:0:-1])

"""traversing the element of list.."""
i =0
n = len(list)
while i<n:
    print(list[n-1],end =" ")
    n = n-1

"""important function of list"""
# len(list)
# print(list.count(10))
# print(list.index(39))#it gives you index of first accurence

"""manipulating list..."""
# list.append("A")
# print(list)

# list.insert(1,"web")
# print(list)

# list1 = ["A","d","u"]
# list.extend(list1)
# print(list)

#list = [10,20,30,40,39,39,45,67,78,89,10]

# list.remove(10)
# print(list)

#print(list.pop())
#print(list.pop(0))

"""ordering element in list"""

# list.reverse()
# print(list)


# list.sort()------------------------------------->
# print(list1)

# list.sort(reverse=True)
# print(list)

"""Aliasing and cloning of list object"""

#list = [10,20,30,40,39,39,45,67,78,89]

#aliasing means two different reference pointing to the same object means 
# there address is same ..

# list1 = list
# print(id(list1))
# print(id(list))

#cloning means a sepeate object will create..

# list1 = list[:]

# list1 = list.copy()

# print(id(list1))
# print(id(list))


"""membership operator"""

# in 
# not in 

"""list comprehension"""

list = [10,20,30,40,39,39,45,67,78,89]
s = [x*x for x in list]
print(s)


