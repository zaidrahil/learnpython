# class emp():
#         salary=120000
#         role="zaid"
# zaid=emp

# print(zaid.salary,zaid.role)

# class student():
#         name="zaid" #this is class attribute 
#         salary=20000

# harry =student()
# #harry.name="rahil" this is object attribute  it override the 
# #different method for accessing and changing content 
# print(harry.name,harry.salary)

# class success():
#         work="hard as much as i can"
#         result="you get what you want"
#         def will(self):
#                 print(f"the thing is work {self.work} then only {self.result}")
# fire=success()
# fire.will()

# class cse1():
#     def zaid(self):
#         name="zaid rahil"
#         rollno=25265
#         print(name,rollno)
# student=cse1()
# student.zaid()



# class student:
#         name=""
#         roll=0
#         def display(self):
#                 print(f"the man is {self.name} how every let down his confindence {self.roll}")
# zaid=student()
# zaid.name="zaid"
# zaid.roll=10
# zaid.display()


# class user:
#     def get_name(self):
#         return "ayani"
#     def greet(self):
#         name=self.get_name()
#         print(f"hello ji {name}")
# usoppa=user()
# usoppa.get_name()
# usoppa.greet()



#this topic are constructor similar to java as you can remeber 
#basically ther are two word in this __init__ in order to define or declare a constructor and before giving
 #a parameter we need to give 


# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=student("zaid",20)
# print(s1.name,s1.age)

# class person:
#     def __init__(self,name,dob,phno,place):
#             self.name=name
#             self.dob=dob
#             self.phno=phno
#             self.place=place

# persona=person("zaid","26012007","9","armoor")
# print(persona.name)
# print(persona.dob)
# print(persona.phno)
# print(persona.place)


# class persons:
#     def __init__(self,name,dob,phno,place):
#         self.name=name
#         self.dob=dob
#         self.phno=phno
#         self.place=place
#     def details(self):
#         return f'{self.name} he is a great boy from {self.place} born on {self.dob} futher details contact{phno}'

# p=persons("zaid","2007","99","armoor")
# print(p.details())

# class person:
#     def __init__(self): #automitically called when object  is called 
#         print("this is dunder method type is constructor ")
    
#     def year(self):
#             print("rowanova zoro")
# p2=person()

# print(p2.year())

class calc:
    n1=int(input("enter a number "))
    def squre(self):
        print(f"a square is n1{n1*n1}")
    def root(self):
        print(f"a root is {self.n1/2}")
cal=calc()
cal.squre()
cal.root()

