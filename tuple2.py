#immutability (no changes)

t = (10,20,30)
#t[1] = 99
#print(t) #error

#packing
coordinate = (4,5)
#unpacking 
x,y = coordinate
print("X : " +  str(x))
print("Y : " +  str(y))

#swaping variable
a = 5
b = 10
a,b = b,a
print("A = "+str(a))
print("B = "+str(b))