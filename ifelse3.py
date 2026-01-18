'''WAP to find out whether student has passed  or failed if it requireds total of 40 per. and atlyst 35 per. in
each sub. to pass assume 3 sub. and take marks input from user'''

n1 = int(input("Enter a marks  subject 1: "))
n2 = int(input("Enter a  marks  subject 2: "))
n3 = int(input("Enter  a marks  subject 3: "))


per = (n1 + n2 + n3 / 300 )* 100
print(per)

if  40 and n1 >= 35 and n2 >= 35 and n3 >= 35 <=per:
    print("Student is PASSED")
else:
    print("Student is FAILED")
