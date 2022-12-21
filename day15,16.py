#Sets-unordered and cannot be indexed

a={1,1,1,1,1}
print(a)
print(type(a))

a=list(a)
print(a)

a={1,2,3,4,5}
a.add(7)
print(a)

a.remove(2)
print(a)

for i in a:
    print(i)

a={1,2,3,4}
b={3,4,5,6}

print(a-b)

print(a.union(b))

print(a.intersection(b))

a=[1,2,3,4,5,6]
print(id(a))

class Student:
    name="himanshi"
    college="LPU"

a=48
b=48
print(a==b)
print(a is b)

a="himanshi"
print(hash(a))

#keys of dict can be any hashable object


#Comprehension of Data Structures

a=[]
for i in range(5):
    a.append(i)
print(a)

print([ i for i in range(5) ])

print(list(map(lambda x: x**2,range(5))))

a=[]
for i in range(5):
    temp=[]
    for j in range(5):
        temp.append(j)
    a.append(temp)
print(a)

print([ [j for j in range(5)] for i in range(5) ])

n=5
print([ [max(i+1,j+1,n-i,n-j) for j in range(n)] for i in range(n) ])

#syntax of list comprehension
#''' [<value to appen> <for statement>...<if statement>...]'''

a=[]
for i in range(3):
    for j in range(3):
        a.append(j)
print(a)

print([j for i in range(2) for j in range(2)])

print([(i,j) for j in range(2) for i in range(2)])

#dict comprehension

print({
    2:4,
    3:9,
    4:16,
})

print({i:i**2 for i in range(5)})

#set comprehension

print({i for i in range(5)})