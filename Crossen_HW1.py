# Alexis Crossen
# 9/13/2025
# homework 1

# assignment 1
# ask and create inputs
item_price = float(input("what is the item's price?: "))
item_quanity = float(input("what is the quanity of the item? "))

#create the tax equations

item_subtotal = item_price * item_quanity

tax_amount = item_subtotal * 0.075

total_amount = item_subtotal + tax_amount

# print out the ouputs 

print("Your subtotal without tax is: ", + item_subtotal)
print("Your tax amount is:", + tax_amount)
print("Your total amount, with tax and items is: ", + total_amount)

# assignment 2
#ask for employee - inputs

hourly_wage = float(input("what is your hourly wage?: "))
total_hours = float(input("Total amount of hours worked: "))

# determine over-time pay

if total_hours <= 40:
    base_pay = hourly_wage * total_hours
    overtime_pay = 0
else:
    base_pay = hourly_wage * 40 
    overtime_hours = total_hours - 40
    overtime_pay = hourly_wage * 1.5 * overtime_hours

#calculate the total pay
total_pay = base_pay + overtime_pay

#print results (rounded to 2 decimals)

print("Base Pay: $", round(base_pay, 2))
print("Ovetime pay: $", round(overtime_pay, 2))
print("Total Pay: $", round(total_pay, 2))

#assignment 3:

student_grade = float(input("What is your numeric grade? (1-100):" ))

#create the logic
if student_grade >= 90:
    letter_grade = "A"
elif student_grade >= 80:
    letter_grade = "B"
elif student_grade >=70:
    letter_grade = "C"
elif student_grade >=60:
    letter_grade = "D"
else:
    letter_grade = "F"
# pring both number and letter grade
print("Numeric Grade:", student_grade)
print("Letter Grade:", letter_grade)


#Bonus Eligibility chcker

#Ask for inputs
hours_worked = float(input("Enter total hours worked: "))
performance_score = float(input("Enter performance score (0-100): "))

#Check eligibility
if hours_worked > 35 and performance_score > 85:
    # Step C: Eligible
    print("Congratulations! You earned a $100 bonus!")
else:
    # Step D: Not eligible - figure out what is missing
    missing_hours = 0
    missing_points = 0
    
    if hours_worked <= 35:
        missing_hours = 36 - hours_worked  # need at least 36 hours
    if performance_score <= 85:
        missing_points = 86 - performance_score  # need at least 86 points
    
    print("Sorry, you are not eligible for the bonus.")
    
    # Show what’s missing
    if missing_hours > 0:
        print("You need", missing_hours, "more hours.")
    if missing_points > 0:
        print("You need", missing_points, "more performance points.")

    
    
    
    
    