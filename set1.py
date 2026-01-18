#create a set

n = {1,2,3,4,5}
f = {"apple","banana","mango"}
m = {1,"hello",(5,6)}
emt = set()
b = set()
print(type(b))

#adding and removing element

s = {10,20}
s.add(30)
print(s)
s.update([10,20,30,40,50])
print(s)

s.remove(30)
print(s)


s.clear()
print(s)