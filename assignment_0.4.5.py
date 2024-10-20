# Constants are all caps
MIN_YEARS_DRIVING = 2
MAX_ACCIDENTS_LIMIT = 4

years_driving = int(input('Enter your years of experience driving: '))
accidents_limit = int(input('Enter how many accidents you have been in: '))

if years_driving >= MIN_YEARS_DRIVING and accidents_limit >= MAX_ACCIDENTS_LIMIT:
    print('Congratulations! You are eligible for a loan.')
else: 
    print(f'''
          Sorry, you do not meet the requirements for a loan.
          
          YOu need at leas: 
          - {MIN_YEARS_DRIVING} years of driving
          - {MAX_ACCIDENTS_LIMIT} amount of accidents
          ''')