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

def canPlay(colindex):
    IsTrue = True
    
    
    
    if array_of_board[5][colindex] == 'A' or array_of_board[5][colindex] == "B":
        
        if array_of_board[4][colindex] == 'A' or array_of_board[4][colindex] == "B":
        
    
            if array_of_board[3][colindex] == 'A' or array_of_board[3][colindex] == "B":
         
    
        
                if array_of_board[2][colindex] == 'A' or array_of_board[2][colindex] == "B":
                    IsTrue = False
    
    
    
    

                    
    return IsTrue
print(canPlay(2))    



def clearboard():
    rows = 6
    cols = 7
    for i in range(rows):
        for j in range(cols):
            if array_of_board[i][j] != 0:
                array_of_board[i][j] = 0   
clearboard()

def play(Isred, colindex):
    
    Isred == "Player RED" == True 
    
    
    
    if Isred:
        if array_of_board[5][colindex] ==0:
            array_of_board[5][colindex] = "A"
        
        
        elif array_of_board[4][colindex]==0:
            array_of_board[4][colindex] = "A"
        
        elif(array_of_board[3][colindex]) == 0:
            array_of_board[3][colindex] = "A"

         elif(array_of_board[2][colindex]) == 0:
            array_of_board[2][colindex] = "a"
       
        
        elif(array_of_board[1][colindex]) == 0:
        
            array_of_board[1][colindex] = "A"
        
         elif(array_of_board[0][colindex]) == 0:
            array_of_board[0][colindex] = "A"
       
        
    else:

        if(array_of_board[5][colindex]) == 0:
            array_of_board[5][colindex] = "B"
        
        elif(array_of_board[4][colindex]) == 0:
            array_of_board[4][colindex] = "B"
        
        
        elif(array_of_board[3][colindex]) == 0:
            array_of_board[3][colindex] = "B"

        elif(array_of_board[2][colindex]) == 0:
            array_of_board[2][colindex] = "B"
        
        elif(array_of_board[1][colindex]) == 0:
            array_of_board[0][colindex] = "B"
        
        
        

       
                
        elif array_of_board[1][colindex] == 0:
        
            array_of_board[1][colindex] = "B"
    return array_of_board
Isred = input ('the name of player')
colindex = int(input('the column index'))
print(play(Isred,colindex))

        
        