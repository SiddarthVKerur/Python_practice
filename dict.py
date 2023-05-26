# dic3 = {"a":1,"a":2,"b":3}
# print(dic3)
# print(dic3['a'])
#-------------------------------------------------------------------------
# dic1 = {"a": {"b": "john", 3: "A" }, "b": True}

# print(dic1["a"]["b"])       #=> john
#--------------------------------------------------------------------------

dic2 = {"a": 1, "b": 2, "c":3, "c": 4, "d":4, True: 1}  #value c is override

for i in dic2:
    print(i)            #prints key values only
    print(dic2[i])      #prints values

print('a' in dic2)      
print("y" in dic2)

#changing values of the keys
dic2["a"]=10
dic2["b"]=99

#adding elements to dictionary

dic2["e"]=5
print(dic2)

dic2["num"]=5
print(dic2)

dic2[True]="two"                    # type: ignore
print(dic2)

dic2["name"]="ramu"                 # type: ignore      #pylance error

dic2[(1,2,34,6)]={1,2,35,6}         # type: ignore

#del deleting elements from dictionary

del dic2["a"]
print(dic2)

del dic2[True]
print(dic2)

# pop() removing elements 

dic2.pop("b")
print(dic2)

dic2.pop("name")
print(dic2)

# popitem() removes last element from the dictionary
dic2.popitem()
print(dic2)



#clear() clearing dictionary elements
dict = {1:"a", 2: True, "c": 3, "num": 3} 
dict.clear()

print(dict)

#copy() elements
b = {1:"a", 2:"b", "c": 'cat', "t":(2.1,4,25)}
a = b.copy()
print(a)


#items() #Returns a list containing a tuple for each key-value pair in dictionary dic
print(b.items()) 


#get() Returns the value of the specified key k from dictionary dic

print(b.get(1))     
print(b.get(2))     
print(b.get("t"))     
print(b.get("c"))     

#keys()returns the list containing keys

print(b.keys())

#value() return a list containing values

print(b.values())


a = {}
a[1]="ramu"
a["f"]="john"
a["b"]="boolean"
print(a)






# def histogram(seq):
#     d = dict[]
#     for element in seq:
#         if element not in d:
#             d[element] = 1
#         else:
#             d[element] += 1
#     return d

# h = histogram('brontosaurus')
# print h





# dic = {"a": (1,2,4,56), (2,3,4): [3,5,3]}
# print(dic[2,3,4])

# t = (2,{5:"g"},4)
# print(t[1])

