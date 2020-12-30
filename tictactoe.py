board = {'7': ' ' , '8': ' ' , '9': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in board:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def play():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(board)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if board['1'] == board['2'] == board['3'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")                
                print("Player" +turn + " won.")                
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")                
                print("Player" +turn + " won.")
                break
            elif board['7'] == board['8'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")                
                print("Player" +turn + " won.")
                break
            elif board['1'] == board['4'] == board['7'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")                
                print("Player" +turn + " won.")
                break
            elif board['2'] == board['5'] == board['8'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")                
                print("Player" +turn + " won.")
                break
            elif board['3'] == board['6'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")                
                print("Player" +turn + " won.")
                break 
            elif board['7'] == board['5'] == board['3'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")                
                print("Player" +turn + " won.")
                break
            elif board['1'] == board['5'] == board['9'] != ' ':
                printBoard(board)
                print("\nGame Over.\n")                
                print("Player" +turn + " won.")
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        if turn =='X':
            turn = 'O'
        else:board
            turn = 'X'
    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y"board or restart == "Y":  
        for key in board_keys:board
            board[key] = " "

        play()

if __name__ == "__main__":
    play()