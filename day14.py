#Tuples

a=(1,2,3,4,5)
print(type(a))

def sum_diff(a,b):
    s=a+b
    d=a-b
    return(s,d)
c=sum_diff(10,5)
print(c)
print(type(c))

print(list(range(5)))
print(tuple(range(5)))

#Dictionary

a={ 
    "name":'himanshi',
    "college": "LPU"
}
print(a["name"])

key="marks"
if key in a:
    print(a[key])
else:
    print("key does not exist")

print(a.get(key))

print(a.get(key,"key does not exist"))

print(a.keys())

print(a.values())

for key,value in a.items():
    print(key,"->",value)

for x in a:
    print(x)

a=list(a)
print(a)