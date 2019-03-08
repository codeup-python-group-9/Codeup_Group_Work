def view_current_balance(trans_by_field):
    # choice 1
    balance = 0
    for i in range(0,len(trans_by_field)):
        balance += float(trans_by_field[i][1])
    print(f'Your balance is ${balance:.2f}.')
    print()


def record_withdrawal(transactions):
    # choice 2
    debit_input = input('How much is the withdrawal? ')
    # check for valid debit
    while not debit_input.isdigit() or int(debit_input) <= 0:
        debit_input = input('Please re-enter your withdrawal, using only digits: ')
    debit = float(debit_input)
    print(f'You entered ${debit:.2f}.')
    print()


def record_deposit(transactions):
    # choice 3
    credit_input = input('How much is the deposit? ')
    # check for valid deposit
    while not credit_input.isdigit():
        credit_input = input('Please re-enter your debit, using only digits: ')
    credit = float(credit_input)
    print(f'You entered ${credit:.2f}.')
    print()


# @@@@@@@ MAIN @@@@@@@@
# read file of transaction and set up lists
with open('random_data_python_group_project.txt') as transactions_file:
    whole_file = transactions_file.readlines()
headings = whole_file[0]

transactions = whole_file[1:]

trans_by_field = []

for trans in transactions:
    trans_by_field.append(trans.split('\t'))

print('~~~ Welcome to your terminal checkbook! ~~~')
print()
again = True
while again:
    choice_input = '4'
    print('What would you like to do?')
    print('1) view current balance')
    print('2) record a debit (withdraw)')
    print('3) record a credit (deposit)')
    print('4) exit')
        
    choice_input = input('Your choice? ')
        
    if not choice_input.isdigit() or (int(choice_input) < 1 or int(choice_input) > 4):
        print('Invalid choice.')
        print('Please enter a 1, 2, 3, or 4.')
    else:
        choice = int(choice_input)
        if choice == 4:
            again = False
        else:
            if choice == 1:
                view_current_balance(trans_by_field)
            elif choice == 2:
                record_withdrawal(trans_by_field)
            elif choice == 3:
                record_deposit(trans_by_field)

print('Thanks, have a great day!')