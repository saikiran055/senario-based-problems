ic=int(input("enter item code: "))
q=int(input("enter quantity: "))
ct=input("enter customer type: ")
def fun(ic):
    if ic==1:
        a=530*q
    elif ic==2:
        a=300*q
    elif ic==3:
        a=950*q
    else:
        print("enter valid item code")
    return a
    
a=fun(ic)
if ct=='L':
    print(f"discount:{a*0.25}")
    print(f"Total bill after discount:{a-(a*0.25)}")
elif ct=='N':
    print(f"discount:{a*0.05}")
    print(f"Total bill after discount:{a-(a*0.05)}")
else:
    print("enter valid customer type")