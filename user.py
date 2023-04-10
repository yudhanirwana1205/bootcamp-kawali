from file_ops import write_to_file, read_file

_USER_FILE = './users.txt'
_ACCOUNT_FILE = './accounts.txt'

users = [
    {
        'user': '',
        'password': '1234',
        'role': 'admin'
    }
]

accounts = []

current_user = {}


def add_user(users, user, password, role):

    for u in users:
        if u['user'] == user:
            print('User already exist')
            return False
    else:
        users.append({
            'user': user,
            'password': password,
            'role': role
        })
        print('User added')
        write_to_file(_USER_FILE, users)
        return True


def show_user(users):
    for u in users:
        print('User: ', u['user'], 'Role: ', u['role'])


def add_user_prompt(users, accounts):
    while True:
        user = input('Username: ')
        password = input('Password: ')
        role = input('Role (1: admin, 2: customer): ')
        if int(role) == 1:
            role = 'admin'
        elif int(role) == 2:
            role = 'customer'
        else:
            print('Role must be 1 or 2')
            continue
        if role == 'admin' or role == 'customer':
            if add_user(users, user, password, role):
                add_account(accounts, user)
            break
        else:
            print('Role must be admin or customer')


def add_account(accounts, user, balance=0):
    accounts.append({
        'user': user,
        'balance': balance
    })
    write_to_file(_ACCOUNT_FILE, accounts)


def delete_account(accounts, user):
    for a in accounts:
        if a['user'] == user:
            accounts.remove(a)
            print('Account deleted')
            return True
    else:
        print('Account not found')
        return False


def delete_user(users, user):
    for u in users:
        if u['user'] == user:
            users.remove(u)
            print('User deleted')
            return True
    else:
        print('User not found')
        return False


def delete_user_prompt(users):
    while True:
        user = input('Username: ')
        if delete_user(users, user):
            delete_account(accounts, user)
            break


user_file = read_file(_USER_FILE)
if user_file:
    users.clear()
    users = user_file
