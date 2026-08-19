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

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("zaid",20)
print(s1.name,s1.age)