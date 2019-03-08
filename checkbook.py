def view_current_balance(list_of_transactions):
    # choice 1
    balance = 0
    for i in range(0,len(list_of_transactions)):
        balance += float(list_of_transactions[i][1])
    print(f'Your balance is ${balance:.2f}.')
    print()


def record_withdrawal(all_transactions, transaction_number):
    # choice 2
    transaction_number += 1
    debit_input = input('How much is the withdrawal? ')
    # check for valid debit
    while not debit_input.isdigit() or int(debit_input) <= 0:
        debit_input = input('Please re-enter your withdrawal, using only digits: ')
    debit = float(debit_input)
    print(f'You entered ${debit:.2f}.')
    print()


def record_deposit(all_transactions, transaction_number):
    # choice 3
    transaction_number += 1
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

all_transactions = whole_file[1:]

list_of_transactions = []

for trans in all_transactions:
    list_of_transactions.append(trans.split('\t'))

holder = list_of_transactions[len(list_of_transactions)-1][0]
transaction_number = int(holder)

print('~~~ Welcome to your terminal checkbook! ~~~')
print()
again = True
while again:
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
                view_current_balance(list_of_transactions)
            elif choice == 2:
                record_withdrawal(list_of_transactions, transaction_number)
            elif choice == 3:
                record_deposit(list_of_transactions, transaction_number)

print('Thanks, have a great day!')