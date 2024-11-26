import sys  # don't use quit() or exit() in production code. Use sys.exit.

# Make program repeat:
while True:

    # Get user input for file:
    file_variable = input('''What file would you like to search for? 
    a) 60s-music file 
    b) athletes file
    x) to exit
    ''')


    # Process user input
    if file_variable == 'x':
        sys.exit()
    elif file_variable == 'a':
        file_variable = '60s_music.csv'
    elif file_variable == 'b':
        file_variable = 'athletes.csv'
    else:
        print('Invalid option. Please select a, b, or x.')
        continue
    # Enter a search term
    search_variable = input(f'Enter the search term for {file_variable} file: ')
    search_variable = search_variable.title() 

    # Define the search function
    def find(file_variable, search_variable):
        with open(file_variable, 'r') as file:
            content = file.read()

            if search_variable in content:
                print(f'Your search term "{search_variable}" exists in the {file_variable} file!')
                see_entries = input('Would you like to see the entries (y or n)? ')

                if see_entries.lower() == 'y':
                    print(f'Here are all the entries with the term "{search_variable}":')
                    with open(file_variable, 'r') as file:
                        for line in file:
                            if search_variable in line:
                                print(line.strip())

                elif see_entries.lower() == 'n':
                    print('Goodbye')
                    sys.exit()

                else:
                    print("Invalid option. Please enter 'y' or 'n'.")
            else:
                print(f'{search_variable} does not exist in {file_variable}.')

    # Call the function
    find(file_variable, search_variable)

        