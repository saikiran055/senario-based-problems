tp=int(input("enter time period:"))
nt=int(input("no of times:"))
pt=input("you want at peak time(Y/N):")
a=0
if pt=='Y':
    if tp<45:
        a=7500
    elif tp>=45 & tp<60:
        a=12000
    else:
        a=25000
    print(f"total amout to be paid to the tv channel:{(a*nt)+0.20}")
elif pt=='N':
    if tp<45:
        a=7500
    elif tp>=45 & tp<60:
        a=12000
    else:
        a=25000
    print(f"total amout to be paid to the tv channel:{(a*nt)}")