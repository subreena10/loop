n=int(input("Enter a number: "))
i=1
sum=0
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if sum==n:
    print("it is perfect number",n)
else:
    print("it is not a perfect number",n)
