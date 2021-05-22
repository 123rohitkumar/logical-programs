# def testgen(index):
#     weekdays = ['sun','mon','tue','wed','thu','fri','sat']
#     yield weekdays[index]
#     yield weekdays[index+1]


# day = testgen(0)
# print(next(day))
# print(next(day))
#----------------------------------------------------
# def countdown(value):
#     while value>0:
#         yield value
#         value = value-1

# count = countdown(5)
# for each in count:
#     print(each)
#-----------------------------------------------------

# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         #a,b = b,a+b
#         a=b
#         b=a+b

# for f in fib():
#     if f>100:
#         break
#     print(f)

#------------------------------------------------------------

# weekdays = ['sun','mon','tue','wed','thu','fri','sat']
# listAsString = ' '.join(weekdays)
# print(listAsString)
#----------------------------------------------------------------

# def listtostring(s):
#     str =" "

#     for each in s:
#         string = str+each
#         print(string)

# s = ['Geeks', 'for', 'Geeks'] 
# value = listtostring(s)

#----------------------------------------------------------------
# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20

#     def m1(self):
#         self.c= 30

# t = Test()
# t.m1()
# print(t.__dict__)

#-------------------------------------------------------------------
# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20

#     def m1(self):
#         self.c= 30

# t = Test()
# t.d=40
# print(t.__dict__)
#--------------------------------------------------------------------
# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20

#     def talk(self):
#         del self.a

# t = Test()
# print(t.__dict__)
# t.talk()
# print(t.__dict__)

#--------------------------------------------------------------------
# class Test:
#     def __init__(self):
#         self.a=5
#         self.b=10
#         self.c=20
#         self.d=30
#         self.d=40

# t1= Test()
# t2= Test()
# print(t1.__dict__)
# print(t2.__dict__)
# del t1.a 
# print(t1.__dict__)
# print(t2.__dict__)

# #----------------------------------------------------------
# # class Test:
# #     x = 10
# #     def __init__(self):
# #         self.a=20
# #         self.b=30

# # t1 = Test()
# # t2 = Test()

# # print(Test.x)
# # print(t1.x)
# # print(t2.x)
# #--------------------------------------------------------
# class Test:
#     a=10#inside class

#     def __init__(self):#inside constructor
#         self.b=20

#     def m1(self):#inside instance method
#         self.c=30

#     @staticmethod#inside static method
#     def m2():
#         d=40

#     @classmethod#inside class method
#     def m3(cls):
#         cls.e= 50
#         Test.f=60

# t T
# print(Test.__dict__)

#-------------------------------------------

#how to access static variable
# class Test:
#     a= 10
#     def __init__(self):
#         print(self.a)
#         print(Test.a)
    
#     def m1(self):
#         print("instance method")
#         print(self.a)
#         print(Test.a)

#     @staticmethod
#     def m2():
#         print("static method")
#         print(Test.a)

#     @classmethod
#     def m3(cls):
#         print("class method")
#         print(cls.a)
#         print(Test.a)

# t = Test()
# print("ouside from class",t.a)
# t.m1()
# t.m2()
# t.m3()
#---------------------------------------------------
# class Test:
#     a=10
#     def __init__(self):
#         self.b=20

#     @classmethod
#     def m1(cls):
#         cls.a = 888
#         cls.b = 999

# t1 = Test()
# t2 = Test()
# t1.m1()
# print(t1.a,t1.b)
# print(t2.a,t2.b)
#-------------------------------------------------
#create student class with name and marks using instance method and
#takes input from user 

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def display(self):
#         print("Hi",self.name)
#         print("your marks are:",self.marks)

#     def grade(self):
#         if self.marks >=60:
#             print(self.name," got first division:")
#         elif self.marks>=50:
#             print(self.name," is second division")
#         elif self.marks>=35:
#             print(self.name," is third  divison")
#         else:
#             print(self.name," failed:")

# n = int(input("Enter the no of student:"))
# for i in range(n):
#     name = input("Enter the name:")
#     marks = int(input("Enter the marks"))
#     s = Student(name,marks)
#     s.display()
#     s.grade()
#     print()
#---------------------------------------------------------------------
# class Student:
#     def setName(self,name):
#         self.name=name
    
#     def getName(self):
#         return self.name
    
#     def setMarks(self,marks):
#         self.marks = marks

#     def getMarks(self):
#         return self.marks

# n = int(input("Enter no of student:"))
# for i in range(n):
#     s = Student()
#     name = input("Enter name:")
#     s.setName(name)
#     marks = int(input("Enter marks:"))
#     s.setMarks(marks)

