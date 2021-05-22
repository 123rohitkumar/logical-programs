# 1 Python program to add two numbers

# def sum(a,b):
#     res = a+b
#     print(res)

# sum(2,5)
#==========================================================================
# 2 Maximum of two numbers in Python

# def max(a,b):
#     if a>b:
#         print(a ,"is greter then:", b)
#     else:
#         print(b,"is greater then:",a)

# max(2,-5)
#============================================================================
# 3 Python Program for factorial of a number

# def fact(num):
    
#     sum=1
#     i=0
#     if num<0:
#         return 0
#     elif num==0 or num==1:


#         return 1
#     else:
#         while num>i:
#             sum = sum*num
#             num = num-1
#         return sum

# val= fact(5)
# print(val)


# def func(n):
#     if n<0:
#         return 0
#     elif n==0 or n==1:
#         return 1
#     else:
#         return n*func(n-1)

# val = func(5)
# print(val)
#============================================================================
#count the no of duplicate elements in list;

#Input--> L=[1, 2, 3, 4, 2, 7, 8, 8, 3]
#output--> 3

# def main():
#     pass

# def countduplicate(numbers):
#     size = len(numbers)
#     count =0
#     for i in range(size):
#         for j in range(i+1,size):
#             if numbers[i] == numbers[j]:
#                 count = count+1
#             #else:
#                 #continue
#     return count
                
# val=countduplicate([1, 2, 3, 4, 2, 7, 8, 8, 3])
# print(val)

# if __name__ == '__main__':
#     main()

d = {}
count = 0
for i in list1:
    value = list1.count(i)
    d[i] = value
print(d.items())

for key,value in d.items():
    if value>1:
        count = count+1
print(count)

#=================================================================================
#Python Program to check Armstrong Number


# def Armstrong(n):
#     c=0
#     temp =n
#     while(n>0):
#         a = n%10#remainder
#         n = n//10#quotient
#         c = c+(a*a*a)
#     #print(c)
#     if temp == c:
#         print(temp, "is an armstrong number:")
#     else:
#         print(temp,"not an armstrong:")
    

# n = int(input("Enter number:"))
# Armstrong(n)

#======================================================================================
# Python program to print all prime no in an interval ,number should be greater than 1
# start = 11
# end = 25
# prime = []

# for i in range(start,end):
#     for j in range(2,i):
#         #print(j)
#        if i%j == 0:
#             break#if break will execute else won't execute 
#     else:        #and flow diectly go to outer loop and increment of ouetr will happen.
#         print(i)
#=========================================================================================
#Python program to check whether a number is Prime or not


# def prime(num):
#     for i in range(2,num):
#         if num%i == 0:
#             print(num,"no is not prime:")
#             break
#         else:
#             print(num,"no is prime:")
#             break


# num = int(input("Enter number:"))
# prime(num)
#========================================================================================
#Python Program for n-th Fibonacci number

# def Fibonacci(n):
#     a=0
#     b=1
#     if n<0:
#         print("incorrect output:")
#     elif n==0:
#         print(a)
         
#     elif n==1:
#         print(a,b)
#     else:
#         fab = [a,b]
#         for i in range(2,n):
#             c = a+b
#             a=b
#             b=c
#             fab.append(c)
#         print(fab)
        

# Fibonacci(9)

#===============================================================================
#Python Program to find sum of array

# def sum_array(arr):
#     sum= 0
#     for i in arr:
#         sum = sum+i
#     return sum

# val=sum_array([2,3,4,5])
# print(val)
#===============================================================================

#Python Program to find largest element in an array

# def find_max(arr,n):
#     max = arr[0]

#     for i in range(1,n):
#         if arr[i]>max:
#             max = arr[i]
#     return max


# a = [1,4,2,8,9,0,23,56,7]
# n = len(a)
# val =find_max([1,4,2,8,9,0,23,56,7],n)
# print(val)

arr1 = [1,4,2,8,9,0,23,56,7]
n = len(arr1)

max = arr1[0]
min = arr1[0]
for i in arr1:
    if i>max:
        max = i
    if i<min:
        min = i
print(max)
print(min)

