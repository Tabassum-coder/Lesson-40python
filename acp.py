# Armstrong number

sum=0
num=int(input("Enter a number"))
#153

temp=num
while temp>0:
    digit=temp%10 #153%10=3 #15%10=5     #1%10=1
    sum=sum+digit**3#sum=0+27 #sum=27+125 sum=27+125+1=153
    temp=temp//10#153//10=15  #15//10=1   #1//10=0

if sum==num:
    print(num," is armstrong number")
else:
    print(num," is not armstrong number")