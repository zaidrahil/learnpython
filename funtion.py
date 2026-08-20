# def clear(name):
#         return name.lower().strip()
# a=clear('zaiA')
# print(a)

# def person():
#     print("zaid")
# person()
# person()
# person()

# def compliment(name='human begin'):
#     print(name)
# compliment('zaid')

#global local varible

# case_rule='nop'#global varible

# def person(name):#parameter
#     namecleaned=name.lower()#local varible 
#     if case_rule=='zaid':
#         namecleaned=namecleaned.strip()
#     print(namecleaned)
#     print(name)#local varible
# person('   zAId  ')
# print(case_rule)


#postional and keyword argument
# def name(first_name,second_name,gender):
#          person=(first_name.lower()+second_name.lower())
#          print(person,gender)
# name('zaid',' rahil','male')                                #postional  argument
# name(first_name='ayan',second_name='rahil',gender='male')  #keyword argument


def cleandata(id):
    clean=id.strip().lower()
    username,domain=clean.split('@')
    return {username:domain}
print(cleandata('zaid@gamil.com'))

#i did only few practice in funtioon i will do it later 