#====================================================================================
#Python Program to Split the array and add the first part to the end
# Input : arr[] = {12, 10, 5, 6, 52, 36}
#             k = 2
# Output : arr[] = {5, 6, 52, 36, 12, 10}

# def splitArray(arr,k,n):
#     asplit = split(2,n)
#     print(asplit)



# arr=[12, 10, 5, 6, 52, 36]
# a = len(arr) 
# b=2
# splitArray([12, 10, 5, 6, 52, 36],b,a)
#=====================================================================================
# How to define an array

# from array import *
# val = array('i',[2,3,5,6])
# print(val)
# print(val.buffer_info())
#=====================================
# how to print an array
# from array import *
# val = array('i',[2,3,4,5,6,7])
# for i in range(len(val)):
#     print(val[i],end=' ')
#=======================================
#how to crate new array by using old array
# from array import *
# val = array('i',[2,3,4,5,6,7])
# new_array = array(val.typecode,(a*a for a in val))
# for i in new_array:
#     print(i,end =' ')
#=========================================
#take an input from user and print it by using array
# from array import *
# val = array('i',[])
# n = int(input("Enter the size of an array:"))
# for i in range(n):
#     x = int(input("Enter the next value:"))
#     val.append(x)

# print("ye dekho niche mara array")
# for i in range(n):
#     print(val[i],end =',')
#============================================================================================interview
#reverse a string using for loop
# def reverse(s): 
#   str = "" 
#   for i in s: 
#     str = i + str
#   return str
  
# s = "Geeks"
  
# print ("The original string  is : ",end="") 
# print (s) 
  
# print ("The reversed string(using loops) is : ",end="") 
# print (reverse(s)) 

#reverse a string using for loop

str1 = "rohit"
str2 = ""
for i in range(len(str1)):
    str2 = "".join(str1[i]) + str2

print(str2)


#====================================================================
# remove first repetative element from list and keep the rest as same.
#input = [2, 3, 4, 5, 3, 6, 4, 1]
#first repetion is 3
#[2, 3, 4, 5, 6, 4, 1]

# def firstdup(input):
#     first_dup = None
#     for i in input:
#         if input.count(i)>1:
#             first_dup = i
#             print("first dup is:",first_dup)
#             input.remove(first_dup)
#             break
#     return input

# #input = [2, 3, 4, 5, 3, 6, 4, 1]
# input = list("abcabcdef")
# res = firstdup(input)
# resstr = "".join(res)
# print(str(resstr))
            
#####################################################################

# def find_dup(rohit):
#     seen = set()
#     it = iter(lst)
     

#     for item in it:
#         if item not in seen:
#             seen.add(item)
#     return seen

# lst = [2, 3, 4, 5, 3, 6, 4, 1]
# res=list(find_dup(lst))
# print(res)

###########################################################################
# remove first repetative element from list and keep the rest as same.
#input = [2, 3, 4, 5, 3, 6, 4, 1]
#first repetion is 3
#[2, 3, 4, 5, 6, 4, 1]

# def first_dup(list):
#     #len = len(list)
#     for ele in list:
#         if list.count(ele)>1:
#             list.remove(ele)
#             break
#     return list

# input = [2, 3, 4, 5, 3, 6, 4, 1]
# res = first_dup(input)
# print(res)

##############################################################################
#remove all duplicate element from list..

# def remove_dup(list):
#     s = set()

#     for i in list:
#         if i not in s:
#             s.add(i)
#     return s

# input = [2, 3, 4, 5, 3, 6, 4, 1]
# res = list(remove_dup(input))
# print(res)
##############################################################################
#reverse a string using for loop

# def reverse(input):
#     s =""
#     for i in input:
#         s = i+s
#     return s

# input = "rohit"
# res = reverse(input)
# print(res)
##############################################################################
#Python Program to Split the array and add the first part to the end
# Input : arr[] = {12, 10, 5, 6, 52, 36}
#             k = 2
# Output : arr[] = {5, 6, 52, 36, 12, 10}

# def split_array(input,l,k):
#     for i in range(k,l):
#         remain.append(input[i])