#     print("Hi",s.getName())
#     print("Your marks is:",s.getMarks())
#     print()

#----------------------------------------------------------

# class Animal:
#     legs =4
    
#     @classmethod
#     def walk(cls,name):
#         print("{} wlaks with {}legs".format(name,cls.legs))

# a = Animal()
# a.walk("Dog")
#==================================================================
#pass one class object to another class as an argument..

# class Employee:
#     def __init__(self,ename,eno,esal):
#         self.ename = ename
#         self.eno = eno
#         self.esal = esal

#     def display(self):
#         print("Employee name",self.ename)
#         print("Employee eno",self.eno)
#         print("Employee esal",self.esal)

# class Test:

#     def modify(emp):
#         emp.esal = emp.esal+1000
#         emp.display()

# e = Employee("rohit",2,100000)
# Test.modify(e)
#==========================================================================
# class Outer:
#     def m1(self):
#         print("outer class:")
    
#     class Inner:
#         def m2(self):
#             print("Inner class:")

# o = Outer()
# o.m1()
# i = o.Inner()
# i.m2()

#===============================================================================
# class Outer:
#     def m1(self):
#         print("class outer")
    
#     class Inner:
#         def m2(self):
#             print("class Inner")
# o = Outer()
# o.m1()
# #o.Inner().m2()
# #i = o.Inner().m2()
# i = o.Inner()
# i.m2()
# Outer().Inner().m2()


# class Person:
#     def __init__(self):
#         self.name = "rohit"
#         self.db = self.Dob()
    
#     def display(self):
#         print("Name:",self.name)
    
#     class Dob:
#         def __init__(self):
#             self.dd = 23
#             self.mm = 8
#             self.yy = 2019

#         def display(self):
#             print("{}/{}/{}".format(self.dd,self.mm,self.yy))

# p = Person()
# p.display()
# p.db.display()
#========================================================================
# import time
# class Test:
#     def __init__(self):
#         print("constructor ececution...")

#     def __del__(self):
#         print("performing last activities:")

# t1=Test()
# t1 =None
# time.sleep(5)
# print("end of application...")
#===========================================================================
#has-a relationship .
# when we want to add all features or functionality of other class into our class we will go
# for has a relation ship it is different from ineer class concept because we create a separaete
# class for specific functionality an and we can use that functionality into multiple class just
#  using the object referecnce of that class.

# class Car:
#     def __init__(self,name,model,color):
#         self.name = name
#         self.model = model
#         self.color = color

#     def getinfo(self):
#         print("car name:{},car model: {},car color:{}".format(self.name,self.model,self.color))


# class Employee:
#     def __init__(self,ename,esal,car):
#         self.ename= ename
#         self.esal =esal
#         self.car = car

#     def display(self):
#         print("emp name:{},emp sal:{}".format(self.ename,self.esal))
#         self.car.getinfo() 

# c = Car("indica","c4","Red")
# e = Employee("rohit",12345678,c)
# e.display()
#================================================================================
# class X:
#     a= 10
#     def __init__(self):
#         self.name = "rohit"
#         self.sal = 1034473264387
#         print("parent constructor.........")

#     def m1(self):
#         print("parent class instance method",self.name,self.sal)
    
#     @classmethod
#     def m2(cls):
#         print("parent class class method:")

#     @staticmethod
#     def m3():
#         print("parent class static method:")


# class Y(X):
#     a= 234
    
#     def __init__(self):
#         super().__init__()
#         print(super().a)
#         print("child class constructior:")

# y = Y()
# y.m1()
# y.m2()
# y.m3()
# print(y.a)

#======================================================================
# class Person:
#     def __init__(self,name,sal):
#         self.name = name
#         self.sal = sal
    
#     def eatdrink(self):
#         print("eating biryani and drinking beer:")

# class SE(Person):
#     def __init__(self,name,sal,age,eno):
#         super().__init__(name,sal)
#         self.age = age
#         self.eno = eno
    
#     def work(self):
#         print("python is easy:")
#         print(self.name,self.sal,self.age,self.eno)

# s = SE("rohit",123456,26,3)
# s.eatdrink()
# s.work()
#===========================================================================
# class GF:
#     def m1(self):
#         print('Land')

# class F(GF):
#     def m2(self):
#         print('cash')

# class U(F):
#     def m3(self):
#         print('enjoy')

# c = U()
# c.m1()
# c.m2()
# c.m3()
#===========================================================================












    
















