# #loops practice 

# #sum of a given number 

# n=int(input("enter a number"))
# i=1
# product=1#for  sum of given num sum=0
# for i in range(1,n+1): #for sum range(1,n)
#      product=product*i
#     #for sum sum=sum+1
# print(product)


n=int(input("enter a number"))
for i in range(1,n+1):
        print(" "*(n-i),end=" ")
        print("*"*(2*i-1),end=" ")
        print(" ")

for i in range(1,11):
        print(n,"X",(11-i),"=",(n*(11-i)))