#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")
new_total_bill = float(total_bill)

percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
new_percentage_tip = int(percentage_tip)

total_people = input("How many people to split the bill? ")
new_total_people = int(total_people)

individual_payment = (new_total_bill / new_total_people) * (1 + (new_percentage_tip / 100))
final_payment = round(individual_payment, 2)
print(f"Each person should pay: ${final_payment}")