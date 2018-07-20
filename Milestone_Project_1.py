def tic_tac_toe():
    #Defines variables and sets up matrix
    row0 = ['   ','   ','   ']
    row1 = ['   ','   ','   ']
    row2 = ['   ','   ','   ']
    matrix = [row0,row1,row2]
    
    #Users input names
    p1name = input("Player 1, please input your name: ")
    p2name = input("Player 2, please input your name: ")

    #Defines function that draws board
    def draw_board():
        print('\n')
        print('\t\t\t',row0,'\n')
        print('\t\t\t ---------------------')
        print('\t\t\t',row1,'\n')
        print('\t\t\t ---------------------')
        print('\t\t\t',row2,'\n')
    
    #Defines function for Player 1's move
    def player_1_move():
        #While loop ensures player does not make invalid move (within board and not on spot previously taken)
        while True:
            #Exception handling in case player inputs incorrect format for move
            try:
                #Player inputs move
                p1row, p1col = input("%s, please input where you want to place your move \n"
                            "in the format row #,column #. Valid nums: (0,1,2): " % p1name).split(',')
                p1 = [int(p1row),int(p1col)]
                if (int(p1row) in range(0,3)) and (int(p1col) in range(0,3)):
                    if p1[0] == 0 and row0[p1[1]] == '   ':
                        break  
                    elif p1[0] == 1 and row1[p1[1]] == '   ':
                        break  
                    elif p1[0] == 2 and row2[p1[1]] == '   ':
                        break
                    else:
                        print("\nSorry, that position has already been taken. Please try again.\n")
                        continue
                #Informs user chosen move is outside board     
                else:
                    print("\nSorry, that input is invalid. Please enter a valid input in the correct range.\n")
                    continue
            except ValueError:
                print("\nIncorrect format.  Please try again.\n")
                pass
        #Places X mark for Player 1's move                    
        if p1[0] == 0:
            row0[p1[1]] = ' X '
        elif p1[0] == 1:
            row1[p1[1]] = ' X '
        elif p1[0] == 2:
            row2[p1[1]] = ' X '
        #Draws new board
        draw_board()
        
    #Defines function for Player 2's move        
    def player_2_move():
        #While loop ensures player does not make invalid move (within board and not on spot previously taken)
        while True:
            #Exception handling in case player inputs incorrect format for move
            try:
                #Player inputs move
                p2row, p2col = input("%s, please input where you want to place your move \n"
                            "in the format row #,column #. Valid nums: (0,1,2): " % p2name).split(',')
                p2 = [int(p2row),int(p2col)]
                if (int(p2row) in range(0,3)) and (int(p2col) in range(0,3)):
                    if p2[0] == 0 and row0[p2[1]] == '   ':
                        break  
                    elif p2[0] == 1 and row1[p2[1]] == '   ':
                        break
                    elif p2[0] == 2 and row2[p2[1]] == '   ':
                        break
                    else:
                        print("\nSorry, that position has already been taken. Please try again.\n")
                        continue
                #Informs user chosen move is outside board      
                else:
                    print("\nSorry, that input is invalid. Please enter a valid input in the correct range.\n")
                    continue
            except ValueError:
                print("\nIncorrect format. Please try again.\n")
                        
        #Places O mark for Player 2's move 
        if p2[0] == 0:
            row0[p2[1]] = ' O '
        elif p2[0] == 1:
            row1[p2[1]] = ' O '
        elif p2[0] == 2:
            row2[p2[1]] = ' O '

        #Draws new board
        draw_board()
    #Defines main function that runs game
    def game():
        #Draws initial board, sets up counter and turn variables to determine who wins and when game ends.
        draw_board()
        counter = 0
        turn = 0

        while True:
            #Player 1 moves first
            player_1_move()
            counter += 1
            turn += 1
            
            #Checks if Player 1 wins
            #Cross Checks
            if matrix[0][0] == matrix[1][1] == matrix[2][2] != '   ':
                break
            if matrix[2][0] == matrix[1][1] == matrix[0][2] != '   ':
                break
            #Row Checks
            if matrix[0][0] == matrix[0][1] == matrix[0][2] != '   ':
                break
            if matrix[1][0] == matrix[1][1] == matrix[1][2] != '   ':
                break
            if matrix[2][0] == matrix[2][1] == matrix[2][2] != '   ':
                break 
            #Column Checks
            if matrix[0][0] == matrix[1][0] == matrix[2][0] != '   ':
                break
            if matrix[0][1] == matrix[1][1] == matrix[2][1] != '   ':
                break
            if matrix[0][2] == matrix[1][2] == matrix[2][2] != '   ':
                break
            #Checks to see if game ended with no winner (tie)
            elif turn == 5:
                counter = 5
                break

            #Player 2 moves if Player 1 has not already won            
            player_2_move()
            counter -= 1

            #Checks if Player 2 wins
            #Cross Checks
            if matrix[0][0] == matrix[1][1] == matrix[2][2] != '   ':
                break
            if matrix[2][0] == matrix[1][1] == matrix[0][2] != '   ':
                break
            #Row Checks
            if matrix[0][0] == matrix[0][1] == matrix[0][2] != '   ':
                break
            if matrix[1][0] == matrix[1][1] == matrix[1][2] != '   ':
                break
            if matrix[2][0] == matrix[2][1] == matrix[2][2] != '   ':
                break 
            #Column Checks
            if matrix[0][0] == matrix[1][0] == matrix[2][0] != '   ':
                break
            if matrix[0][1] == matrix[1][1] == matrix[2][1] != '   ':
                break
            if matrix[0][2] == matrix[1][2] == matrix[2][2] != '   ':
                break
            else:
                continue

        #Prints which player won, unless no one won
        if counter == 0:
            print('%s won!' % p2name)
        elif counter == 1:
            print('%s won!' % p1name)
        else:
            print("Game is a draw. No one wins.")
        print("Game over.  Thanks for playing!")
    #Runs one single game
    game()
    
#Defines function that repeats game as long as players want
def run_tic_tac_toe():
    while True:
        tic_tac_toe()
        while True:
            again = input("Would you like to play again? (y/n): ")
            if again == 'y' or again == 'yes':
                break
            elif again == 'n' or again == 'no':
                break
            elif again != 'y' and again != 'yes' and again != 'n' and again != 'no':
                print("\nPlease enter a valid answer: ")
                continue
        if again == 'y' or again == 'yes':
            continue
        else:
            break
run_tic_tac_toe()
