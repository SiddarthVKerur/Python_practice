# # # print(3//1.15)
# # # print(10%3.2)
# # # sts = "\"alwd"
# # # print(sts)
# # # # A multi-line quote
# # quote = "\"Always remember your unique,"
# # multi_line_quote = ''' just
# # like everyone else" '''
# # print(quote + multi_line_quote)

# # print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

# # print("I don't like ",end="")
# # print("newlines")

# # a ="hello"
# # print(3+5/8*3-3)

# # print("tha add symbol is %s "%a)

# # a = "hello"
# # a = a+3
# # print(a)

# # long_string = "I'll catch you if you fall - The Floor "

# # print(long_string[5:] + "im there")
# # long_string = "                I'll catch you if you fall - The Floor           " 
# # quote_list = long_string.strip()
# # print(quote_list)
# # print(long_string.capitalize())
# # print(long_string.replace("Floor", "ground"))
# # print(long_string.isalnum())

# # multiplicands = (2, 2, 2, 3, 3, 5)
# # mul=1
# # for mult in multiplicands:
# #     mul=mul*mult
# # print(mul)

# """
# long_string = "HELLO"
# print(long_string.isupper())
# for i in range(10):
#     print("hello", end=" ")

# i=0
# while i<10:
#     print(i,end=" ")
#     i+=1
# """

# # square=[]
# # for i in range(10):
# #     i=i**2
# #     square.append(i)
# # print(square)

# # square = [i**2 for i in range(10)]
# # print(square)

# # planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# # p = []
# # for planet in planets:
# #     if len(planet)<6: 
# #         p.append(planet)
# # print(p)

# # arr = [2*i for i in range(10) if i<10]
# # print(arr)


# # arr = [21,22,23,65,115,415]
# # arr1 = []
# # for i in arr:s
# #     if i<30:
# #         i+=10
# #         arr1.append(i)
# #     else:
# #         i+=5
# #         arr1.append(i)
# # print(arr1)

# '''
# lista = list(range(10))
# for i in lista:
#     if i%2==0:
#         lista.append(i)
#     # else:
#     #     lista.append(i)
# print(lista)

# '''
# '''
# numList = [1,2,3,20,45,95,395]
# list2 = []

# for i in numList:
#     if i<10:
#         list2.append(i*2)
#     elif i%2:
#         list2.append(i+5)
#     else:
#         list2.append(i**2)
# print(list2)
# '''


# class student:
#     a=45                        #property of the class
#     def work():                 #function of the class
#         print("working")
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def getAge(self):
#         return self.age
    
#     def __str__(self):
#         return "Student name "+self.name + " Age is" +str(self.age)


# student1 = student("raju", 15)
# # print(student1)
# # i = 10
# # print(id(i))
# # print(student1.age)
# # print(student1.getAge())

# # print(getattr(student1, "name"))
# # print(getattr(student1, "age"))

# # # getattr
# # print(getattr(student1, "getAge")())    #use() bcz getAge is a function

# # # hasattr
# # print(hasattr(student1, "name"))  #name n age(attributes/property) both are exist in the object student1 so shows true
# # print(hasattr(student1, "age"))
# # print(hasattr(student1, "getAge"))    #no need to use () for the function in hasattr
# # print(hasattr(student1, "height"))  #height is not exist in the object student1 so shows false

# # # Attributes/properties


# # # To call property of a class  (this is class property)
# # print(student1.__class__.a)    

# ##To call function of a class
# # print(student1.__class__.work())

# # # To access property of an object (this is data property)
# # print(student1.name) 


# l = [1,2,1,3,15,1,5,3,3,24,6,1]
# def remove(x,num):
#     [x.remove(i) for i in x if i==num]
#     print(x)
    
# m = [1,5,1,8,4,1,3,56,]
# print(remove(m,8))

# # m = []
# # for i in l:
# #     if i==1:
# #         l.remove(i)
# # print(l)

# text = "hello"[::-1]
# print(text)

# l[0] = 50
# print(l)





# (a,b,c) = (1,2,3)
# print(a)

# print(l.count(1))
# print(l.index(1))




# num1 = int(input("enter 1st num"))
# num2 = int(input("enter 2nd num"))
# num3 = int(input("enter 3rd num"))

# if num1>num2 & num1>num3:
#     print(num1, "is greater")
# elif num2>num1 & num2>num3:
#     print(num2, "is greater")
# else:
#     print(num3, "is greater")

# n1 = 0
# n2 = 1
# series = 10

# for i in range(0,series):
#     print(n1,n2)
#     n1, n2 = n2,n2+n1

# print("falsk & geeks programme")

# for i in range(1,50):
#     if i%3==0 and i%5==0:
#         print("flask geeks")
#     elif i%3==0:
#         print('flask')
#     elif i%5==0:
#         print('geegks')
#     else:
#         print(i)





def fab(n):
    if n<=1:
        return n
    else:
        return fab(n-2) + fab(n-1)

for i in range(4):
    print(fab(i))






print("falsk & geeks programme")

for i in range(1,50):
    if i%3==0 and i%5==0:
        print("flask geeks")
    elif i%3==0:
        print('flask')
    elif i%5==0:
        print('geegks')
    else:
        print(i)