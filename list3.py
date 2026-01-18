#insert function 
l = [10,99,30,100]
l.insert(1,7)
print(l)

# + operator
m = [1,2]+ [3,4]
print(m)  #add the list

#removing
l.remove(99)
print(l)   # [10,7,30,100]

# pop function   (remove by index)
l.pop(2)
print(l) #[10,7,100]

#del function  
del l [0:2]
print(l) #[100]


#clear function
l.clear()
print(l)  #[]
