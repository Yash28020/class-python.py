# # def arth(a,b): 
# #     ask=str(input("sign: ")) 
# #     if "+" in ask: 
# #         return a+b 
# #     elif "-" in ask:
# #          return a-b 
# # x = int(input("first number : ")) 
# # y = int(input("second number :")) 
# # m=arth(x,y) 
# # print(m) 
 
# #  #armstrong number# 
# # def arm(n): 
# #     n = input("enter the value") 
# #     a = len(n)
# #     b = int(n) 

#     # wap to take two input or integer from the user and the find the greatest common# 

def gcd(x,y): 
    x=int(input("Enter the first number: ")) 
    y=int(input("Enter the second number: "))
    i = 1 
    while(i<=x and i<=y): 
        if(x%i==0 and y%i==0): 
            p=i 
        i=i+1 
    return p 
gcd()

# #1. write a function to find the prime numbers 1 to 13 and return product and sum of first and last prime number in the range 
# # wap TO FIND PRIME NUMBER. 
# # def prime(a): 
# #     count = 0 
# #     for i in range (1,a): 
# #         if (a%i==0): 
# #             count = count + 1 
# #     if (count >1): 
# #         print("not prime") 
# #     else: 
# #         print("prime") 
# #     a = int(input()) 
# #     prime(a)

# # ANSWER 1.# 
# def prime(a,b): 
#     s = 0 
#     m = 1 
#     for i in range(a,b+1): #(1,11)
#         count = 0 
#         if i == 1:
#             pass #print("number is 1")
#         else: 
#             for j in range(1,i+1): #(1,3) 
#                 if i%j == 0: 
#                     count = count + 1 
#                 if count > 2: 
#                     pass #print(1,not prime1)
#                 else: 
#                     s = s + i 
#                     m = m * i 
#     print("value of sum:",s) 
#     print("value of multiply:",m)
# a = int(input("Enter the number: ")) 
# b = int(input("Enter the second number: ")) 
# prime(a,b)

