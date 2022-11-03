import random

roll_again="Y"

while roll_again=="Y" or roll_again=="y" or roll_again=="Yes" or roll_again=="yes":
    n=int(input("Input number: "))
    r=random.randint(1,6)
    print("Dice shows: ",r)
    if ( r== n):
        
        print("Congrats")
    else:
        print("Sorry , You are wrong")
    
    print("Press Y to try again")
    roll_again=input()
