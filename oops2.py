# class twoDvector():
#     def __init__(self,i,j):
#      self.i=i
#      self.j=j

# class threedevector(twoDvector):
#     def __init__(self,i,j,k):
#        super().__init__(i, j)
#        self.k=k

#     def showing(self):
#        print(f"{self.i}i and {self.j} and k{self.k}")
# twoD=twoDvector(2,4)
# threeD=threedevector(2,4,6)
# threeD.showing()

# class employee():
#      eno=23
#      salary=100000
#      increase=1000
#      def incrementing(self):
#           return(self.salary+self.salary*(self.increase/100))
# e1=employee()
# print(e1.incrementing())

# class animal():
#           pass
# class pets(animal):
#         pass
# class dog(pets):
#         @staticmethod
#         def bark():
#                 print("bahooo")
# d1=dog()
# d1.bark()

class customer():
    def __init__(self,name,bankno,branch):
        self.name=name
        self.bankno=bankno
        self.branch=branch
    def detaails(self,bank):
        self.bank=bank
        print(f"name of customer{self.name} and this details \n bankno {self.bankno} \n {self.branch}\n {self.bank}")
c1=customer("zaid",5,"armoor")
c1.detaails("sbi")

class vec1():
        def __init__(self,x,y,z):
             self.x=x
             self.y=y
             self.z=z
        def add(self,other):
             result=self.x+other.x,self.y+other.y,self.z+other.z
             return result
        def mul(self,other):      
             result1=self.x*other.x,self.y*other.y,self.z*other.z
             return result1
vec11=vec1(2,4,6)
vec22=vec1(3,5,7)


class computer():
     brand="zaid rahil"
     
     def __init__(self,cpu,ram,ssd):
          self.cpu=cpu
          self.ram=ram
          self.ssd=ssd
          
     def display(self):
          print(f"{self.ram}")
     @classmethod
     def info(nigga):
          return nigga.brand
c1=computer("zaid","16","500")          
c1.display()
print(computer.info()) 


class student():
     
     college="gptnzb"
     
     def __init__(self,pinno,name,branch):
          self.pinno=pinno
          self.name=name
          self.branch=branch
     
     def display(self):
          print(self.pinno,self.name,self.branch)
     
     def feedetails(self,fee):
          if self.branch=="cse":
               fee=30000
               return fee
          elif self.branch=="ece":
               fee=20000
               return fee
          elif self.branch=="eee":
               fee=10000
               return fee
     
s1=student(5,"zaid","cse")
s1.display()
s1.feedetails()
print("practice it properly ")
#the syntax is simple init is constutor which can accesesd by 