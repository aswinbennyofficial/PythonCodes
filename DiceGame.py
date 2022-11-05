
import random

roll_again=""
score=0

print(r"""  
  ____
 /\' .\    _____
/: \___\  / .  /\
\' / . / /____/..\
 \/___/  \'  '\  /
          \'__'\/ 
                  """ )

name=input(">>>Enter your name: ")



print("\nWelcome {} to the dice game!!!".format(name))

print("------------------------------ \n")

while roll_again=="":
    n=input("    Predict the number: ")
    
    if not(49<=ord(n)<=54):
        print("    invalid input. Choose range between 1 and 6")
        break
    r=random.randint(1,6)
    print("    Dice shows:        ",r,"\n")
    if ( r== int(n)):
        score+=1
        print("    Congrats. Your score is",score)
        
    else:
        print("    Sorry, You are wrong. Your score is",score)
    
    print("\n")
    print(">>> Press Enter to try again or press N to exit: ")
    roll_again=input()
    
print("\n   ------------------------------ ")    
print("   ",name,"Your total score is:",score)


    
  
