# hour=(input("enter hours"))
# rate=(input("enter rate per hour"))
# print("weekly earning is :",int(hour)*int(rate))

# a=int(input("enter a value"))
# b=int(input("enter b value"))
# print("the final value is ",int((a+b)/2))
#

#LEAP YEAR CHECKER

# year=int(input('enter year'))
# if year%4==0:
#    if year%100==0:
#        if year%400==0:
#            print("leap year")
#        else:
#            print('enter valid year')
#    else:
#        print('enter valid year')
# else:
#    print('enter valid year')

height = int(input("enter your height"))
if height < 120:
    print("let check your height")
    age = int(input("enter your age"))
    if age < 12:
        print("the price will be 12")
        bill = 12
    if age <= 15:
        print("your price will be 14")
        bill = 14
    elif age >= 45 and age <= 55:
     print("your price will be 0")
     bill = 0
    else:
        print("your price will be 15")
        bill = 15

    wantapotho = input("want a photo ? for 3 dollar")
    if wantapotho == 'yes':
        bill = bill + 3
        print('your total will', bill)
else:
    print("sorry dinosaur i cant")

# #PIZZA ORDERING PROBLEM
# size=int(input("size of pizza 12,15,18"))
# peppronis=int(input("peppronis to pizza 12,15,18"))
# extrachesses=int(input("extra chesses to pizza 12,15,18"))
# bill=0
#
# if size==12:
#     print("your bill will be 15")
#     bill+=15
# elif size==15:
#     print("your bill will be 12")
#     bill+=18
# else:
#     print("your bill will be 20")
#     bill+=20
#
# if peppronis==12:
#     print("your peppronis cost will 2 for small")
#     bill+=2
# elif peppronis==15:
#     print("your peppronis cost will 3 for large")
#     bill+=3
# else:
#     print("your peppronis cost will 4 for large")
#     bill+=4
#
#
# totalbill=bill+peppronis
# print("total bill is "+str(totalbill))
#
