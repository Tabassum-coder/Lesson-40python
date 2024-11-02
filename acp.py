# Armstrong number

sum=0
num=int(input("Enter a number"))

temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10

if sum==num:
    print(num," is armstrong number")
else:
    print(num," is not armstrong number")