# s={1,2,3,4,5,'ZAID'}
# t={4,5,6,7,8,9 }
# #print(s)
# #s.add(6)
# #s.update([7,8,9])
# #print(s)
# #s.remove(9)
# #print(s)
# #s.pop()
# print(s)

# print(t.intersection(s))
#creating a dictionary of hindi words and their meanings

# d={"bola":"spoke","kya":"what","hai":"is","tum":"you","kaise":"how","ho":"are"}
# word=input("enter a hindi word")
# print(d.get(word, "Word not found"))
# s=set()
# for i in range(1,6):
#     n=int(input("enter a number"))
#     s.add(n)
# print(s)

#creating a dictionary of 4 person and there languages they know
d={"zaid":"urdu",
   "rahil":"hindi",
    "ali":"english",
    "sana":"french"
   }
print(d.get("zaid"))
person=str(input('enter a person name'))
lang=str(input('enter a language'))
d[person]=lang
print(d)