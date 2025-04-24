total = 0
count = 0

while True:
    num = input("Enter a number and done when you finished : ")
    
    if num == 'done':
        break
    
    try:
        value = int(num)
        total += value
        count += 1
    except ValueError:
        print("Invalid input. Please enter an integer.")

if count > 0:
    average = total / count
    print("Total:", total)
    print("Count:", count)
    print("Average:", average)
else:
    print("No valid numbers entered.")
