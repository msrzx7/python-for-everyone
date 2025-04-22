'''Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.'''
Hours = int(input("How many hours have you worked? : "))
Rate = int(input("what's your rate per hour? : "))

if Hours > 40:
    Pay = (Hours - 40) * Rate * 1.5 + (40 * Rate)
    print("your pay is ₹", Pay)

else:
    Pay = Hours * Rate
    print("your pay is  ₹", Pay)
    

