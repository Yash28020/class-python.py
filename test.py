# print("hello world") 
# a = 8 
# b = 6
# c = a+b 
# print(c)

def minimum(a,b): 
    if a<b: 
        return a 
    elif b<a: 
        return b 
    else: 
        return ("both the numbers are equal") 
x = minimum(10,3) 
print(x)

def arth(a,b): 
    return a+b, a-b, a*b, a/b 
print(arth(20,10)) 

def fact(n): 
    if n == 0: 
        return 1 
    return n*fact(n-1) #5*4*3*2*1 
print(fact(5)) 

# def demo(*x): 
#     for i in x: 
#         print(i) 
# demo(1,2,4,8,7) 
 
#  #Anonymous function#
# tax = lambda salary: salary*20/100 
# salary = int(input()) 
# print(tax(salary)) 

a = (1,2,3,4) 
print(a*2)