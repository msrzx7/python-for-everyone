'''Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.
If the score is between 0.0 and 1.0, print a grade using the following table:
Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
< 0.6     F'''

#Solution:

try:
    score = float(input("Enter your score : "))

    if score > 1.0 or score < 0.0:
        print(' Type your score properly.')

    elif 1.0 >= score >= 0.9:
        print("congrats, you got grade 'A'")

    elif 0.9 > score >= 0.8:
        print("keep on good work you got 'B' grade")

    elif 0.8 > score >= 0.7:
        print("You have to work hard you got 'C' grade")

    elif 0.7 > score >= 0.6:
        print("You  have to work really hard, you got 'D' grade")

    else:
        print("Try again next term. you got 'F' grade")

except:
    print("Please enter your score correctly.")

