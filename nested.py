ticket = input("Enter whether the customer have ticket of not(Yes/No)").strip().lower()
age = int(input("enter the age:"))

if(ticket == 'yes'):
    if(age < 18 or age > 60):
        print("you can not watch the movie")
    else:
        print("you can watch the movie")
else:
    print("pleasue buy the ticket")
        
        
'''age = int(input("Enter the age:"))      
if(age < 18 or age > 60):
    print("you can not watch the movie")
    print("you can not watch the movie")
else:
    print("you can watch the movie")
    '''