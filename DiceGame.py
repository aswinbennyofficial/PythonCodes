import random

roll_again="Y"
score=0

while roll_again=="":
    n=int(input("Input number: "))
    r=random.randint(1,6)
    print("Dice shows: ",r)
    if ( r== n):
        score+=1
        print("Congrats. Your score is",score)
        
    else:
        print("Sorry , You are wrong. Your score is",score)
    
    print("Press Enter to try again or press N to exit")
    roll_again=input()
