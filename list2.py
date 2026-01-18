#slicing list
y = [10,20,30,40,50]
print(y[1:4])

x = ['A','B','C','D','E']

print(x[1:4])
print(x[:3])
print(x[3:])
print(x[: :2])
print(x[: :-1])

#mutability

l = [10,20,30]
l[1] = 99 #[10,99,30]
print(l)

# Adding items

l.append(100)
print(l)   #[10,99,30,100] 