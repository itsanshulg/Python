##String
while(True):
    print("1-Concatinate")
    print("2-Upper Case")
    print("3-String present or not")
    print("4-split")
    print("5-Sliceing")
    print("6-Reverse")
    print("7-length of string")
    print("8-Iterate")
    print("9-Multiply")
    print("10-last character")
    print("0-exit")
    ch=int(input("enter your choice="))
    if(ch==1):
        a=input("Enter String=")
        b=input("Enter String=")
        print(a+b)
    elif(ch==2):
        a=input("Enter String=")
        b=input("Enter String=")
        print(a.upper())
        print(b.upper())
    elif(ch==3):
        a=input("enter string")
        b=input("Enter string to check")
        print(b in a)
    elif(ch==4):
        a=input("Enter String")
        print(a.split())
    elif(ch==5):
        a=input("Enter strin")
        b=int(input("Enter starting location"))
        c=int(input("Enter last location"))
        print(a[b:c])
    elif(ch==6):
        a=input("Enter String=")
        b=a[::-1]
        print(b)
    elif(ch==7):
        a=input("Enter String=")
        print(len(a))
    elif(ch==8):
        a=input("Enter String=")
        for b in a:
            print(b)
    elif(ch==9):
        a=input("Enter String=")
        b=int(input("Enter how many time mul"))
        print(a*b)
    elif(ch==10):
        a=input("Enter String=")
        b=a[-1]
        print(b)