#     for i in range(0,k):
#         remain.append(input[i])
#     return remain

# input = [12, 10, 5, 6, 52, 36]
# remain = []
# k = 2
# l = len(input)
# res = split_array(input,l,k)
# print(res)

###################################################################################
#Python Program for n-th Fibonacci number

# def fabonaci(n):
#     a = 0
#     b = 1
    
#     if n<0:
#         print("incorrect input:")
#     elif n==0:
#         return a
#     elif n ==1:
#         return a,b

#     else:
#         fab =[a,b]
#         for i in range(2,n):
#             c = a+b
#             a = b
#             b = c
#             fab.append(c)

#         return fab
        
# res = fabonaci(8)   
# print(res)

########################################################################
#find the extra element in array..

# arr1 = [1,2,3,4,5,6,7]
# arr2 = [1,2,3,4,5,6,7,8]
##########################################################################

# def find_max(arr,n):
#     max = 0
#     for i in range(n):
#         if arr[i]>max:
#             max = arr[i]
#     return max

# arr = [10, 324, 45, 90, 9808] 
# n = len(arr)
# res = find_max(arr,n)
# print(res)

############################################################################
#Find remainder of array multiplication divided by n
# Input : arr[] = {100, 10, 5, 25, 35, 14}, 
#             n = 11
# Output : 9
# 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9

# def calculation(input,n):
#     mul = 1
#     for i in range(len(input)):
#         mul *= (input[i])
#         res = mul % n
#     return res

# input = [100, 10, 5, 25, 35, 14]
# n = 11
# cal = calculation(input,n)
# print(cal)

##############################################################################
# Python program to interchange first and last elements in a list..
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]


# def change(arr,n):
#     temp = arr[n-1]
#     arr[n-1] = arr[0]
#     arr[0] = temp
#     return arr

# Input = [12, 35, 9, 56, 24]
# n = len(Input)
# res = change(Input,n)
# list(res)
# for  i in res:
#     print(i)

#################################################################################
# Python3 program to swap elements 
# at given positions 
# input  = [1,2,3,4,5] pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]

# def swap(list,pos1,pos2):
#     list[pos1], list[pos2] = list[pos2], list[pos1]
#     return list



# list  = [1,2,3,4,5]
# pos1 = 2
# pos2 = 5
# res = swap(list,pos1-1,pos2-1)
# print(res)
############################################################################
#reverse a list 
#lst = [10, 11, 12, 13, 14, 15] 
# print(lst[::-1])
#lst.reverse()
#print(lst)
# for i in range(n):
# print(lst[n-1-i])

# lst = [10, 11, 12, 13, 14, 15] 
# n = len(lst)-1
# while n>0:
#     print(lst[n])
#     n = n-1
###############################################################################
# Python program to find sum of elements in list
#list1 = [11, 5, 17, 18, 23]

# def sum(list1):
#     sum=0
#     for i in range(len(list1)):
#         sum = sum + list1[i] 
#     return sum
# list1 = [11, 5, 17, 18, 23]
# res = sum(list1)
# print(res)

# def sum(list1,n):
#     sum = 0
#     while n>=0:
#         sum = sum + list1[n]
#         n = n-1
#     return sum

# list1 = [11, 5, 17, 18, 23]
# n= len(list1)-1
# res = sum(list1,n)
# print(res)
###################################################################
# def min(list1):
#     min = list1[0]
#     for i in list1:
#         if i<min:
#             min = i
#     return min

# list1 = [11, 5, 17, 18, 23]
# val = min(list1)
# print(val)

###################################################################

# def max(list1):
#     max = list1[0]
#     for i in list1:
#         if i>max:
#             max = i
#     return max

# list1 = [11, 5, 17, 18, 23]
# val = max(list1)
# print(val)

######################################################################
#list1 = [11, 5, 17, 18, 23]
# list1.sort()
# print(list1[:1])
####################################################################
#find the second largest no in list

# list1 = [10,20,4,45,99]
# n = len(list1)
# mx = max(list1[0],list1[1])
# secondmax = min(list1[0],list1[1])

