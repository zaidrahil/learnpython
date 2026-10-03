
#   EXCEPTION HANDLING 

# print("HELLO EVERYONE TODAYS IS EXCEPTION HANDLING CORE CONCEPT IN PROGRAMMING")
# s=input("enter a number ")
# try :
#     if s=="zaid":
#      print("inshallah")
#     else :
#         raise ValueError("the given input is not correct ")    #rasing the error is excplitx defined by the 
# except ValueError as e :                                        #programmer where we need to define 
#         print(e)

# try :
#     print(5/0)
# except TypeError as e :
#     print(e)
# except ZeroDivisionError as e2 :
#     print(e2,"asdf")
# except Exception as e3:
#     print(e3,"zxc")
# def good():
#     try :
#         print("the coruage is fallen the amunish fallen does there life become meaning less they where not")
#         print("because we refused to died ")

#     except Exception as e :
#          print(e)
#     else :
#        print("great")
#     finally:
#        print("Im zaid i here declare that i will one who going to destroy them")

# good()

# def readit(filename):

#  try:
#     with open(filename) as f:
#         readed=f.read()
#         print(readed)
#  except FileNotFoundError as e:
#     print(e)
#  except FileNotFoundError as e1:
#     print(e1)
# r1=readit("op.txt")

def numpro():
    n1=int(input())
    n2=(input())
    try:
        print(n1+n2)
    except TypeError as e:
        print(e,"i request to enter the number ")
    except ValueError as e1:
        print(e1,"exception")
numpro()


