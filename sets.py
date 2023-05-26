set = {99,0,3,6,7,99,87, True, "name"}      

# print(set)            # does not contain duplicates(6) shows only one time
a = {1,2,3,4,5,6}
b = {5,6,7,8,9,0}

# print(a.union(b))       # returns a set containing elements of a n b
# print(a.update(b))      # set (a) is updated and contains its elements n b elements removes duplicates
# print(a.intersection(b))  #return a set containing elements which are common between a & b
# print(a.intersection_update(b)) # set (a) is updated and contains those elements which are common between a&b

#add() used to add single element
# a.add(100)
# print(a)

#remove() used remove elements from the set
# a.remove(1)      
# print(a)
# a.remove(8)     # if the entered value is not found in set thn throws error but not discard() method

#discard() used remove elements from the set
# a.discard(1)
# print(a)
# a.discard(28)       #if the entered value is not found in set thn doesnt shw error

#pop() removes any elements from the set bcz sets are unorderd 
a.pop()
print(a)
