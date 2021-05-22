# # d = {"fruit name":("guava","banana","mango","papaya")}
# # print(d)
# # print(d.values())
# # print(d.keys())

# import numpy as np 

# a = np.array([1,2,3])
# print(a)

# import numpy as np

# a = np.zeros((5,5))

# print(a)

# import numpy as np

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(np.sum((a,b),axis=2))

#import numpy as np

# a = np.array([12,43,2,100,54,5,68])
# print(a)
# print(np.argsort(a))
# print(a[np.argsort(a)[-2:]])  


# import pandas as pd 

# l1 = [[1,2,3,4,5,6,7],[4,5,6,7,89]]
# data = pd.DataFrame(l1)
# print(data)

# import pandas as pd 

# dic1 = {'fruit name':['apple','papaya','banana','gauva'],'count':[1,2,3,4]}

# data = pd.DataFrame(dic1)
# print(data)

#import pandas as pd

# x = lambda a: a+10

# print(x(5))

# import copy

# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.copy(old_list)


# print("Before....................")
# print()
# print("Old list:", old_list,print(id(old_list)))
# print("New list:", new_list,print(id(new_list)))

# old_list.append([4, 4, 4])

# print("after....................")
# print()

# print("Old list:", old_list,print(id(old_list)))
# print("New list:", new_list,print(id(new_list)))

# import copy

# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_list = copy.copy(old_list)

# print("Old list:", id(old_list))
# print("New list:", id(new_list))


def decor(func):
    def inner(name):
        if name == 'nitish':
            print("Hello nitish good morning..")
        else:
            func(name)
    



@decor
def wish(name):
    print("Hello",name, "GOOD morning:")


wish("rohit")
wish("nitish")









