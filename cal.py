
# long_string = "HELLO"
# print(long_string.isupper())
# for i in range(10):
#     print("hello", end=" ")

# i=0
# while i<10:
#     print(i,end=" ")
#     i+=1
    



arr = [21,22,23,65,115,415]
arr1 = []
for i in arr:
    if i<30:
        i+=10
        arr1.append(i)
    else:
        i+=5
        arr1.append(i)
print(arr1)

ar = [num+10 if num<30 else num+5 for num in arr ]
print(ar)