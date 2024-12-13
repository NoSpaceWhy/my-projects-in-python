import random

def main_game():
    score = 0
    while True:
        
        # Ask for the number of rolls
        how_many_times = input('How many times do you want to roll? (Enter a number greater than 0)\n')
        
        if not how_many_times.isdigit() or int(how_many_times) <= 0:
            print("Please enter a valid number greater than zero")
            continue
            
        # Roll the dice
        for i in range(int(how_many_times)):
            
            random_num = random.randint(1, 6)  # Roll a dice (1 to 6)
            
            if random_num != 1:
                print(f'You rolled {random_num}')
                score += random_num
            else:
                print('You rolled a 1, you lost!!')
                print(f'Your final score is {score}')
                return
        
        print(f'Your score after {how_many_times} rolls is: {score}')
        
        # Ask if the player wants to continue
        go_on = input("Do you want to continue? (y/n): \n").lower()
        if go_on == 'n':
            print(f'Thanks for playing, your final score is {score}')
            break
        elif go_on != 'y':
            print('Invalid Input. Please type "y" or "n".\n \n \n')
            continue

def solo():
    main_game()

def two_player():
    player_1_score = 0
    player_2_score = 0
    while True:
        
        # Player 1 rolls
        random_num = random.randint(1, 6)
        how_many_times = input('How many times do does player 1 want to roll? (Enter a number greater than 0)\n')
        if not how_many_times.isdigit() or int(how_many_times) <= 0:
            print("Please enter a valid number greater than zero")
            continue
            
        if random_num!= 1:

            player_1_score += random_num
            print(f'Player 1 rolled {random_num}')
        else:
            print('Player 1 rolled a 1, Player 1 lost!!')
            print(f'Player 1 final score is {player_1_score}')
            print(f'Player 2 final score is {player_2_score}')
            return
        
        # Player 2 rolls
        how_many_times = input('How many times do does player 2 want to roll? (Enter a number greater than 0)\n')
        if not how_many_times.isdigit() or int(how_many_times) <= 0:
            print("Please enter a valid number greater than zero")
            continue
            
        random_num = random.randint(1, 6)
        if random_num!= 1:
            player_2_score += random_num
            print(f'Player 2 rolled {random_num}')
        else:
            print('Player 2 rolled a 1, Player 2 lost!!')

while True:
    # game starts here
    start = input('''
Welcome to PIG!
This is a 2-player game.
You can call your friend if you want
Or you can play solo.

The aim of the game is to roll the dice and try to get the highest score.
Rules:
- You can roll the dice as many times as you want.
- But if the dice rolls a 1, you lose.

How are you playing? (Enter 1 for solo or 2 for 2-player mode): 
    ''').lower()

    if start == '1' or start == 'solo':
        solo()
        break
    elif start == '2':
        two_player()
        break
    else:
        print('Invalid input, please choose 1 for solo or 2 for 2-player mode.')