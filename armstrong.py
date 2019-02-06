#harish
N=int(input("enter the number:"))
sum=0
temp=N
if(N<100000):
    while(N>0):
        dig=N%10
        sum=sum+dig**3
        N=N//10
    if(sum==temp):
        print("armstrong number")
    else:
        print("not a armstrong number")
else:
    print("invalid")

