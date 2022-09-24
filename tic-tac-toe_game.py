#CSE-210, Week 2: Tic-Tac-Toe Game, Autor: Greis Michell Garcia Villanueva


class adding:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    OCEAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():

    turn=  adding.BLUE + 'X' + adding.ENDC
    count=0

    board_game_1=['1','2','3',
              '4','5','6',
              '7','8','9']

    keys=[]
    for key in board_game_1:
        keys.append(key)

    print('\n'+ adding.GREEN + 'Welcome to Tic-Tac-Toe Game' + adding.ENDC + '\n')
    while True:
        while True:
            the_board(board_game_1)
           
            move = input(f"{turn}'s your turn to choose a square by typing its number (choose wisely): ")
    
            try:
                move = int(move)
                move= move-1
                    
                if board_game_1[move] == '1' or board_game_1[move] == '2' or board_game_1[move] == '3' or board_game_1[move] == '4' or board_game_1[move] == '5' or board_game_1[move] == '6' or board_game_1[move] == '7' or board_game_1[move] == '8' or board_game_1[move] == '9':
                    board_game_1[move] = turn
                    count += 1
                else:
                    print(adding.MAGENTA + 'this place is unvalaible' + adding.ENDC)
                    continue
            
                #finding the winner
                if count >=5:
                    the_board(board_game_1)
                    #calling the fuction that set all posible ways to win
                    if check_winner(board_game_1):
                        #calling the functions that set property messages
                        game_over()
                        winner_messeage(turn)
                        break
                   
                if count == 9:
                    game_over()
                    print(adding.GREEN + 'It is a tie! Good players share the victory!\n'  + adding.ENDC)
                    break
    
                if turn == adding.BLUE + 'X' + adding.ENDC:
                    turn= adding.YELLOW + 'O' + adding.ENDC
                else:
                    turn= adding.BLUE + 'X' + adding.ENDC
            except:
                print(adding.RED + 'Invalid answer, try again' + adding.ENDC)
                continue
        #To start a new game.
        new_game= input('Do you want to play again? (Y/N): ').upper()
        
        if new_game == 'Y':
            print(adding.OCEAN + 'good choice! A New start gives us new oportunities to win!\n' + adding.ENDC)
            continue
        elif new_game == 'N':
            print(adding.GREEN + 'OK, maybe the next time.' + adding.ENDC)      
            break 
        else:
            #This part give you one more oportunity to enter your answer again if you make a mistake the first time.
            print(adding.RED + 'Invalid answer, try again' + adding.ENDC)
            new_game= input('Do you want to play again? (enter "Y" to continue or any other key to leave): ').upper()
            if new_game == 'Y':
                print(adding.OCEAN + 'good choice! A New start gives us new oportunities to win!\n' + adding.ENDC)
                continue
            else:
                break
       
#function to print the board game 
def the_board(position):
    print('\n')
    print(position[0] + '|' + position[1] + '|' + position[2])
    print('-+-+-')    
    print(position[3] + '|' + position[4] + '|' + position[5])
    print('-+-+-')
    print(position[6] + '|' + position[7] + '|' + position[8])
    print('\n')

#this function set the winner message
def winner_messeage(turn):
    print('\n' + adding.OCEAN + adding.BOLD + f'Congratulations, {turn}' + adding.OCEAN + '´s player!' + adding.OCEAN + ' You won this game! Well done!' + adding.ENDC + '\n')

def game_over():
    print(adding.RED + adding.BOLD + 'Game Over' + adding.ENDC)

#This function check all conditions to win.
def check_winner(board_game_1):
    return (board_game_1[0] == board_game_1[1] == board_game_1[2]) or (board_game_1[3] == board_game_1[4] == board_game_1[5]) or (board_game_1[6] == board_game_1[7] == board_game_1[8]) or (board_game_1[0] == board_game_1[3] == board_game_1[6]) or (board_game_1[0] == board_game_1[4] == board_game_1[8]) or (board_game_1[1] == board_game_1[4] == board_game_1[7]) or (board_game_1[2] == board_game_1[5] == board_game_1[8]) or (board_game_1[2] == board_game_1[4] == board_game_1[6])


if __name__=='__main__':
    main()