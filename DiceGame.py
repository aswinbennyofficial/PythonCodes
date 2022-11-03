import random

roll_again=""
score=0

name=input("   Enter your name: ")

print("   Welcome {} to the dice game!!!".format(name))
print("\n \n")

while roll_again=="":
    n=int(input("Input number: "))
    r=random.randint(1,6)
    print("Dice shows: ",r)
    if ( r== n):
        score+=1
        print("  Congrats. Your score is",score)
        
    else:
        print("  Sorry , You are wrong. Your score is",score)
    
    print("\n")
    print("Press Enter to try again or press N to exit: ")
    roll_again=input()
    
print("Your total score is:",score)
