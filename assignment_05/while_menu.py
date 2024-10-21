# prime menu option variable 
menu_option = ''

while menu_option != 'q':
    #print menu options
    print(f'''
      Newspaper Sections
      a: read City and County Report
      b: read Opinion articles
      q: close 
      ''')
    # Allows user to input a menu option, sets menu_option variable equal to user input
    menu_option = input('Enter a letter to read a section of our Newspaper:')
    #if menu option is 'a' prints this statement:
    if menu_option == 'a' :
        print ('Why Voting This Week is Crucial for Students by Lawerence Jones')
    #else, if menu option is 'b' prints an input statment asking if the user is a new plant owner
    elif menu_option == 'b':
        new_plant_owner = input('Do you want to read Opinion Columns or Editorials? (c or e):')
        if new_plant_owner == 'c':
            print("Graduate School isn't for Everyone Column by Delaney Broderick")
        else:
            print("2024 Editorial Board Endorsements")
