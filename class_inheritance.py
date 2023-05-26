
class student:
    a=45                        #property of the class
    def work():                 #function of the class
        print("I am method of the class")
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def getAge(self):
        return self.age
    
    def __str__(self):
        return "Student name "+self.name + " Age is" +str(self.age)


student1 = student("raju", 15)
# print(student1)
# i = 10
# print(id(i))
# print(student1.age)
# print(student1.getAge())

# print(getattr(student1, "name"))
# print(getattr(student1, "age"))

# # getattr
print(getattr(student1, "getAge")())    #use() bcz getAge is a function

# # hasattr
# print(hasattr(student1, "name"))  #name n age(attributes/property) both are exist in the object student1 so shows true
# print(hasattr(student1, "age"))
# print(hasattr(student1, "getAge"))    #no need to use () for the function in hasattr
# print(hasattr(student1, "height"))  #height is not exist in the object student1 so shows false

# # Attributes/properties


# # To call property of a class  (this is class property)
# print(student1.__class__.a)    or
# print(student1.a)

##To call function of a class
# student1.__class__.work()

# # To access property of an object (this is data property)
# print(student1.name) 

#inheritance

class Cs_student(student):
    def __init__(self, name, age, standard):
        super().__init__(name, age)
        self.standard = standard
    def getAge(self):
        print("age = ",self.age)
        

Cs_student1 = Cs_student("raj", 25, 7)

print(Cs_student1.name)
print(Cs_student1.age)
print(Cs_student1.standard)
Cs_student1.getAge()

#printing property and method of class student
print(Cs_student1.a)  #or 
print(Cs_student1.__class__.a)
Cs_student1.__class__.work()

#-------------------------- Practice-------------------------------------

class LivingBeings(student):
    living = 'alive'
    health = "good"
    def look():
        print("seeing things")
    def __init__(self, name, age, category, legs, eyes, ears, location):
        super().__init__(name, age)
        self.category = category
        self.legs = legs
        self.eyes = eyes
        self.ears = ears
        self.location = eyes
        self.location = location
    def sound(self):
        print("making sound")
    def work(self):
        print("earning")
    def getCategory(self):
        return self.category
    def setLegs(self, legs):
        self.legs = legs
    def getlegs(self):
        return "human beings have", self.legs, 'legs'

humanBeing = LivingBeings("raju", 34, "human", 2, 2, 2, "on earth")
print(humanBeing.category)
print(humanBeing.legs)
humanBeing.sound()
humanBeing.work()
humanBeing.setLegs(4)
print(humanBeing.getlegs())
print(humanBeing.getCategory())
humanBeing.legs = 3             #changing attributes value
print(humanBeing.legs)

#attributes & methods of class
print(humanBeing.living) #or
print(humanBeing.__class__.living)
print(humanBeing.health) #or
print(humanBeing.__class__.health)
humanBeing.__class__.look()
LivingBeings.health = "poor"            #changing attribute value of class
print(LivingBeings.health)


class Human(LivingBeings):
    def __init__(self,name, age, category, legs, eyes, ears, location, speak):
        super().__init__(name, age, category, legs, eyes, ears, location)        
        self.speak = speak
    def usingMob(self):
        print("calling people")
        print('capturing things')
    def setLocation(self, location):
        self.location = location
    def work(self):
        return super().work()



human1 = Human("raju", 34, "man", 2, 2, 2, 'bengaluru', "english")
print(human1.eyes)
human1.setLocation("mumbai")
print(getattr(human1, "location"))
getattr(human1, "usingMob")()
print(human1.name)


Human.health = "nice"
print(Human.health)
human1.health = "healthy"
print(human1.health)

print(human1.name)



