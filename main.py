from functions import *

menu = '''
1. Check your password.
2. Generate a new password.
3. QUIT.
'''

def main ():
    print('-' * 40)
    print(menu)
    print('-' * 40)
    print('')

    user_option = int(input('> '))

    if user_option == 1:
        print('')
        password = input('Enter password to check: ')
        check_password(password)
        main()
    elif user_option == 2:
        generate_password()
        main()
    else:
        exit()

main()