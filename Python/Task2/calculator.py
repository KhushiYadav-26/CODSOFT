#calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if(b==0):
        return "Error: divide by zero"
    return a/b
ch="y"
while(ch=="y"):
    print("---Calculator---")
    print("1.Add")
    print("2.Sub")
    print("3.Mul")
    print("4.Div")
    print("----------------")
    a=float(input("enter first num:"))
    b=float(input("enter second num:"))

    print("Enter your choice: ")
    choice=int(input())

    match choice:
     case 1:
        print("The addition is:",add(a,b))
     case 2:
        print("The difference is:",sub(a,b))
     case 3:
        print("The product is:",mul(a,b))
     case 4:
        print("The division is:",div(a,b))
     case _ :
        print("enter valid choice")
    print("Do you want to continue? (y/n):")
    ch=input()

    
        
