# stateofindia=["telangana","goa","dehli","mumbai","andra","karnataka"]
# print(len(stateofindia))
# stateofindia.pop()
# print(stateofindia)
import random

#RANDOMISATION AND LIST

# import random
# dish=['biryani','paya','harees','tahari','talahua gosht','fried rice']
# curry=['salan','shorba','tomato gsoht']
# recipe=[dish,curry]
# print(random.choice(recipe))

#rock paper sciroo
import random
user=int(input("enter your choic 0-paper,1-for rock,2-scrior,"))
computer=random.randint(0,2)
print(computer)
if user==computer:
        print("draw the match")
elif user==0 and computer==1:
    print("user wins")
elif user==1 and computer==2:
    print("user wins")
elif user==2 and computer==0:
    print("user wins")
elif computer==0 and user==1:
    print("computer  wins")
elif computer==1 and user==2:
    print("computer wins")
elif computer==2 and user==0:
    print("computer wins")
elif user>=3:
    print("usser lose")
