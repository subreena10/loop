user=int(input("Enter ur number: "))
rev=0
while user>0:
    rem=user%10
    rev=(rev*10)+rem
    user=user//10
 