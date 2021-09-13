num=int(input("Enter a number: "))
sum=0
i=num
while i>0:
    number=i%10
    cube=number*number*number
    sum+=cube
    i=i//10
if num==sum:
    print("it is amstrong number.")
else:
    print("it is not amstrong number.")