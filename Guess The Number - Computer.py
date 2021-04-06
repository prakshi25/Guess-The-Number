import random
c=0
a=1
b=20
x=0
y=int(input("Enter The Number:"));

while(y!=x):
    for x in range(1):
        x=random.randint(1,20)    
    print(x)
    if(x==y):
        print("You Have Guessed The Correct Number")
        break;
    elif(x<y):
        print("Wrong Guess!Think About A Smaller Number")
        b=y
        print("Now, Limit:",a,"-",b)
    elif(x>y):
        print("Wrong Guess!Think About A Greater Number")
        a=y
        print("Now, Limit:",a,"-",b)
    c=c+1
print("Chances Taken:",c)
