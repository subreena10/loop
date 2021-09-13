# # num=7
# # factorail=1
# # if num<0:
# #     print("sorry their is no factorail for negitive numbers.")
# # elif num==0:
# #     print("factorail of zero is 1")
# # else:
# #     for i in range(1,num+1):
# #         factorail=factorail*i
# #     print("the factorail of",num ,"is", factorail)

# num=int(input("enter a number: "))
# factorail=1
# if num<0:
#     print("The factorail of negotive number is not defined.")
# elif num==0:
#     print("The factorail of zero is 1.")
# else:
#     for i in range(1,num+1):
#         factorail=factorail*i
#     print("the factorail of",num,"is",factorail)

i=1
factorail=1
num=int(input("enter ur number: ")) #for a particular number#
while i<=num:
    factorail=factorail*i
    print("the factorail of",num,"is",factorail) 
    i=i+1
