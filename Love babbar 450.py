#Q1)Reverse the array

#list1 = [1,2,3,4,5,6,7]
# list2=[]
# n = len(list1)
# for i in range(n):
#     list2.append(list1[n-i-1])
# print(list2)

# i = 0
#list1 = [1,2,3,4,5,6,7]
# n = len(list1)
# while n>0:
#     print(list1[n-1])
#     n = n-1

# list1.reverse()
# print(list1)

#Q2)Find the maximum and minimum element in an array

# list1 = [1000, 11, 445,1, 330, 3000]

# max = list1[0]
# min = list1[0]

# for i in list1:
#     if  max <i:
#         max = i
#     if min>i:
#         min = i

# print("max",max)
# print("min",min)

#Q3)Find the "Kth" max and min element of an array 
# Input: arr[] = {7, 10, 4, 3, 20, 15} 
# k = 3 
# k = 4
# Output: 7,10

# list1 = [7, 10, 4, 3, 20, 15]
# list1.sort()
# print(list1)
# k = 4
# for i in range(len(list1)):
#     if k ==i:
#         print(list1[i-1])

#Q4)Given an array which consists of only 0, 1 and 2.
#Sort the array without using any sorting algo
# Input: 
# N = 5
# arr[]= {0 2 1 2 0}

# Output:
# 0 0 1 2 2


#Q5)Move all the negative elements to one side of the array 
#list1= [12, 11, -13, -5, 6, -7, 5, -3, -6]
#Output: -12 -13 -5 -7 -3 -6 11 6 5

# j =0
# for i in range(len(list1)):
#     if list1[i] <0:
#         temp = list1[i]
#         list1[i]=list1[j]
#         list1[j] = temp
#         j = j+1

# print(list1)

#Q6)Find the Union and Intersection of the two sorted arrays.

#intrsection..
# A = [1, 4, 5, 3, 6], and B = [2, 3, 5, 7, 9],
# [3, 5]

# arr1 = [1, 4, 5, 3, 6]
# arr2 = [2, 3, 5, 7, 9]
# intrsection =[]

# for i in arr1:
#     if i in arr2:
#         intrsection.append(i)
# print(intrsection)
        

#union..
# arr1 = [1,2,2,3,4,5]
# arr2 = [1,2,8,2] 
# union=[]
# arr1.extend(arr2)
# for i in arr1:
#     if i not in union:
#         union.append(i)
# print(union)

#Q)7 Write a program to cyclically rotate an array by one.
#output = 5 1 2 3 4
# arr1 = [1, 2, 3, 4, 5] 
# n = len(arr1)
# x = arr1[n-1]

# for i in range(n-1,0,-1):
#     arr1[i] = arr1[i-1]

# arr1[0]=x
# print(arr1)

#Q)8find Largest sum contiguous Subarray [V.IMP]
# def Kadane(A,n):
#     max_current = max_global = A[0]
#     for i in range(1,n-2):
#         max_current = max(A[i],max_current+A[i])

#         if max_current>max_global:
#             max_global = max(max_global, max_current)
        

#     return max_global


# A= [2, 1, 5, 1, 3, 2] 
# n = len(A)
# res = Kadane(A,n)
# print(res)

#Q)9 Minimise the maximum difference between heights [V.IMP]

# def minjumps(arr,n):
#     jumps = [0 for i in range(n)]

#     if n ==0 or arr[0]==0:
#         return float('inf')

#     jumps[0] = 0

#     for i in range(1,n):
#         jumps[i] = float('inf')
#         for j in range(i):
#             if (i <= j+arr[j] and jumps[j]!= float('inf')):
#                 jumps[i] = min(jumps[i],jumps[j]+1)
#                 break
            
#     return jumps[n-1]
# #Driver Program to test above function
# arr = [1, 3, 6, 1, 0, 9]
# size = len(arr)
# res = minjumps(arr,size)
# print(res)

##########################################################################
#Q)10 find duplicate in an array of N+1 Integers

#nums = [1,3,4,2,2]
#Output: 2

# nums = [1,3,4,2,2]
# nums.sort()
# for i in range(len(nums)):
#     if nums[i]==nums[i+1]:
#         print(nums[i+1])
#         break
        
    
#Q)11  Merge 2 sorted arrays without using Extra space.

arr1 = [1,3,6,8,9]
arr2 = [4,7,9,10]

arr1.extend(arr2)
#print(arr1)

for i in range(1,len(arr1)):
    item = arr1[i]
    j = i-1

    while(j>=0 and arr1[j]>item):
        arr1[j+1] = arr1[j]
        j = j-1
    arr1[j+1] =item 
print(arr1)












 







    
    

































    











 











