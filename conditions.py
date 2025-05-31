'''
Conditional statements:

if condition:when we have only one condition we use if condition.

syntax:

if (condition):
    we execute the code
    code to executes
    
ex : 
1) if persong is older than 18 than can vote
2) if temperature is gtrreater than 30 than it is hot
3) if marks are greater than 20 student is passed
4) if attendence is greater than 75% than can attend the exams
5) if age is lesser than 12 than its a kid.




if else condition: When we have two options and need to choose one condition in that case we should use ifelse condition.

1, vote eligibility
2, Even odd
3, pass failed


elif condition

'''

#1
#age=int(input("Enter the age:"))
#if(age>18):
   # print("\nhe can 20vote")
   
   
   
#'''temp=int(input("enter the temp")) 
#if(temp>30):
 #   print("we have  heatmap") '''
    
    
'''marks=int(input("Enter the marks:"))
if(marks>20):
    print("pass")'''

'''attendance=int(input("enter attendance"))
if(attendance>75):
    print("eligible")'''

'''age=int(input("enter the age"))
if(age<12):
    print("kid")
'''
'''marks=int(input("enter the marks:"))
if(marks>35):
  print("pass")
else:
  print("fail")'''

'''In an online shopping system, the confirmation of a customer's order depends on two important conditions: 
->the availability of the item in stock and whether delivery is possible in the customer's pin code area. 
If both conditions are satisfied — meaning the item is currently available and the delivery service can reach the customer's location — the order is successfully confirmed. However, if either the item is out of stock or delivery is not available in the given pin code, the system displays a message informing the customer that the order cannot be placed. This ensures a smooth and transparent shopping experience by setting clear expectations before the payment process.

if in stock ---> product is available
if in area of pincode ---> availability

if in stock not available and if in area of pincode alsi it is not available --->  product is not available

'''

'''#stock_availability = str(input())
stock_availability = input("Enter wether the stock is available or not? (yes or no):").strip().lower()
availability_area = input("ENter wether the product is available at the area of pincode or not? (yes or no):").strip().lower()
'''
'''if stock_availability == 'yes' and availability_area == 'yes':
    print("The product is available")
else:
    print("The product is not available")
'''

'''if stock_availability == 'no' and availability_area == 'no':
    print("The product is not available")
else:
    print("The product is  available")'''
    
'''
A child is going to play tennis in the group if it is sunny outside and if it is raining dont let the child play in the groung if not than let the child play in the ground

'''
'''user_sun = input("IS IT SUNNY OUTSIDE(Y/N):").strip().lower()
user_rain = input("IS IT RAINY OUTSIDE(Y/N):").strip().lower()

if user_rain=='y' or user_sun=='y':
    sunny=True
    rainy=True
else:
    sunny=False
    rainy=False
    
if(sunny or rainy):
    print("YOU MAY NOT GO OUT TO PLAY ")
else:
    print("YOU MAY GO OUT TO PLAY")'''
    
    
    