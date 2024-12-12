import random

score = 0

game_active = True
comand_line = '>'


print(f"{comand_line}Hello, Wellcome to a Game of chance.")
print(f"{comand_line}Type 'help'. ")

while game_active:
    cmd = input(f"{comand_line}").lower()
    if cmd not in ["help", "quit", "stop", "rules", "start"]:
            print(f"{comand_line}Error, No command like that.")
    
    else:
        if cmd == 'help':
            print(f"{comand_line}These are the command you can use.\n{comand_line}Rules - To know the Rules.\n{comand_line}Start - to start the Real game.\n{comand_line}Quit/Stop - to Leave the game.")
        elif cmd in ['quit', 'stop']:
            exit()
        elif cmd == 'rules':
            print(f'{comand_line}If you get 1 you will lose all points.')
        elif cmd == 'start':
            print(f"{comand_line}Let's GO")
            break
        
while True:
    
    random_num = random.randint(1,6)
    
    print(f"{comand_line}You rolled {random_num}")
    
    if random_num == 1:
        print(f"{comand_line}You lost, you did't win this might have been your score {score}")
        exit()
    else:
        score += random_num
        print(f"{comand_line}Your current score is {score}")
        
        while True:    
            player_want_to_play = input(f"{comand_line}Do you want to continue?\n>").lower()
            
            if player_want_to_play in ["yes", "no"]: 
                      
                if player_want_to_play == 'yes':
                    break
                elif player_want_to_play == 'no':
                    print(f"{comand_line}This is your score {score}")
                    exit()
            else:
                print(">Invalid input type 'yes' or 'no'.")
                continue