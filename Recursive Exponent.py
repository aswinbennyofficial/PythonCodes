def main():
    b=int(input("Enter b: "))
    e=int(input("Enter e: "))
    
    if b>=1 and e<=1000:
        print(pow(b,e,1))
    else:
        print("Out of range error")

# def pow(b,e):
#     return b**e

def pow(b,e,s):
    if e==0:
        return s
    s=s*b
    return pow(b,e-1,s)

main()    
    
