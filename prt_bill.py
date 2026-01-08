pt=input("package type(S/G): ")
ft=int(input("food type: "))
ng=int(input("number of guests: "))
def fud(x):
    if x==1:
        a=1000
    elif x==2:
        a=2000
    elif x==3:
        a=1500
    else:
        print("enter valid food type")
    return a
a=fud(ft)
if pt=='S':
    print(f"total bill:{10000+(a*ng)}")
elif pt=='G':
    print(f"total bill:{25000+(a*ng)}")
else:
    print("enter valid package type")