'''
Laptop EMI Eligibility-->

senario --> A bank checks eligibility based on income and credit score so a person can buy laptop if he satisfies the following conditions: 

income >= 50000 and credit score >= 800 ---> eligible
income >= 50000 but credit < 800  ---> Not eligible
income < 50000 not eligible

inputs:
income
credit score

output:
Eligibility

Tracing

1. income = 45000
credit score = 840

income >= 50000
45000 >= 50000 ---> False
credit score >= 800
840 >= 800 --> True

2. income = 52000
   creadit score = 740
   
   income >= 50000
   52000 >= 50000 --> True
   
   creadit score >= 800
   740 >= 800 ---> False
   
3. income = 50000
   credit score = 900
   
   income >= 50000
   50000 >= 50000 ---> True
   credit score >= 800
   900 >= 800 --> True
   
4. income = 10000
   credit score = 200
   
   income >= 50000
   10000 >= 50000 --> False 
   credit score >= 800
   200 >= 800 --> False
   
   



'''

income = int(input("Enter salary:")) #45000,
credit_score = int(input("Enter Credit Score:"))#840

if(income >= 50000): #45000 >= 50000 45000 > 50000? 45000 = 50000 Will not enter inside if block it will go to else block
   if credit_score >= 800:
       print("You are eligible")
   else:
       print("Need to improve Credit score") 
else: 
    print("You are not eligible") #Execute the else block'''
    
income = int(input("Enter salary:")) #52000 52000 >= 50000T The condition is true so it will go inside te if block
credit_score = int(input("Enter Credit Score:"))#740

if(income >= 50000): 
   if credit_score >= 800: #740 >= 800? F Directly go to else block in this scope
       print("You are eligible")
   else:
       print("Need to improve Credit score") #print the statement
else: 
    print("You are not eligible")


income = int(input("Enter salary:")) #50000 >= 50000 Go inside if block
credit_score = int(input("Enter Credit Score:")) #800 >= 800 True Execute the code

if(income >= 50000): 
   if credit_score >= 800: 
       print("You are eligible")
   else:
       print("Need to improve Credit score") 
else: 
    print("You are not eligible")