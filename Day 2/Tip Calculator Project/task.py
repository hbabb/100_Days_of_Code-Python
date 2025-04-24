print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percent = tip / 100
total = (bill * percent) + bill
total_str = str(total)
split = str(total / people)

print("The total bill is = " + total_str)
print("Your portion is = " + split)
