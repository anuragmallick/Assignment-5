#Question 1
d={}
for i in range(1,5):
    key=input("enter the key: ")
    value=input("enter the value: ")
    d[key]=value
print(d)

#Question 2
a={}
b={}
for i in range(1,4):
    b={}
    name=input("enter name")
    for j in range(1,4):
        sub=input("enter subject")
        marks=int(input("enter marks"))
        db[sub]=marks
    a[name]=b
print(a)
stud=input("enter the student's name whose marks u want to see")
print(a[stud])
