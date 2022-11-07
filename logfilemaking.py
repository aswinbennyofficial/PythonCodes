import random
import datetime

 
try_again="Y"
attempts=0


current_time=str(datetime.datetime.now())
print("Current time is: ",current_time)
with open('RandGameFilez.txt','a') as f:
    print("Game started at "+current_time,file=f)


rand=random.randint(100,999)

while try_again=="Y":
    n=int(input("Enter number: "))
    
    if n==rand:
        current_time=str(datetime.datetime.now())
        attempts+=1
        print("Congrats",attempts)
        with open('RandGameFilez.txt','a') as f:
            print("attempt "+str(attempts)+", Your Guess was at "+current_time,file=f)
        try_again=""
    else:
        current_time=str(datetime.datetime.now())
        attempts+=1
        print("try again",attempts)
        with open('RandGameFilez.txt','a') as f:
            print("attempt "+str(attempts)+", Your Guess was at "+current_time,file=f)
        
