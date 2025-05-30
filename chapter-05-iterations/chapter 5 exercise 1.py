''' Exercise 1: Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers. 
If the user enters anything other than a integers, detect their mistake using try and except and print an error message and skip to the next integers.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333''

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
