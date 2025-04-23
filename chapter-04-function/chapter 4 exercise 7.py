'''Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.'''
def computegrade(score):
    try:
        score = float(score)

        if score > 1.0 or score < 0.0:
            return 'type your score properly'

        elif 1.0 >= score >= 0.9:
            return "congrats, you got 'A' grade"
        elif 0.9 > score >= 0.8:
            return "keep on good work you got 'B' grade"

        elif 0.8 > score >= 0.7:
            return "You have to work hard you got 'C' grade"

        elif 0.7 > score >= 0.6:
            return "You  have to work really hard, you got 'D' grade"

        else:
            return "Try again next term. you got 'F' grade"

    except:
        return"Please enter your score correctly."

