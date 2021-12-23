import requests
import subprocess 

def generate_password () :
    print('')
    numbers = input('Do you want numbers in your password [Y/N]: ')
    char = input('Do you want to special charchters in your password [Y/N]: ')
    caps = input('Do you want CAPITAL letters in your password [Y/N]: ')
    length = input('Enter the length of your password: ')
    
    if numbers.lower() == 'y':
        IS_NUMBER = True
    else:
        IS_NUMBER = False

    if char.lower() == 'y':
        IS_CHAR = True
    else:
        IS_CHAR = False

    if caps.lower() == 'y':
        IS_CAPS = True
    else:
        IS_CAPS = False

    if IS_NUMBER and IS_CAPS and IS_CHAR:
        request = requests.get(f'https://passwordinator.herokuapp.com/generate?num=true&char=true&caps=true&len={length}')
        password = request.json()['data']
    elif IS_NUMBER == True and IS_CAPS == False and IS_CHAR == False:
        request = requests.get(f'https://passwordinator.herokuapp.com/generate?num=true&len={length}')
        password = request.json()['data']
    elif IS_NUMBER == False and IS_CAPS == True and IS_CHAR == False:
        request = requests.get(f'https://passwordinator.herokuapp.com/generate?caps=true&len={length}')
        password = request.json()['data']
    elif IS_NUMBER == False and IS_CAPS == False and IS_CHAR == True:
        request = requests.get(f'https://passwordinator.herokuapp.com/generate?char=true&len={length}')
        password = request.json()['data']
    elif IS_NUMBER == True and IS_CAPS == True and IS_CHAR == False:
        request = requests.get(f'https://passwordinator.herokuapp.com/generate?num=true&caps=true&len={length}')
        password = request.json()['data']
    elif IS_NUMBER == False and IS_CAPS == True and IS_CHAR == True:
        request = requests.get(f'https://passwordinator.herokuapp.com/generate?char=true&caps=true&len={length}')
        password = request.json()['data']
    elif IS_NUMBER == True and IS_CAPS == False and IS_CHAR == True:
        request = requests.get(f'https://passwordinator.herokuapp.com/generate?num=true&char=true&len={length}')
        password = request.json()['data']
    elif IS_NUMBER == False and IS_CAPS == False and IS_CHAR == False:
        request = requests.get(f'https://passwordinator.herokuapp.com/generate?len={length}')
        password = request.json()['data']

    subprocess.run("clip", universal_newlines=True, input=password)

    print('')
    print('-' * 40)
    print(f'The generated password is: {password}')
    print(f'Contains Numbers: {IS_NUMBER}')
    print(f'Contains Special Charachters: {IS_CHAR}')
    print(f'Contains Capital Letters: {IS_CAPS}')
    print('The password has been copied to your clipboard')
    print('-' * 40)
    print('')

def check_password (password):

    IS_SECURE = True

    file1 = open('password_list.txt', 'r')
    Lines = file1.readlines()
    
    for line in Lines:
        if line.strip() == password:
            IS_SECURE = False
            break
        else:
            continue
    
    if IS_SECURE:
        print('')
        print('-' * 40)
        print('Your password WAS NOT FOUND IN A PASSWORD LIST.')
        print('-' * 40)
        print('')
    else:
        print('')
        print('-' * 40)
        print(f'Your password: {password} is FOUND IN A PASSWORD LIST.')
        print('-' * 40)
        print('')