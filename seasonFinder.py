# Input the month and day
input_month = input()
input_day = int(input())

# TODO: Write if-else statments to determine if the input is valid. Output the result if input is not valid.

# TODO: Write if-else statments to test each month and determine the season of the corresponding date. Output the season.
# Note: Pay special care on March, June, September, and December for two possible seasons
if input_month == "March":
    if input_day > 31 or input_day <= 0:
        print('Invalid')
    elif 20 > input_day:
        print('Winter')
    else:
        print('Spring')
elif input_month == 'April':
    if input_day > 31 or input_day <= 0:
        print('Invalid')
    else:
        print('Spring')
elif input_month == 'May':
    if input_day > 31 or input_day <= 0:
        print('Invalid')
    else:
        print('Spring')
elif input_month == 'June':
    if input_day > 31 or input_day <= 0:
        print('Invalid')
    elif input_day < 21:
        print('Spring')
    else:
        print('Summer')
elif input_month == 'July':
    if input_day > 31 or input_day <= 0:
        print('Invalid')
    else:
        print('Summer')
elif input_month == 'August':
    if input_day > 31 or input_day <= 0:
        print('Invalid')
    else:
        print('Summer')
elif input_month == 'September':
    if input_day > 30 or input_day <= 0:
        print('Invalid')
    elif 22 > input_day:
        print('Summer')
    else:
        print('Autumn')
elif input_month == 'October':
    if input_day > 31 or input_day <= 0:
        print('Invalid')
    else:
        print('Autumn')
elif input_month == 'November':
    if input_day > 31 or input_day <= 0:
        print('Invalid')
    else:
        print('Autumn')
elif input_month == 'December':
    if input_day > 31 or input_day <= 0:
        print('Invalid')
    elif input_day < 21:
        print('Autumn')
    else:
        print('Winter')
elif input_month == 'January':
    if input_day > 31 or input_day <= 0:
        print('Invalid')
    else:
        print('Winter')
elif input_month == 'February':
    if input_day > 28 or input_day <= 0:
        print('Invalid')
    else:
        print('Winter')
else:
    print('Invalid')
