array_of_board =[]
rows = 6
cols = 7
for i in range(rows):
    array_of_board.append([])
    for j in range(cols):
        array_of_board[i].append(0)  

        
def setSign(col,sign):
    
    #rows = 6
    cols = 7
    #newrow = 0
    
    for j in range(cols): 
        if j == col:
                        # if newarray[5][j] == sign:
                        #     newarray[4][j] = sign
                        # else:
                        #     newarray[5][j] = sign
                        # if newarray[4][j] == sign:
                        #     newarray[3][j] = sign
                        # else:
                        #     newarray[4][j] = sign
                        # if newarray[3][j] == sign:
                        #     newarray[2][j] == sign
                        # else:
                        #     newarray[][j] = sign
            array_of_board[5][j] = sign 
            
            
    return array_of_board

def canPlay(conindex):
    IsTrue = True
    
    
    
    if array_of_board[5][conindex] == 'A' or array_of_board[5][conindex] == "B":
        
        if array_of_board[4][conindex] == 'A' or array_of_board[4][conindex] == "B":
        
    
            if array_of_board[3][conindex] == 'A' or array_of_board[3][conindex] == "B":
         
    
        
                if array_of_board[2][conindex] == 'A' or array_of_board[2][conindex] == "B":
                    IsTrue = False
    
    
    
    

                    
    return IsTrue
print(canPlay(2))    




    
    





