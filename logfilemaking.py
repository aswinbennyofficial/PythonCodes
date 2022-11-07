import random
import datetime 

 
try_again="Y"
attempts=0


current_time=str(datetime.datetime.now().strftime("%H:%M:%S")) #fetches current time
print("Current time is: ",current_time)
with open('RandGameFilez.txt','a') as f:
    print("Game started at "+current_time,file=f) #logs it to the file


rand=random.randint(100,999) #generates random number
#print(rand)

while try_again=="Y":
    n=int(input("Guess the number: "))
    if 100<=n<=999:
        if n==rand:
            current_time=str(datetime.datetime.now().strftime("%H:%M:%S"))
            attempts+=1
            print("Congrats. Thanks for playing")
            with open('RandGameFilez.txt','a') as f:
                print("It took you "+str(attempts)+" attempts to guess the code at time "+current_time+"\n\n",file=f)
            try_again=""
        else:
            current_time=str(datetime.datetime.now().strftime("%H:%M:%S"))
            attempts+=1
            print("wrong try again")
            with open('RandGameFilez.txt','a') as f:
                print("attempt "+str(attempts)+", Your Guess was at "+current_time,file=f)
    else:
        print("Number is out of range")

        
