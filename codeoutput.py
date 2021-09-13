# c=0
# d=1
# while c<3:
#     c=c+1
#     d=d*c
#     print("loop ka andar",c,d,end=" ")
# else:
#     print("loop ka bahar",c,d)

# n=6
# s=0
# i=1
# while i <=n:
#     i=i+1
#     s=s+i
# print (s)

# num=int(input("enter a number: "))
# i=2
# while(i<num):
#     if num%i==0:
#         print(num,"it is not a prime.")
#         break
#     i=i+1
# else:
#     print(num,"it is a prime.")

# i = 0
# while(i<5):
#     j = 0
#     while(j<5): #loop2
#         if (j > 3): 
#             break 
#         else:
#             print ("*",end=" " )
#         j = j + 1    
#     print ('%')
#     i = i + 1

x = 0
while(x<7):
    if (x == 3 or x==5):
        x = x + 1
        continue
    print(x)
    x = x + 1