#lambda expressions

lambda a,b: a+b

a=["john","jake","marie","maggi"]
for a in a:
    print(a)

a=["john","jake","marie","maggi"]
for a in enumerate(a):
    print(a)

a=["john","jake","marie","maggi"]
for a in enumerate(a):
    print(a[0],a[1])

#swapping values
a=15
b=16
a,b=b,a
print(a,b)

#packing and unpacking values

a=[1,2]
b,c=a
print(b,c)

a=["john","jake","marie","maggi"]
for i,a in enumerate(a):
    print(i,"-",a)


#zip
a=["john","jake","marie","maggi"]
b=[10,9,6,8]
for a,b in zip(a,b):
    print(a,"-",b)