from user import show_user, add_user_prompt, delete_user_prompt, users, current_user, accounts
from transactions import (show_balance, withdraw_prompt, deposit_prompt,
                          transfer_prompt, show_transaction_prompt, show_transaction,
                          transaction)


def login(current_user, user, password):
    for u in users:
        if u['user'] == user and u['password'] == password:
            current_user.update(u)
            return True
    return False


def login_process(current_user):
    while True:
        user = input('Username: ')
        password = input('Password: ')
        if login(current_user, user, password):
            print('Login Success')
            break
        else:
            print('Login Failed')

# create menu function, if admin show admin menu, if customer show customer menu


def menu(current_user):
    if current_user['role'] == 'admin':
        while True:
            print('1. Add User')
            print('2. Delete User')
            print('3. Show Users')
            print('4. Show Transaction')
            print('5. Logout')
            choice = input('Choice: ')
            if choice == '1':
                add_user_prompt(users, accounts)
            elif choice == '2':
                delete_user_prompt(users)
            elif choice == '3':
                show_user(users)
            elif choice == '4':
                show_transaction_prompt(transaction)
            elif choice == '5':
                current_user.clear()
                break
    elif current_user['role'] == 'customer':
        while True:
            print('1. Show Balance')
            print('2. Withdraw')
            print('3. Deposit')
            print('4. Transfer')
            print('5. Show Transaction')
            print('6. Logout')
            choice = input('Choice: ')
            if choice == '1':
                show_balance(accounts, current_user['user'])
            elif choice == '2':
                withdraw_prompt(accounts, current_user)
            elif choice == '3':
                deposit_prompt(accounts, current_user)
            elif choice == '4':
                transfer_prompt(accounts, current_user)
            elif choice == '5':
                show_transaction(transaction, current_user['user'])
            elif choice == '6':
                current_user.clear()
                break


def main():
    while True:
        print('1. Login')
        print('2. Exit')
        choice = input('Choice: ')
        if choice == '1':
            login_process(current_user)
            menu(current_user)
        elif choice == '2':
            break
        print('\033c', end='')


main()
