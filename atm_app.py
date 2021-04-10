# Improve on your ATM mockup from last course to include the following:

# 1. Use functions
#
# 2. Include register, and login
#
# 3. Generate Account Number
#
# 4. Any other improvement you can think of(extra point) ---> Set Password During Registration and Change Password
# after login if you want while you login with the new set password


import random
from datetime import datetime
today = datetime.now().strftime('%c')

database = {
    1234567890: {
        'first_name': 'admin',
        'last_name': 'admin',
        'email': 'admin@email.com',
        'password': 1234
    },
    1111111111: {
        'first_name': 'Seyi',
        'last_name': 'Onifade',
        'email': 'seyi@zuri.team',
        'password': 0000
    }
}

accounts = [1234567890, 1111111111]

def login():
    login_details_valid = False
    while not login_details_valid:
        try:
            login.acc_num = int(input('Enter your account number\n'))
            try:
                password = int(input('Enter your password\n'))
                if login.acc_num in database and database[login.acc_num]['password'] == password:
                    print(f"Successfully Logged In {database[login.acc_num]['last_name'].capitalize()}"
                          f" {database[login.acc_num]['first_name'].capitalize()}")
                    print(f'Your Bank Details is {database[login.acc_num]}')
                    login_details_valid = True
                    print('What would you like to do?\n1. Withdrawal\n2. Cash deposit\n3. Complaints\n4. Change Password')
                    try:
                        login.banking_option = int(input('Enter a number to perform an operation\n'))
                        if login.banking_option == 1:
                            withdrawal()
                        elif login.banking_option == 2:
                            cash_deposit()
                        elif login.banking_option == 3:
                            complaint()
                        elif login.banking_option == 4:
                            change_password()
                        else:
                            print('Wrong input, Try again!!!')
                            continue
                    except:
                        print('Only Numbers shown as options are allowed\nAlphabeths are not allowed\nTry Again')
                        continue

                else:
                    print('Wrong log in details')
                    continue
            except:
                print('Only Numbers shown as options are allowed\nAlphabeths are not allowed\nTry Again')
                continue
        except:
            print('Only account number is expected, you might have introduced a string')
            continue


def generate_acc_num():
    acc_num_duplicate = False
    while not acc_num_duplicate:
        acc_num = random.randrange(1111111111, 9999999999)
        if acc_num not in accounts:
            print('Account Number Issued')
            acc_num_duplicate = True
        else:
            continue
    return acc_num



def set_password():
    print('Please set a password for your account')
    password_valid = False
    while not password_valid:
        try:
            password = int(input('Set Password \nEnter 4 digit pin: \n'))
            try:
                confirm_password = int(input('Confirm Password \n'))
                if len(str(password)) == 4 and len(str(confirm_password)) == 4:
                    if password == confirm_password:
                        print('Password Set Successfully')
                        confirmed_password = confirm_password
                        password_valid = True
                    else:
                        print('Password doesn\'t match')
                        continue
                else:
                    print('Only enter four digit numbers for your new password!!!')
                    continue
            except:
                print('Wrong input, please enter a 4 digit number')
        except:
            print('Wrong input, please enter a 4 digit number')


    return confirmed_password


def register():
    first_name = input('Enter your first name: \n')
    last_name = input('Enter your last name: \n')
    email = input('Enter your email: \n')
    account_num = generate_acc_num()
    password = set_password()
    accounts.append(account_num)
    database[account_num] = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password
    }
    print(f'Your Account Number is {account_num}\nlogin with your account number')
    login()


def withdrawal():
    print(f'You selected {login.banking_option}')
    withdrawal_amt = input('How much would you like to withdraw? : ')
    print('Take your cash')


def cash_deposit():
    current_balance = 0
    print(f'You selected {login.banking_option}')
    try:
        cash_deposit = int(input('How much would you like to deposit? :'))
        current_balance += cash_deposit
        print(f'Current Account Balance is ${current_balance}')
    except:
        print('wrong input, try again')


def complaint():
    print(f'You selected {login.banking_option}')
    complaint = input('What issue will you like to report? - ')
    print('Thank you for contacting us!')


def change_password():
    print(f"Your Old Password{database[login.acc_num]['password']} ")
    password_valid = False
    while not password_valid:
        try:
            new_password = int(input('Change password \nEnter 4 digit pin: \n'))
            try:
                confirm_password = int(input('Confirm password \n'))
                if len(str(new_password)) == 4 and len(str(confirm_password)) == 4:
                    if new_password == confirm_password:
                        database[login.acc_num]['password'] = new_password
                        print('Password changed successfully')
                        print(database[login.acc_num])
                        print('You can log in with your new password!!!')
                        password_valid = True

                    else:
                        print('Password doesn\'t match')
                        continue
                else:
                    print('Only enter four digit numbers for your new password!!!')
                    continue
            except:
                print('wrong input, please enter a 4 digit number')
        except:
            print('Wrong input, please enter a 4 digit number')
    login()


def init():
    print('Welcome to Zuri Bank Plc')
    print(f'Present Date and Time: {today}')

    while True:
        print('Do you have an account with us?\n1. Yes\n2. No ')
        try:
            selected_option1 = int(input('Enter a number as your answer:\n'))
            if selected_option1 == 1:
                print('Would you like to log in?\n1. Yes\n2. No')
                selected_option2 = int(input('Enter a number as your answer:\n'))
                if selected_option2 == 1:
                    login()
                    break
                elif selected_option2 == 2:
                    print('Thanks for banking with us!!!, See you soon')
                    break
                else:
                    print('Wrong input,Please enter option numbers 1 or 2. Try Again!!!')
                    break
            elif selected_option1 == 2:
                print('Would you like to start banking with us?\n1. Yes\n2. No')
                selected_option3 = int(input('Enter a number as your answer:\n'))
                if selected_option3 == 1:
                    print('*******************Register********************')
                    print('Please Register to start banking with us')
                    register()
                    break
                elif selected_option3 == 2:
                    print('Uh Oh!!!...\nHope you change your mind\nSee you soon')
                    break
                else:
                    print('Wrong input,Please enter option numbers 1 or 2. Try Again!!!')
                    break
            else:
                print('Wrong input,Please enter option numbers 1 or 2. Try Again!!!')
                break
        except:
            print('Only Numbers shown as options are allowed\nTry Again')
            init()


init()