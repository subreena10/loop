#print number 1-100#
# number=1
# while number<=100:
#     print(number)
#     number=number+1

# sum=0 #print  numbers from 1 to 10 and their sum#clear

# i=1
# while i<=10:
#     sum=sum+i
#     i=i+1
# print(sum)

i=1
while i<1000:
    j=1
    sum=0
    while i>j:
        if i%j==0:
            sum=sum+i
            j+=1   
    if sum==2:
        print(j,"prime")
    else:
        print(i,"not prime")
    i+=1