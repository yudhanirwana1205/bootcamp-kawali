transaction = []


def add_transaction(transaction, user, amount, type, to='self'):
    transaction.append({
        'user': user,
        'to': to,
        'amount': amount,
        'type': type
    })


def withdraw(accounts, user, amount):
    for a in accounts:
        if a['user'] == user:
            if a['balance'] >= amount:
                a['balance'] -= amount
                print('Withdraw success')
                add_transaction(transaction, user, amount, 'withdraw')
                return True
            else:
                print('Insufficient balance')
                return False
    else:
        print('User not found')
        return False


def deposit(accounts, user, amount):
    for a in accounts:
        if a['user'] == user:
            a['balance'] += amount
            print('Deposit success')
            add_transaction(transaction, user, amount, 'deposit')
            return True
    else:
        print('User not found')
        return False


def transfer(accounts, user, amount, to):
    for a in accounts:
        if a['user'] == user:
            if a['balance'] >= amount:
                for b in accounts:
                    if b['user'] == to:
                        a['balance'] -= amount
                        b['balance'] += amount
                        add_transaction(transaction, user, amount, 'transfer', to)
                        print('Transfer success')
                        return True
                else:
                    print('User not found')
                    return False

            else:
                print('Insufficient balance')
                return False
    else:
        print('User not found')
        return False


def show_balance(accounts, user):
    for a in accounts:
        if a['user'] == user:
            print('Balance: ', a['balance'])
            return True
    else:
        print('User not found')
        return False


def show_transaction(transaction, user):
    user_found = False
    for t in transaction:
        if t['user'] == user:
            user_found = True
            print(t)
    if not user_found:
        print('User not found')


def show_transaction_prompt(transaction):
    while True:
        user = input('Username: ')
        show_transaction(transaction, user)
        break


def transfer_prompt(accounts, current_user):
    while True:
        to = input('To: ')
        amount = int(input('Amount: '))

        if not transfer(accounts, current_user['user'], amount, to):
            print('Transfer failed')
            break
        else:
            print('Transfer success')
            break


def withdraw_prompt(accounts, current_user):
    while True:
        amount = int(input('Amount: '))
        if withdraw(accounts, current_user['user'], amount):
            break


def deposit_prompt(accounts, current_user):
    while True:
        amount = int(input('Amount: '))
        if deposit(accounts, current_user['user'], amount):
            break