# for i in range(2,n):
#     if list1[i]>mx:
#         secondmax = mx
#         mx = list1[i]
    
#     elif list1[i]>secondmax and mx != list1[i]:
#         secondmax = list1[i]

# print("Second highest number is:",secondmax)
#######################################################################
#Python program to find N largest elements from a list

# Input : [81, 52, 45, 10, 3, 2, 96] 
#         N = 3
# Output : [81, 96, 52]

# def Nmax(list1,n):
    
#     Nlist=[]
#     for i in range(n):
#         max = 0
#         for j in range(len(list1)):
#             if list1[j] > max:
#                 max = list1[j]

#         list1.remove(max)        
#         Nlist.append(max)

#     print(Nlist)   


# list1 = [81, 52, 45, 10, 3, 2, 96]
# n = 3
# Nmax(list1,n)
##########################################################################
# list1 = [81, 52, 45, 10, 3, 2, 96]

# list1 = [elem for elem in list1 if elem%2 != 0  ]
# print(list1)
#####################################################################
#Count occurrences of an element in a list
# Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# n = 10
# Output : 3

# def count(list1,n):
#     count =0
#     for i in list1:
#         if n == i:
#             count = count+1
#     return count


# list1 = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# n = 10
# res = count(list1,n)
# print(res)
################################################################

# list1 = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# res = list1.count(10)
# print(res)
#################################################################
# from collections import  Counter
# list1 = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# x = 10
# d = Counter(list1)
# print(d)
# print('{} has occured {} times'.format(x,d[x]))
##########################################################
#Remove empty tuples from a list

# Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
#                   ('krishna', 'akbar', '45'), ('',''),()]
                  
# Output : [('ram', '15', '8'), ('laxman', 'sita'), 
#           ('krishna', 'akbar', '45'), ('', '')]

# def Rempty(tuples):
#     for i in tuples:
#         if len(i)==0:
#             tuples.remove(i)
#     print(tuples) 


# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
#                    ('krishna', 'akbar', '45'), ('',''),()]

# res = Rempty(tuples)
# print(res)

########################################################################
#Program to print duplicates from a list of integers
# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]

# def duplicate(list1):
#     output = []
#     for i in list1:
#         if list1.count(i)>1:
#             list1.remove(i)
#             if i not in output:
#                 output.append(i)
            

#     print(output)

# list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# res = duplicate(list1)
# print(res)
#####################
d ={}
list2 =[]
for i in list1:
    d[i]= list1.count(i)

for key,value in d.items():
    if value>1:
        list2.append(key)
print(list2)
#####################################################################
#find Cumulative sum of a list
# Input : list1 = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]


# def CumulativeSum(list1):
#     new_list = []
#     sum = 0
#     for i in range(len(list1)):
#         sum = sum + list1[i]
#         new_list.append(sum)
#     return new_list

# list1 = [10, 20, 30, 40, 50]
# res = CumulativeSum(list1)
# print(res)
############################################################################
#Sum of number digits in List
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
list1 = [12, 67, 98, 34]
print("original list is :",list1)

res = []

for i in list1:
    sum = 0
    for j in str(i):
        sum = sum +int(j)
    res.append(sum)
print("List Integer Summation:",res)

###################################################31-01-2021^^^
#Break a list into chunks of size N in Python

# Input:-
# my_list = ['geeks', 'for', 'geeks', 'like', 
#            'geeky','nerdy', 'geek', 'love', 
#                'questions','words', 'life'] 

# # Output:-
# # [['geeks', 'for', 'geeks', 'like', 'geeky'], 
# #  ['nerdy', 'geek', 'love', 'questions', 'words'], 
# #  ['life']]


# def chunks(my_list,n):
#     for i in range(0,len(my_list),n):
#         yield my_list[i:i+n]
        


# n = 5  
# res = list(chunks(my_list,n))
# print(res)
####################################################################
#program to check if a string is palindrome or not

# Input : malayalam
# Output : Yes

def palindrome(value,n):
    res =""
    #res = value[::-1]
    for i in range(n):
        #res = res + value[n-i-1]
        res = value[i]+res
    if value == res:
        print(res,":given string is palindrom..")
    else:
        print(res,":given string is not palindrom..")

