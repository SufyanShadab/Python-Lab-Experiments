n=int(input("enter n:"))
dict={}
i=0
while i<n :
    x=input("enter name:")
    y=input("enter phone number:")
    dict.update({x:y})
    i+=1
while True:
    p=int(input("Phone Book Operations:\n1.Print book\n2.Print names\n3.Print phone numbers\n4.Delete entry\n5.Exit\n"))
    if(p==1) :
        print(dict.items())
    elif p==2 :
        print(dict.keys())
    elif p==3 :
        print(dict.values())
    elif p==4 :
        d=input("enter name:")
        del dict[d]
    elif p==5 :
        exit(1)
    else :
        print("invalid input")