# Non-OOP
# Bank version 1
# Single Account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdraw')
    print('Press s to show the account')
    print()

    action = input('What do you want to do?')
    action = action.lower() # Force lowercase
    action = action[0] # Just use the first letter
    print()

    if action == 'b':
        print('Get Balance')
        userPassword = input('Please enter the password.')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print('Your balance is: ', accountBalance)

    elif action == 'd':
        print('Deposit')
        userDepositAmount = input('Please enter the amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        if userDepositAmount < 0:
            print('You cannot deposit a negative amount.')

        elif userPassword != accountPassword:
            print('Incorrect password')

        else:
            accountBalance = accountBalance + userDepositAmount
            print('Your new balance is: ', accountBalance)

    elif action == 's':
        print('Show')
        print('      Name', accountName)
        print('      Balance:', accountBalance)
        print('      Password:', accountPassword)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')

        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        if userWithdrawAmount < 0:
            print('You cannot withdraw a negative amount.')

        elif userPassword != accountPassword:
            print('Wrong password')

        elif userWithdrawAmount > accountBalance:
            print('Account balance to low.')

        else:
            accountBalance = accountBalance - userWithdrawAmount
            print('Your new balance is: ', accountBalance)

print('Done')