#value = "malayalam"
value = "rohit"
n = len(value)
palindrome(value,n)
 
#################################################################################
#reverse words in a given string in python.

# Input : str = geeks quiz practice code
# Output : str = code practice quiz geeks

# str1 = "geeks quiz practice code"

# str2 = str1.split(' ')
# n = len(str2)
# res =[]
# for i in range(n):
#     res.append(str2[n-i-1])
# print(res)

##############################################################################
#remove i’th character from string in Python

# def removeith(str1,n):
#     str2 = ""
#     for i in range(len(str1)):
#         if n != i:
#             str2 = str2 + str1[i]
#     print(str2)

# str1 = "algorithms"
# n = 2
# removeith(str1,n)

def removeith(str1,n):
    for i in range(len(str1)):
        if n ==i:
            str2 = str1.replace(str1[i],'')
    return str2

str1 = "algorithm"
n = 2
res = removeith(str1,n)
print(res)

##########################################################################
#Check if a Substring is Present in a Given String

# str1 = "this is for checking purpose"
# str2 = str1.split(' ')
# sub = "checking"

# def findsub(str1):
#     for i in range(len(str2)):
#         if sub == str2[i]:
#             print("mathced substring is:",str2[i])
#             break
# findsub(str1)

str1 = "this is for checking purpose"
sub = "checking"

for i in str1.split():
    if sub == i:
        print("Sub is present in string.. ",sub)
####################################################################
# Words Frequency in String Shorthands
# Input : test_str = "Gfg Gfg Gfg"
# Output : {‘Gfg’: 3}

str1 = "Gfg is good Gfg good Gfg bad"
str2 = str1.split()
dict1= {}
for key in str2:
    dict1[key] = str2.count(key)
print(dict1)

#####################################################################
#Convert Snake case to Pascal case
# Input : geeks_for_geeks
# Output : GeeksforGeeks

# str1 = "geeks_for_geeks"
# print(str1.replace("_",""))
#####################################################################
#program to print even length words in a string
# Input: s = "This is a python language slect only even words"
# Output: This
#         is
#         python
#         language 

s = "This is a python language slect only even words"
s = s.split()
for i in s:
    if len(i) % 2 != 0:
        s.remove(i)
print(s)
##################################
def evenword(str1):
    str1 = str1.split()
    str2 = []
    for i in str1:
        if len(i)%2==0:
            str2.append(i)
    return str2

res =  evenword("This is a python language slect only even words")
res = ' '.join(res)
print(res)

###################################################################
#Program to accept the strings which contains all vowels
# Input : geeksforgeeks
# Output : Not Accepted
# All vowels except 'o' are not present

# Input : ABeeIghiObhkUul
# Output : Accepted
# All vowels are present

def acceptOnlyVowel(str1):
    str1 = str1.lower()
    str2 = "aeiou"
    str3 = ""
    for i in str2:
        if i in str1:
            str3 = str3+i
    if str3 == str2:
        print("Accepted .. All vowel are present:",str3)
    else:
        print("only",str3,"is matching:")
        
if __name__ == "__main__" : 
      
    str1 = "SEEquoiaL"
    acceptOnlyVowel(str1)
#####################################################################
#Count the Number of matching characters in a pair of string

Input : str1 = 'abcdef'
        str2 = 'defghiaa'
Output : 4 
(i.e. matching characters :- a, d, e, f)

def matchcount(str1,str2):
    count = 0
    for i in str1:
        if i in str2 and str2.find(i):
            count +=1
    return count

str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'
res = matchcount(str1,str2)
print(res)

###################################################################
#Least Frequent Character in String
# The original string is : GeeksforGeeks
# The minimum of all characters in GeeksforGeeks is : f

def minFcount(str1):
    dict1 = {}
    for i in str1:
        dict1[i] = str1.count(i)
    return dict1

str1 = "GeeksforGeeks"
res = minFcount(str1)
print(res)
#res = min(res,key= res.get)
res = max(res,key= res.get)
print(res)

