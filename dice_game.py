import doctest
import random

def dice_roll():
    ''' (none) -> int
    This function rolls two dice and returns the sum of them.
    >>> random.seed(82)
    >>> dice_roll()
    6
    >>> dice_roll()
    8
    >>> random.seed(1)
    >>> dice_roll()
    7
    >>> dice_roll()
    4
    '''
    #Each dice is rolled by generating a random integer between 1 and 6.
    first_dice = random.randint(1,6)
    second_dice = random.randint(1,6)
    #The sum of the numbers rolled is returned.
    return first_dice + second_dice

def second_stage(n):
    ''' (int) -> int
    This function computes the second stage. This function keeps rolling the dice
    until they make up 7 or the input value n. All values it rolls are printed out
    for the user. Whichever of these two the function ends up with is returned to
    the user.
    >>> random.seed(555)
    >>> r = second_stage(10)
    5 4 11 3 7
    >>> r
    7
    >>> random.seed(32)
    >>> r = second_stage(5)
    3 5
    >>> r
    5
    >>> r = second_stage(8)
    8
    >>> r
    8
    '''
    #we set the initial value of n_or_7 to 0.
    n_or_7 = 0
    #The while loop runs until n_or_7 becomes n or 7.
    while n_or_7 != n and n_or_7 != 7:
        #The value of n_or_7 is set to the value of a dice roll.
        n_or_7 = dice_roll()
        #The value rolled is printed.
        print(n_or_7, end = ' ')
    #This print statement is added just so the next statement printed will go on a
    #new line.
    print()
    #The final value of n_or_7 is returned.
    return n_or_7

def can_play(player_bank, player_bet):
    ''' (float, float) -> bool
    This function returns whether or not a player has enough money to place their
    desired bet and whether or not their desired bet is valid.
    >>> can_play(3.00, 1.00)
    True
    >>> can_play(1.00, 3.00)
    False
    >>> can_play(12456765432.04987543, 0.00)
    False
    >>> can_play(4444444.44444, -3.333)
    False
    '''
    #If the player wants to bet less than 0, false is returned.
    if player_bet <= 0:
        return False
    #If the player doesn't have enough money to make their bet, false is returned.
    elif player_bet > player_bank:
        return False
    #If the player has enough money to make their bet, true is returned.
    elif player_bet <= player_bank:
        return True
    #If none of the above conditions are satisfied, an AssertionError is raised,
    #because it means I made a mistake in my code here.
    else:
        return AssertionError

def pass_line_bet(player_bank, player_bet):
    ''' (float, float) -> float
    This function rolls the dice. It prints out whether the player win, loses, or has
    to roll again. If they have to roll again, it uses the second stage function to
    determine what the final number will be. It then tells the player if they won or
    lost. The player's amount of money after winning or losing their bit is what is
    returned.
    >>> random.seed(18)
    >>> m = pass_line_bet(10.0, 5.0)
    A 3 has been rolled. You lose!
    >>> m
    5.0
    >>> m = pass_line_bet(127.27, 127.27)
    A 10 has been rolled. Roll again!
    5 6 10
    You win!
    >>> m
    254.54
    >>> m = pass_line_bet(21.4, 0.4)
    A 6 has been rolled. Roll again!
    7
    You lose. :(
    >>> m
    21
    '''
    #The value of the first roll is found with the dice_roll function.
    first_roll = dice_roll()
    #If the first roll is 7 or 11, the player is told they won and their new balance
    #is returned to them.
    if first_roll == 7 or first_roll == 11:
        print("A " + str(first_roll) + " has been rolled. You win!")
        return player_bank + player_bet
    #If the first roll is 2, 3, or 12, the player is told they lost and their new
    #balance is returned to them.
    elif first_roll == 2 or first_roll == 3 or first_roll == 12:
        print("A " + str(first_roll) + " has been rolled. You lose!")
        return player_bank - player_bet
    #Otherwise, the player is told they must roll again.
    else:
        print("A " + str(first_roll) + " has been rolled. Roll again!")
        #The final value of the second roll is found using second_stage.
        second_roll = second_stage(first_roll)
        #If both of their rolls have the same value, the player is told they won and
        #their new balance is returned.
        if second_roll == first_roll:
            print("You win!")
            return player_bank + player_bet
        #If the second stage returns 7, the player is told they lost and their new
        #balance is returned.
        elif second_roll == 7:
            print("You lose. :(")
            return player_bank - player_bet

def play():
    ''' (none) -> void
    This function plays a hand of the game. It takes input for how much money the
    player has and how much they will be betting. It then plays the hand and tells
    the player what's happening along the way.
    (No doctests because I'm lazy.)
    '''
    #The user is prompted to input the amount of money they have and how much they're
    #betting.
    player_bank = float(input("How much money do you have?: "))
    player_bet = float(input("How much of that would you like to bet?: "))
    #If the player can play, pass_line_bet is used to go through the parts of the
    #game. Their new balance after the hand is printed.
    if can_play(player_bank, player_bet):
        player_bank = pass_line_bet(player_bank, player_bet)
        #The amount of money in the player's bank is multipled by 100 and turned into
        #an int, cutting off every decimal. This int is then converted back into a
        #float and divided by 100. It is finally converted to a string so it can be
        #concatenate to print.
        print("You now have $" + str(float(int(player_bank*100))/100))
    else:
        #If a player didn't meet the monetary critera for playing, they are told that
        #they provided insufficient funds.
        print("Insufficient funds. You cannot play.")

if __name__ == '__main__':
    doctest.testmod()
    play()
    