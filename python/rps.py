# Parameters: a String `move`
# Returns: Boolean for whether move is valid
#
# Valid moves include 'rock', 'paper', or 'scissors'`
#
def check_move(move):

    print move = (move == 'rock' or move == 'paper' or move == 'scissors')# YOUR CODE GOES HERE

# Test the check_move function
print check_move('rock') # Expects: True
print check_move('paper') # Expects: True
print check_move('scissors') # Expects: True
print check_move('roc') # Expects: False
print check_move(1) # Expects: False
