print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L:")
pepperoni =  input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == 'S':
    bill = bill + 15
elif size == 'M':
    bill = bill + 20
else:
    bill = bill +25

if pepperoni == 'Y' and size == 'S':
    bill = bill + 2
else:
    bill = bill +3

if extra_cheese == 'Y':
    bill = bill+1
else:
    bill = bill+0
print (f"Your total bill is s {bill}")