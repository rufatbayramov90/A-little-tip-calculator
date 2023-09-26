
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
print(f"{final_amount}")







