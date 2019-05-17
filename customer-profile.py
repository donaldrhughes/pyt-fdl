customers = []

while True:
    customer = dict.fromkeys(['first', 'last', 'middle', 'address', 'email', 'phone'])

    customer['first'] = input('Enter your first name. ')
    customer['last'] = input('Enter your last name. ')
    customer['middle'] = input('Enter your middle name. ')
    customer['address'] = input('Enter your address. ')
    customer['email'] = input('Enter your email address. ')
    customer['phone'] = input('Enter your phone number. ')

    print('-' * 18)

    for key, value in customer.items():
        print("Customer\'s {0} is {1}. ".format(key, value))

    print('-' * 18)

    if input("Is your info correct? (Y/N) ").lower() == 'y':
        customers.append(customer)
        print(customer)

        if input ('Input another? (Y/N)').lower() == 'y':
            continue
        else:
            print('Customer Profile')

            print('-' * 18)

            for customer in customers:
                for key, value in customer.items():
                    print('Customer\'s {0} is {1}'.format(key, value))

            print('-' * 18)

            break