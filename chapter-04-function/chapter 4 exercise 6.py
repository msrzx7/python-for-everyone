'''Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).'''
def computepay(Hours,Rate):
    try:

        Hours = float(Hours)
        Rate = float(Rate)

        if Hours > 40:
            Pay = (Hours - 40) * Rate * 1.5 + (40 * Rate)
            print('your pay is ₹',Pay)

        else:
            Pay = Hours * Rate
            print('your pay is ₹', Pay)
    except:
        print('type number properly')
    