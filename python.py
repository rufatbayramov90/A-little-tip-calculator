
#questions...
#What was the total bill?
#How many people to split the bill?
#what percentage tip would you like to give?

bill = float(input("Include bill"))
tip = int(input("How much do you want to bet?"))
people = int(input("Write the number of people"))

interest = tip / 100
amount = bill * interest
total = bill + amount
bill_person = total/people
final_amount = round(bill_person,2)
final_amount = "{:.2f}".format(bill_person)
print(f"{final_amount}")

'''
#----another syntax
amount = bill * (tip/100)
total = (amount + bill)/people
final = round(total,2)
print(f"{final}")
'''
'''
#current age
age = input("What is your current age")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months ")
'''