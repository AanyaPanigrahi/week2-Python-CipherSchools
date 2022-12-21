#abstraction
#encapsulation
#polymorphism
#inheritance

student1={
    "name":"aanya",
    "college":"LPU"
}
student2={
    "name":"riya",
    "college":"LPU"
}
print(student1)
print(student2)


#python object can have multiple attributes
#callable
#iterable
#contextable
#in python,classes are callable

class Person():
    pass

p=Person()
print(p)

print(hex(id(p)))


a=1
def square(a):
    print(a**2)

square(2)

class person:
    def say_hi(self):
        self.name="himanshi"
        print("Hello,how are you "+ self.name+"?")

p=person()
p.say_hi()


class person:
    name="himanshi"
    def say_hi(self):
        
        print(f"Hello Everyone! I am {self.name}")

p=person()
p.say_hi()#method call
person.say_hi(p)#function call



#Dunders

 
class person:
    def __init__(self,name):
        self.name=name
    def say_hi(self):
        print("Hello,how are you ",self.name)

p=person('himanshi?')
p.say_hi()


class A:
    a=1
    b=2

    def __add__(self,x):
        return self.a + self.b + x

a=A()
print(a+3)