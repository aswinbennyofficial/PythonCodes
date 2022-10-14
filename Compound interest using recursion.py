p=int(input("enter amount: "))
r=int(input("enter interest: "))
y=int(input("enter year: "))

def compintr(p,r,y):
    if y==0:
        return p
        
    else:
        p=p+p*(r/100)
        
        return compintr(p,r,y-1)

print("Compound interest is: ", compintr(p, r, y),"Rs")
