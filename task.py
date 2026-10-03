import random 
n=random.randint(1,100)
chances=-1
guesses=0
while(guesses!=n):
         guesses=int(input("guess number from 1 to 100   "))

         if guesses==n:
             print(f"\ngood guess:{n}")
             print(f"guessed In the chances of {chances}")
             
             
             
         else:
             print("\n wrong guess")
             chances+=1
             if guesses<n:
                   print("\n enter a greter number")
             else :
                  print('\n enter the less number ')