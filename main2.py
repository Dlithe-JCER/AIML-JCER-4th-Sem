'''

let take a example--->

balance = 5000
amount = 500

1.
amount > balance
500 > 5000 False 

amoutn % 100 != 0
502 % 100 != 0 False

5000-500=4500

you can withdra

2.
balance = 5000
amoutn = 6000

amount > balance
6000 > 5000  True warning

6000 % 100 != 0

3.

balance = 1000
amount = 102

102 > 1000? False

102 % 100 != 0

4. 
balance = 10000
amount = 10000

10000 > 10000 ? False

10000 % 100 != 0 False

10000-10000 = 0


'''

balance = int(input("Enter a balance:"))
amount = int(input("Enter the amount:"))

if amount >  balance:
    print("Insufficient Amount")
elif amount % 100 != 0:
    print("You can not withdraw money")
else:
    balance -= amount
    print("\nWithdraw is succussfull")
    print("\nThe balance is :", balance)