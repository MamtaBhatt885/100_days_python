print("Welcome to the tip calculator!")
total_amount = float(input("What was the total bill? "))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
total_number_of_people = int(input("How many people to split the bill? "))
amount_after_tip = (total_amount * (tip_amount/100)) +total_amount
total_bill = amount_after_tip /total_number_of_people
print(f'Each person should pay: ${total_bill}')
