#other than 3 datatypes all datatypes in python are immutable
a=[1,2,3,4,5,6]
print(a)

b=["himanshi",1,1.5,print]
print(b)

a=[0,1,2,33,4]
a[3]=3
print(a)

print(len(b))

c=[22]
print(c*2)

for x in b:
    print(x)

#indexing and list slicing

d=[13,23,33,43,53]
print(d[-1])

#updating the list
#insert
#append

e=[10,20,30,40]
print(e.append(200))

print(e.pop())
print(e.pop(0))

a=["john","jake","marie","maggi"]
print(a.remove("john"))
print(a)

#sorting and reversing
a=[4,8,54,454,434]
print(sorted(a))#other method a.sort()
print(reversed(a))#other method a.reverse()

#map

g=[10,20,30,40,50]
for x in map(lambda x: x**2,g):
    print(x)


#printing a list using join
print(",".join(["c","a","t"]))