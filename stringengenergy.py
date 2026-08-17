# # # # # #   STRING 22-01-2026
# # # # # # # letter='p'
# # # # # # # sentence='zaid'
# # # # # # # print(letter)
# # # # # # # print(len(letter))
# # # # # # # print(sentence)
# # # # # # # print(len(sentence))
# # # # # # # print(len(letter)==len(sentence))
# # # # #
# # # # # # MULTISTRING
# # # # # # multi_string='''this a multiline sting which means a string with multiple line
# # # # # #  i can write in n number line by the help of triple single quotes and multiple quotes'''
# # # # # # print(multi_string)
# # # # # # multitriple_string="""this a multiline sting which means a string with multiple line
# # # # # #  i can write in n number line by the help of triple single quotes and multiple quotes"""
# # # # #
# # # # # # first_name='madara'
# # # # # # last_name='\tuchiha'
# # # # # # full_name=first_name+last_name
# # # # # # print(full_name)
# # # # # # #it sorted in index form for example
# # # # # # print(first_name[4])
# # # # # # print(last_name[1])
# # # # # #
# # # # # # #the other to concat is follows as directly in print statement
# # # # # # print(first_name+""+"uchiha")
# # # # #
# # # # # #ESCAPE SEQUENCE OF STRING
# # # # # #NOT ONLY IN STRING WE USE FOR VARIOUS PURPOSE
# # # # #
# # # # # # print("Try escape sequene in in python .\n Did you in java \n are do you remenber even that ")
# # # # # # print("how many days it take to complete \n")
# # # # # # print("DAY\tTOPIC\tPRATICE ")
# # # # # # print('1\t 1\t to much ')
# # # # # # print('2\t 3\t 4hours')
# # # # #
# # # # #
# # # # # #STRING METHODS
# # # # #
# # # # # name='zaid\trahiL'
# # # # # n=len(name)
# # # # # lastname=name[n-1]
# # # # # print(lastname)
# # # # # print(name.upper())
# # # # # print(name.lower())
# # # # # print(name.title())
# # # # # print(name.capitalize())
# # # # # print(name.count('a',2,8))
# # # # # print(name.endswith('a'))
# # # # # print(name.expandtabs(9))
# # # #
# # # str="this me still alhamduilaa9876"
# # # sub_str='zaid'
# # #
# # #
# # # numra='232'
# # # print(numra.isnumeric())
# # # print(numra.isidentifier())
# #
# # days='Thirty,Days,of,python'
# # print(days.isupper())
# # print(days.split())
# # print(days.swapcase())
#
# #SLICING
# # langchain='langchain is a software'
# # #first=langchain[0:2]
# # print(len(langchain[-5:-1]))
# # print(langchain[3:])
# # print(langchain[9:])
#
# #REVERSE STRING USiNG SLICING
# name='zaidrahil'
# print(name[::-1])
#
# #SKIPPING CHARACTER
# bt=name[0:9:4]
# print(bt)

#EXCERCISE
# name='ALL STRINGENGENGY'
# print(name[1:])

# name='python for everyone'
# print(name.replace('everyone','all'))
# name='coding for all'
# print(name.find('c'))

# bro='You cannot end a sentence with because because because is a conjunction'
#
# print(bro.index('y',2,5))


#f-string

name='zaid'
height=5.9
isGoodguy=True
#we need to put f just before the the passing string in print
print(f"your name is {name} your height is {height} is {isGoodguy}")

age=int(input("enter your age"))

remainingyear=65
day=remainingyear*365
week=remainingyear*52
print(f"you have this {remainingyear}many years remaining and this week{week},and day{day}")