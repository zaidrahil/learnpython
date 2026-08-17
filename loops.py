#loops excersise 

# li=[1,"ayan",2,"zaid",3,"rahil",4,"sohail",5,3,3.3333]
# i=0
# j=0
# # while (i< len(li)):
# #     print(li[i])
# #     i+=1

# for j in li:
#     print(j)

# I=[12,3,4,5]
# for i in I:
#     print(i)
# else:
#     print("the loop is completed")
# i=0
# for i in range(0,100,10):
#     print(i)

# name=['zaid','rahil','ayan','sohail','kamal','khan','bhai']

# for i in name:
#     if(i=='khan'):
#         print(i)
#         break
    
# i=0
# for i in range(0,20):
#     if(i%2==0):
#         continue
#     print(i)

#practice excersise
# table=int(input("enter the number"))
# for i in range(1,11):
#     print(table,"x",i,"=",table*i)

l=["ayan","ayaana","anaeta","zaid","rahil"]

# for name in l:
#       if(name.startswith("a")):
#           print("salam "+name)
#       else:
#           print("walikum "+name)
# #other option
    # if(l[i][0]=='a'):
    #  print('salam')
i=0
while i<len(l):
     if l[i][0]=='a':
          print('salam',l[i])
          i +=1
     else:
          break