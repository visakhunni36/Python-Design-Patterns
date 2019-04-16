

# python script

import command


# create the client object
user = command.Customer()

# invoke the place order command
print('Place Order Test')
user.order('CONFIRM')


# invoke the cancel order command
print('Cancel Order Test')
user.order('CANCEL')


# invalid command test
print('Invalid Command Test')
user.order('#$%')





































































