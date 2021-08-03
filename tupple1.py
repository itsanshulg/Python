#tupple
while(True):
    print("1-Concatinate")
    print("2-max value")
    print("3-length of tupple")
    print("4-extract an element")
    print("5-count no of element")
    print("6-Reverse")
    print("7-multiply")
    print("8-extract apart of element")
    print("9-convert to list")
    print("10-print last element")
    print("0-exit")
    ch=int(input("enter your choice="))
    t=tuple(input("Enter tupple"))
    if ch==0:
        break
    elif ch==1:
        t1=tuple(input("Enter tuple"))
        print(t+t1)
    elif ch==2:
        print(max(t))
    elif ch==3:
        print(len(t))
    elif ch==4:
        a=int(input("Enter position"))
        print(t[a])
    elif ch==5:
        a=int(input("Enter element"))
        print(t.count(a))
    elif ch==6:
        print(t[::-1])
    elif ch==7:
        a=int(input("enter no of time"))
        print(t*a)
    elif ch==8:
        a=int(input("enter starting position"))
        b=int(input("Enter last element"))
        print(t[a:b])
    elif ch==9:
        l1=list(t)
        print(l1)
    elif ch==10:
        print(t[-1])
