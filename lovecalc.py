name1=input("enter your first name")
name2=input("enter your last name")

name1=name1.lower()
name2=name2.lower()

t1=name1.count('t')
r1=name1.count('r')
u1=name1.count('u')
e1=name1.count('e')
true1=t1+r1+u1+e1

t2=name2.count('t')
r2=name2.count('r')
u2=name2.count('u')
e2=name2.count('e')
true2=t2+r2+u2+e2

l1=name1.count('l')
o1=name1.count('o')
v1=name1.count('v')
e1=name1.count('e')
love1=l1+o1+v1+e1

l2=name2.count('l')
o2=name2.count('o')
v2=name2.count('v')
e2=name2.count('e')
love2=l2+o2+v2+e2

love=love1+love2
true=true1+true2
lovetrue=str(love)+str(true)
lovetrue=int(lovetrue)

print(lovetrue)
if lovetrue<=15 or lovetrue<20:
    print("your good")
elif lovetrue<=20 or lovetrue>=25:
    print("your too good")
else:
    print("your too great")
