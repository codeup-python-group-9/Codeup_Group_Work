def view_current_balance(list_of_transactions):
    # choice 1
    balance = 0
    for i in range(0,(len(list_of_transactions))):
        balance += float(list_of_transactions[i][1])
    print(f'Your balance is ${balance:.2f}.')
    print()


def record_withdrawal(all_transactions, list_of_transactions, transaction_number):
    # choice 2
    transaction_number += 1
    debit_input = input('How much is the withdrawal? ')
    # check for valid debit
    debit_parts = ''.join(debit_input.split('.'))
    while not debit_parts.isdigit() or int(debit_parts) <= 0:
        debit_input = input('Please re-enter your withdrawal, using only digits: ')

    # format the debit amount 
    if debit_parts[0] == '-':
        debit_parts = debit_parts[1:]
    debit = float(debit_input)
    debit_string = str(debit)
    if debit_string[-2] == '.':
        debit_string += '0'
    
    category = input('What category would you like to enter for your withdrawal (1-9)? ')
    while not category.isdigit() or int(category) < 1 or int(category) > 9:
        category = input('Please enter a valid category (1, 2, 3, 4, 5, 6, 7, 8, or 9): ')

    day = datetime.datetime.now().strftime("%Y/%m/%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    # add to lists for code calculations
    this_transaction = []
    this_transaction.append(str(transaction_number)+'\t')
    this_transaction.append('-'+debit_string+'\t') 
    this_transaction.append(category+'\t')
    this_transaction.append(day+'\t')
    this_transaction.append(time+'\n')
    all_transactions.append(this_transaction)
    list_of_transactions.append(this_transaction)
 
    # create a string to write to the text file
    this_transaction_for_file = str(transaction_number)+'\t' + '-'+debit_string+'\t'+ category+'\t' + day+'\t' + time+'\n'

    with open('random_data_python_group_project.txt', 'a') as f:
        f.write(str(this_transaction_for_file))

    print(f'${debit_string} has been withdrawn from your account.')
    print()

    return transaction_number


def record_deposit(all_transactions, list_of_transactions, transaction_number):
    # choice 3
    transaction_number += 1
    credit_input = input('How much is the deposit? ')
    # check for valid deposit
    credit_parts = ''.join(credit_input.split('.'))
    while not credit_parts.isdigit() or int(credit_parts) <= 0:
        credit_input = input('Please re-enter your deposit, using only digits: ')
    
    # format the credit amount 
    if credit_parts[0] == '-':
        credit_parts = credit_parts[1:]
    credit = float(credit_input)
    credit_string = str(credit)
    if credit_string[-2] == '.':
        credit_string += '0'

    category = '10'

    day = datetime.datetime.now().strftime("%Y/%m/%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    # add to lists for code calculations
    this_transaction = []
    this_transaction.append(str(transaction_number)+'\t')
    this_transaction.append(credit_string+'\t') 
    this_transaction.append(category+'\t')
    this_transaction.append(day+'\t')
    this_transaction.append(time+'\n')
    all_transactions.append(this_transaction)
    list_of_transactions.append(this_transaction)

    # create a string to write to text file
    this_transaction_for_file = str(transaction_number)+'\t' + credit_string+'\t'+ category+'\t' + day+'\t' + time+'\n'

    with open('random_data_python_group_project.txt', 'a') as f:
        f.write(str(this_transaction_for_file))

    print(f'${credit_string} has been deposited into your account.')
    print()

    return transaction_number

def print_transactions_in_selected_range(list_of_transactions, input_date_min, input_date_max):
    date_min = int(input_date_min.replace('/',''))
    date_max = int(input_date_max.replace('/',''))

    your_date_range = []
    count = 0
    for row_num in range(len(list_of_transactions)):
        this_rows_date = int(list_of_transactions[row_num][3].replace('/',''))
        if (this_rows_date >= date_min) and (this_rows_date <= date_max):
            this_row = list_of_transactions[row_num]
            your_date_range.append(this_row)
            count += 1
    print()

    if count == 0:
        print(f'There were no transactions between {input_date_min} and {input_date_max}.')
    else:
        print(f'There were {count} transactions between {input_date_min} and {input_date_max}:')
        print()
        for row_num in range(len(your_date_range)):
            for i in range(5):
                if i == 1:
                    if your_date_range[row_num][1][0] == '-':
                        print(f'-${your_date_range[row_num][1][1:]}\t', end='')
                    else:
                        print(f'${your_date_range[row_num][1]}\t', end='')
                    if len(your_date_range[row_num][1]) < 7:
                        print('\t', end='')
                else:
                    print(f'{your_date_range[row_num][i]}\t', end='')
            print()
        print()

def date_search(list_of_transactions):
    input_date_min = input('With what date would you like to start (YYYY/MM/DD): ')
    date_min = int(input_date_min.replace('/',''))
    input_date_max = input('What is your end date (YYYY/MM/DD): ')
    date_max = int(input_date_max.replace('/',''))

    while date_min >= date_max:
        print('Please make sure your end date is not before your start date.')
        input_date_min = input('With what date would you like to start (YYYY/MM/DD): ')
        date_min = int(input_date_min.replace('/',''))
        input_date_max = input('What is your end date (YYYY/MM/DD): ')
        date_max = int(input_date_max.replace('/',''))

    print_transactions_in_selected_range(list_of_transactions, input_date_min, input_date_max)

def print_all_transactions(list_of_transactions):
    dates = []
    for entry in list_of_transactions:
        dates.append(entry[3])
    
    input_date_min = min(dates)
    input_date_max = max(dates)

    print_transactions_in_selected_range(list_of_transactions, input_date_min, input_date_max)
    print(f'Those are all transactions between {input_date_min} and {input_date_max}.')
    print()

# # @@@@@@@ MAIN @@@@@@@@
import time
import datetime
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

dates_of_transactions = []

for trans in list_of_transactions:
    dates_of_transactions.append(trans[-2])



# category_sample = ['2','3','4','5','8','3','9','3','8','4','2','9','4','8','2','7']
# int_category_sample = []
# for category in category_sample:
#     int_category_sample.append(int(category))

# print(int_category_sample)

# def category_search(int_category_sample):
#     user_category = input('What category would you like to search, 1-10: ')
#     user_category_input = int(user_category)
#     user_category_input_int = []
#     for category in int_category_sample:
#         if user_category_input in int_category_sample:
#             user_category_input_int.append(user_category_input)
#     print(user_category_input_int)


print('~~~ Welcome to your terminal checkbook! ~~~')
print()
again = True
while again:
    print('What would you like to do?')
    print('1) view current balance')
    print('2) record a debit (withdraw)')
    print('3) record a credit (deposit)')
    print('4) view transactions within a range of dates')
    print('5) view all transactions')
    print('6) exit')
        
    choice_input = input('Your choice? ')
        
    if not choice_input.isdigit() or (int(choice_input) < 1 or int(choice_input) > 6):
        print('Invalid choice.')
        print('Please enter a 1, 2, 3, 4, 5, or 6.')
    else:
        choice = int(choice_input)
        if choice == 6:
            again = False
            print()
        else:
            if choice == 1:
                view_current_balance(list_of_transactions)
            elif choice == 2:
                transaction_number = record_withdrawal(all_transactions, list_of_transactions, transaction_number)
            elif choice == 3:
                transaction_number = record_deposit(all_transactions, list_of_transactions, transaction_number)
            elif choice == 4:
                date_search(list_of_transactions)
            elif choice == 5:
                print_all_transactions(list_of_transactions)
            # elif choice == 6:
            #     category_search(category_sample)

print('Thanks, have a great day!')

