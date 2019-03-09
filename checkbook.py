def view_current_balance(list_of_transactions):
    # choice 1
    balance = 0
    for i in range(0,(len(list_of_transactions))):
        balance += float(list_of_transactions[i][1])
    print(f'Your balance is ${balance:.2f}.')
    print()


def record_withdrawal(all_transactions, transaction_number):
    # choice 2
    transaction_number += 1
    debit_input = input('How much is the withdrawal? ')
    # check for valid debit
    debit_parts = ''.join(debit_input.split('.'))
    while not debit_parts.isdigit() or int(debit_parts) <= 0:
        debit_input = input('Please re-enter your withdrawal, using only digits: ')
    
    category = input('What category would you like to enter for your withdrawal (1-9)? ')
    while not category.isdigit() or int(category) < 1 or int(category) > 9:
        category = input('Please enter a valid category (1, 2, 3, 4, 5, 6, 7, 8, or 9): ')
    print()

    day = datetime.datetime.now().strftime("%Y/%m/%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    this_transaction = str(str(transaction_number)+'\t' +'-'+debit_input+'\t' +category+'\t' + day+'\t' + time+'\n')
    all_transactions.append(this_transaction)

    with open('random_data_python_group_project.txt', 'a') as f:
        f.write(str(this_transaction))



def record_deposit(all_transactions, transaction_number):
    # choice 3
    transaction_number += 1
    credit_input = input('How much is the deposit? ')
    # check for valid deposit
    credit_parts = ''.join(credit_input.split('.'))
    while not credit_parts.isdigit() or int(credit_parts) <= 0:
        credit_input = input('Please re-enter your deposit, using only digits: ')
    print()
    
    category = '10'

    day = datetime.datetime.now().strftime("%Y/%m/%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    this_transaction = str(str(transaction_number)+'\t' + credit_input+'\t' +category+'\t' + day+'\t' + time+'\n')
    all_transactions.append(this_transaction)

    with open('random_data_python_group_project.txt', 'a') as f:
        f.write(str(this_transaction))



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


update = []
for date in dates_of_transactions:
    update.append(int(date.replace('/','')))

def date_search(update):
    input_date_min = input('What date would you like to start with? Enter as YYYY/MM/DD: ')
    date_min = int(input_date_min.replace('/',''))
    print('Your start date is '+str(date_min))
    input_date_max = input('What is your end date:  Enter as YYYY/MM/DD: ')
    date_max = int(input_date_max.replace('/',''))
    your_date_range = []
    for date in update:
        if date >= date_min and date <= date_max:
            your_date_range.append(date)
    print(your_date_range)

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
    print('4) exit')
        
    choice_input = input('Your choice? ')
        
    if not choice_input.isdigit() or (int(choice_input) < 1 or int(choice_input) > 6):
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
            elif choice == 5:
                date_search(update)
            # elif choice == 6:
            #     category_search(category_sample)

print('Thanks, have a great day!')

