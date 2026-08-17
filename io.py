# f=open("demo.txt","+a")
# data=f.read()

# z=open("demo.txt","+a")
# d=z.write("not in the blood sir not in blood")
# data=z.read()
# print(data)


# with open("demo.txt","+r") as file:
#         print(file.read())
#         file.write("you can zaid ")

# with open("student.txt","a") as file:
#         file.write("\n zaid is my name ")

# with open("student.txt","r") as f:
#                 data=f.read()
# newdata=data.replace("not","nt")
# print(newdata)

# def check_word():
#     with open("student.txt","r") as file:
#         data=file.read()
#         # if(data.find(word)!=1)
#         if check_word in data:
#             print("i did")
#             print(data.index(check_word))
#         else:
#             print("no use")

# check_word(word='i can')


# with open("student.txt","r") as file:
#         data=file.read()
#         # if(data.find(word)!=1)
#         print(data)
#         num=""
     
#         for i in range(len(data)):
#                 if(data[i]==","):
#                         print(int(num))
#                         num=""
#                 else:
#                         num += data[i]
#         # print(int(data))
#         # print(len(data))


# with open("poem.txt","r") as file:
#       data=file.read()
#       print(data.index("twinkle"))
# import random

# # Generate a random score
# score = random.randint(10, 60)
# print(f"The generated score is: {score}")

# # Use 'with' to open the file in write mode ('w') to overwrite it with the new score.
# with open("gamescore.txt", "w") as f:
#     f.write(str(score) + "\n")

# # Reopen the file in read mode ('r') to read its contents
# with open("gamescore.txt", "r") as f:
#     data = f.read()
#     print("Content read from file:")
#     print(data.strip()) # .strip() removes the extra newline for cleaner output

import random
def flyhigh():
    highscore = random.randint(10,40)
    print(highscore)

with open("gamescore.txt","r") as f:
    score=f.read()
    if(highscore>score or highscore==score):
        print(highscore)
        with open("gamescore.txt","w") as f:
            if(highscore>score):
                highscore=int(highscore)
                f.write(highscore)
    else:
        print("not an highscore")

flyhigh()