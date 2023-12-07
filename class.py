# # class Person:
# #     name = "yash" 
# #     a = 5 
# #     occupation = "HR"

# # b = Person()
# # print("(self b.name) is a (self b.occupation)")
# #Self means that object on which this method is being called.
# class Vehicle: 
#     def __init__(self,max_speed,mileage):
#         self.max_speed = max_speed 
#         self.mileage = mileage
# X = Vehicle(60,342)
# print(X.mileage,X.max_speed) 

# class SubString: 
#     def SubStringExist(self,str1,str2):
#      if str2 in str1:
#         print(str1)
#      else:
#         print(str2) 
# str1 = input()
# str2 = input()
# Subs=SubString()
# Subs.SubStringExist(str1,str2) 

class Calculation:
    def __init__(self,a,b): 
        self.a=a 
        self.b=b 
    def addition(self): 
     print(self.a+self.b) 
class My_Calculation(Calculation):
   def __init__(self,a,b):
      self.a=a
      self.b=b 
      def multiplication(self): 
         print(self.a*self.b) 

a = int(input())
b = int(input()) 
c=My_Calculation(a,b) 
c.addition()
c.multiplication()
    