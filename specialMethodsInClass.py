
class student:
    a=45                        
    def work():                 
        print("I am method of the class")
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def getAge(self):
        return self.age
    
    def __str__(self):
        return "Student name "+self.name + " Age is" +str(self.age)

    def __repr__(self):
        return "Im named " + self.name


s1=student("john", 25)
print(s1)


class mob:
    def __init__(self, brand, ram, camera, cNum):
        self.brandName = brand
        self.ram = ram
        self.camera = camera
        self.callingNum = cNum
    def shot(self):
        print("shooting started")
    def cal(self):
        print("calling" ,self.callingNum)


mob1 = mob("nokia", 8, 108, 7411)
print(mob1.brandName)
print(mob1.camera)
print(mob1.ram)
print(mob1.shot())
print(mob1.cal())


class SmartMobile(mob):
    def __init__(self, brand, ram, camera, cNum, gps):
        super().__init__(brand, ram, camera, cNum)
        self.mylocation = gps
    def record(self):
        return "recording started...."
    



sm1 = SmartMobile("apple", 6, 24, 7411, "mexico")
print(sm1.brandName)
print(sm1.record())
getattr(sm1, "brandName")
getattr(sm1, "shot")()
print(hasattr(sm1, "brandName"))
print(sm1.__doc__)


class aiMob(SmartMobile):
    def __init__(self, brand, ram, camera, cNum, gps):
        super().__init__(brand, ram, camera, cNum, gps)
        
        
        
        