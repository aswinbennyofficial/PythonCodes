import random
import datetime

 
try_again="Y"
attempts=0


current_time=str(datetime.datetime.now().strftime("%H:%M:%S"))
print("Current time is: ",current_time)
with open('RandGameFilez.txt','a') as f:
    print("Game started at "+current_time,file=f)


rand=3#random.randint(100,999)

while try_again=="Y":
    n=int(input("Enter number: "))
    
    if n==rand:
        current_time=str(datetime.datetime.now().strftime("%H:%M:%S"))
        attempts+=1
        print("Congrats")
        with open('RandGameFilez.txt','a') as f:
            print("Correct guess. You cracked it on "+str(attempts)+"th attempt at "+current_time+"\n\n",file=f)
        try_again=""
    else:
        current_time=str(datetime.datetime.now().strftime("%H:%M:%S"))
        attempts+=1
        print("wrong try again")
        with open('RandGameFilez.txt','a') as f:
            print("attempt "+str(attempts)+", Your Guess was at "+current_time,file=f)
        
