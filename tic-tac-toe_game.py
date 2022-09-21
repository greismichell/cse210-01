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
   
    for i in range(10):
        the_board(board_game_1)
       
        move = int(input(f"{turn}'s turn to choose a square by typing its number (choose wisely): "))
        move= move-1

        if board_game_1[move] == '1' or board_game_1[move] == '2' or board_game_1[move] == '3' or board_game_1[move] == '4' or board_game_1[move] == '5' or board_game_1[move] == '6' or board_game_1[move] == '7' or board_game_1[move] == '8' or board_game_1[move] == '9':
            board_game_1[move] = turn
            count += 1
        else:
            print(adding.RED + 'this place is unvalaible' + adding.ENDC)
            continue
   
    #finding the winner
        if count >=5:
            the_board(board_game_1)
            #win through the horizontal top
            if check_winner(board_game_1):
                
                game_over
                winner_messeage(turn)
                break
           
        if count == 9:
            game_over
            print(adding.GREEN + 'It is a tie!' + adding.ENDC)
        if turn == adding.BLUE + 'X' + adding.ENDC:
            turn= adding.YELLOW + 'O' + adding.ENDC
        else:
            turn= adding.BLUE + 'X' + adding.ENDC

        

#funtion to print the board game 
def the_board(position):
    print('\n')
    print(position[0] + '|' + position[1] + '|' + position[2])
    print('-+-+-')    
    print(position[3] + '|' + position[4] + '|' + position[5])
    print('-+-+-')
    print(position[6] + '|' + position[7] + '|' + position[8])
    print('\n')

def winner_messeage(turn):
    print('\n' + adding.MAGENTA + f'the player {turn} won this game! Well done!' + adding.ENDC + '\n')

def game_over():
    print(adding.RED + adding.BOLD + 'Game Over' + adding.ENDC)

def check_winner(board_game_1):
    return (board_game_1[0] == board_game_1[1] == board_game_1[2]) or (board_game_1[3] == board_game_1[4] == board_game_1[5]) or (board_game_1[6] == board_game_1[7] == board_game_1[8]) or (board_game_1[0] == board_game_1[3] == board_game_1[6]) or (board_game_1[0] == board_game_1[4] == board_game_1[8]) or (board_game_1[1] == board_game_1[4] == board_game_1[7]) or (board_game_1[2] == board_game_1[5] == board_game_1[8]) or (board_game_1[2] == board_game_1[4] == board_game_1[6])
    

if __name__=='__main__':
    main()