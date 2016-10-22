#name = raw_input('What is your name? ')
#print('Hi ' + name)
#name = raw_input('What is your name?')
#meal_cost = float(raw_input('How much was your meal?'))
#tip = meal_cost * .20
#total_price = meal_cost + tip

#print('You did not enter a valid option, defaulted to 20%')
#print('Your total cost would be $' + str(total_price))

meal_price = float(raw_input('How much was your meal? '))
print('How would you rate the service? ')
print('a. Not so good')
print('b. Good')
print('c. Excellent!')
chosen_option = raw_input('Choose an option: ')

# Here's where conditionals come in...
if chosen_option == 'a':
    percentage = .15;
elif chosen_option == 'b':
    percentage = .18;
elif chosen_option =='c':
    percentage = .20;
else:
    percentage = .20;

tip = meal_price * percentage
total_price = meal_price + tip
print('You should tip $' + str(tip))
print('Your total cost would be $' + str(total_price))
