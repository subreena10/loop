# count=1
# while count<100:
#     if count%2==0:
#         print( count,"is even")
#     else:
#         print(count,"is odd")
#     count=count+1
        
i=1
sum=0
while i<=100:
    if i%2==0:
       sum=sum+i
       average= sum/100
       print(i,"is even")
    else:
        sum=sum+i
        average= sum/100
        print(i,"is odd.")
    print(average,"of odd number")
    i=i+1
print(average," average of even number.")
