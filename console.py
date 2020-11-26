import board
def printboard():
    
    num = ""
    for i in range(len(board.array_of_board)):
        
        for j in range(len(board.array_of_board[i])):
            num = num + str(board.array_of_board[i][j]) + " "  
        num += "\n" 
    print(num)          
printboard()
