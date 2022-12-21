#Functions

a=5
b=7

print(a+b)
print("waiting....")
print("waiting....")
print("waiting....")

print(a-b)
print("waiting....")
print("waiting....")
print("waiting....")

print(a*b)
print("waiting....")
print("waiting....")
print("waiting....")



def show_loading():
    for _ in range(3):
        print("loading....")
    
x=5
y=7

print(x+y)
show_loading()

print(x-y)
show_loading()

print(x*y)
show_loading()


#Functions can take parameters

def sheldon_knock(name):
    for _ in range(3):
        print("knock knock knock",name)

sheldon_knock("leonard")

def sheldon_knock(name , times):
    for _ in range(times):
        print("knock knock knock",name)

sheldon_knock("john", 6)

#return statement

def add(a,b):
    return a+b

x=add(4,5)
print(x)


#keyword arguments

print(1,2,3,4,5,sep=",")

def func(a,b,c):
    print(a)
    print(b)
    print(c)

func(1,2,3)
func(c=1,a=2,b=3)

def hello():
    print("hello world!")

a=hello
a()


#non-default argument follows default argument
#def fun(a,b=10,c):
#   print(a,b,c)


#Arguments in python
#required arguments
#default arguments 
#optional positional only arguments
#required keyworded only arguments
#default keyworded only arguments
#optional keyworded only arguments

def func(r,s):
    print(r,s)

func(1,2)

def func(c=1,d=2):
    print(c,d)

func()
func(2)

def fun(*n):
    print(n)

func(1,2)

def show(a,b,*c,d):
    print(a)
    print(b)
    print(c)
    print(d)

show(1,2,3,4,5,6,7,d=8)

def input(**k):
    print(k)

input(name="john")

#anonymous function or lambda gunction

lambda a, b: a+b