# Constants are all caps
MIN_YEARS_SALES = 2
MIN_YEARS_TOP_AWARD = 1

years_sales = int(input('Enter your years of sales exeperience'))
years_top_award = int(input('Enter how many years you have been salesperson of the year: '))

if years_sales >= MIN_YEARS_SALES and years_top_award >= MIN_YEARS_TOP_AWARD:
    print('Congratulations! You are eligible for the Sales manger Position.')
else: 
    print(f'''
          Sorry, you do not meet the requirements fo rthe Sales manager Position.
          
          YOu need at leas: 
          - {MIN_YEARS_SALES} years of sales experience
          - {MIN_YEARS_TOP_AWARD} years as salesperson of the year
          ''')