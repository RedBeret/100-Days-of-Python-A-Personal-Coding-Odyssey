# Welcome the user to the application
print("Welcome to the tip calculator!")

# Request the total bill from the user and convert the input to a float
bill = float(input("What was the total bill? $"))

# Request the tip percentage from the user and convert the input to an integer
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Request the number of people the bill will be split between and convert the input to an integer
people = int(input("How many people to split the bill?"))

# Calculate the tip as a percentage
tip_as_percent = tip / 100

# Calculate the total amount of the tip
total_tip_amount = bill * tip_as_percent

# Calculate the total bill including the tip
total_bill = bill + total_tip_amount

# Calculate the amount each person should pay
bill_per_person = total_bill / people

# Round the final amount each person should pay to two decimal places
final_amount = round(bill_per_person, 2)

# Output the final amount each person should pay
print(f"Each person should pay: ${final_amount}")

# Potential improvements: 
# - Add input validation to ensure the user is inputting reasonable values
# - Allow the user to enter a custom tip amount, not just 10, 12, or 15
# - Add a clearer output that includes a breakdown of the bill, the tip amount, and the total
# - Add error handling to protect against user input errors
