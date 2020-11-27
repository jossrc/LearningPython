#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator.")
total_bill = float( input("What was the total bill? $") )
percentage = int( input("What percentage tip would you like to give? 10, 12, or 15? ") )
number_people = int( input("How many people to split the bill? ") )

tip = total_bill * percentage / 100

total_pay = (total_bill + tip) / number_people

print(f"Each person should pay: ${ round(total_pay, 2) }")