#####################################################################----28-01-2021^^
#check if a string contains any special character..
# Input : Geeks$For$Geeks
# Output : String is not accepted.

# import re

# def check(str1):
#     regex = re.compile("[@_!#$%^&*()<>?/|}{~:]")
#     if(regex.search(str1)==None):
#         print("String is accepted:")

#     else:
#         print("String not accepted.")

# str1 = "Geeks$For$Geeks"
# res = check(str1)
#############################################################
# words which are greater than given length k

# Input : str = "hello geeks for geeks 
#           is computer science portal" 
# k = 4
# Output : hello geeks geeks computer 
#          science portal

# def eliminate(str1,k):
#     str1 = str1.split(' ')
#     for i in str1:
#         if len(i)<k:
#             str1.remove(i)
#     return str1
# str1 = "hello geeks for geeks is computer science portal"
# k = 4
# res =eliminate(str1,k) 
# print(' '.join(res)) 
############################################################################
# x = {"rohit":1,"kumar":5}
# #d={}
# # d.update(x)
# # print(d)
# # print(sum(d.values()))
# s = x.values()
# squares = {x:x*x for x in s}
# print(squares)

#######################################################33
# s = lambda n:n*n 
# print(s(4))

# def iseven(x):
#     if x%2 == 0:
#         return True
#     else:
#         False

# l=[0,1,2,3,4,5,6,7,8]
# l1 = list(filter(iseven,l))
# print(l1)

# l=[0,1,2,3,4,5,6,7,8]
# l1 = list(filter(lambda n:n%2==0,l))
# print(l1)

#l=[0,1,2,3,4,5,6,7,8]
# l1 = list(map(lambda n: n*2,l))
# print(l1)

# from functools import *
# result = reduce(lambda x,y:x+y,l)
# print(result)
###############################################################################

# def decor(func):
#     def inner(name):
#         if name == "aman":
#             print("hello",name,"good evening:")
#         else:
#             func(name)
#     return inner

# @decor
# def wish(name):
#     print('hello',name,"good morning:")

# wish("rohit")
# wish("aman")
#############################################################################
# def countdown(num):
#     print("start countdown:")
#     while(num>0):
#         yield num
#         num = num-1

# res = countdown(5)
# for i in res:
#     print(i)
#############################################################################
# print('stmt-1')
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)
# print('stmt-2')
#############################################################################
# from threading import*
# import time

# def display():
#     for i in range(5):
#         print("Sheeta thread:")
#         time.sleep(2)

# t = Thread(target=display)
# t.start()
# t.join()
# for i in range(5):
#     print("rama thread:")

#############################################################################
# from threading import *
# import time
# l = Lock()
# def wish(name):
#     l.acquire()
#     for i in range(5):
#         print(name,"good morning")
#         time.sleep(2)
#     l.release()

# t1 = Thread(target = wish,args = ("dhoni",))
# t2 = Thread(target = wish,args = ("rohit",))
# t1.start()
# t2.start()
########################################################

# def Check_Sum(input,sum):
#     res = []
#     for i in range(len(input)):
#         for j in range(i):
#             if sum == input[i] + input[j]:
#                 res.append(input[i])
#                 res.append(input[j])
#     return res 

# res = [0,-1,2,-3,1]
# sum = -2
# output = Check_Sum(res,sum)
# print("out put is:",output)
#####################################################3

# def reverse_word(str1):
#     res = []
#     arr1 = str1.split()
#     for i in arr1:
#         res.append(i[::-1])
#     return res
        
# output = reverse_word("rohit kumar")
# print("output of reverse word:",output)
######################################################
# str1 = "gEeks for geeks "
# str2 = ""
# d = {}
# for i in str1.split():
#     str2 +=i
# str2=str2.lower()
# str2 = list(str2)

# str2 = "geeksforgeeks"
# str2 =list(str2)
# str3=""
# value = 0
# d={}
# for i in str2:
#     d[i] = value+str2.count(i)

# print(d)
# max1 = max(d,key = d.get)
# print(max1)

# for i in str2:
#     if i!=max1:
#         str3 +=i
# print(str3)

























































































































        
            


















 













































            


















 




    










