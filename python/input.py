#name = raw_input('What is your name? ')
#print('Hi ' + name)
#name = raw_input('What is your name?')
meal_cost = float(raw_input('How much was your meal?'))
tip = meal_cost * .20
total_price = meal_cost + tip

print('You did not enter a valid option, defaulted to 20%')
print('Your total cost would be $' + str(total_price))
