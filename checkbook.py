with open('random_data_python_group_project.txt') as transactions:
    customers_file = transactions.readlines()
headings = customers_file[0]
print(headings)

customers = customers_file[1:]
for cust in customers[:3]:
    print(cust)



# def view_current_balance(customer_id):
#     # choice 1
#     print('Your current balance is $50.00')
#     print()


# def record_withdrawal(customer_id):
#     # choice 2
#     debit_input = input('How much is the withdrawal? ')
#     # check for valid debit
#     while not debit_input.isdigit() or int(debit_input) <= 0:
#         debit_input = input('Please re-enter your withdrawal, using only digits: ')
#     debit = float(debit_input)
#     print(f'You entered ${debit:.2f}.')
#     print()


# def record_deposit(customer_id):
#     # choice 3
#     credit_input = input('How much is the deposit? ')
#     # check for valid deposit
#     while not credit_input.isdigit():
#         credit_input = input('Please re-enter your debit, using only digits: ')
#     credit = float(credit_input)
#     print(f'You entered ${credit:.2f}.')
#     print()


# # @@@@@@@ MAIN @@@@@@@@
# customer_id = '123'

# print('~~~ Welcome to your terminal checkbook! ~~~')
# print()
# again = True
# while again:
#     choice_input = '4'
#     print('What would you like to do?')
#     print('1) view current balance')
#     print('2) record a debit (withdraw)')
#     print('3) record a credit (deposit)')
#     print('4) exit')
        
#     choice_input = input('Your choice? ')
        
#     if not choice_input.isdigit() or (int(choice_input) < 1 or int(choice_input) > 4):
#         print('Invalid choice.')
#         print('Please enter a 1, 2, 3, or 4.')
#     else:
#         choice = int(choice_input)
#         if choice == 4:
#             again = False
#         else:
#             if choice == 1:
#                 view_current_balance(customer_id)
#             elif choice == 2:
#                 record_withdrawal(customer_id)
#             elif choice == 3:
#                 record_deposit(customer_id)

# print('Thanks, have a great day!')