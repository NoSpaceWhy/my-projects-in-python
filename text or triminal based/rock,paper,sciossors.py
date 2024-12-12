import random 

print("This is a game of rock,paper,scissors")

Computer_win = 0
player_win = 0

option = ['rock', 'paper', 'scissors']

while True:
    print("Enter your choice: rock/paper/scissors or Q to quit.")
    player_choice = input().lower()
    
    if player_choice in ['q', 'quit']:
            print(f"Final Score: Player: {player_win}, Computer: {Computer_win}")
            quit()
        
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid Input")
        continue
    else:
        
        random_num = random.randint(0,2)
        # converts a int into rock or paper or scissors
        #rock: 0 paper: 1 scissors: 2
        Computer_turn = option[random_num]
        
        print(f"Computer chose: {Computer_turn}")
        if True:
            if player_choice == Computer_turn:
                print("It's a tie!")
            elif (player_choice == "rock" and Computer_turn == "scissors"):
                print("You won!")
                player_win += 1
            elif (player_choice == "scissors" and Computer_turn == "paper"):
                print("You won!")
                player_win += 1
            elif (player_choice == "paper" and Computer_turn == "rock"):
                print("You won!")
                player_win += 1
            else:
                print("Computer won!")
                Computer_win += 1
                
        else:
            print("Invalid input")
            continue 