import os
class Board:

    board = [0,1,2,3,4,5,6,7,8,9]
    win_combinations = [
        (1,2,3),
        (4,5,6),
        (7,8,9),
        (1,5,9),
        (3,5,7),
        (1,4,7),
        (2,5,8),
        (3,6,9),
    ]
    GameOver = False

    #Draws the
    def drawboard(self):
        print('=========')
        print(self.board[7], '|', self.board[8], '|', self.board[9])
        print(self.board[4], '|', self.board[5], '|', self.board[6])
        print(self.board[1], '|', self.board[2], '|', self.board[3])
        print('=========')

    #Checks if the move the player just made, made him/she win the game
    def checkIfWon(self, choice):
        
        for a, b, c in self.win_combinations:
            if self.board[a] == self.board[b] == self.board[c]:
                print('Game over, player ' + choice + ' won the game')
                self.GameOver = True
    
    #Update the current board 
    def update(self, input, choice):

        self.board[input] = choice
        os.system('clear')
        self.drawboard()
        self.checkIfWon(choice)

    #Resets the board
    def resetBoard(self):
        self.board = [0,1,2,3,4,5,6,7,8,9]
    
    #Stops the game if tie
    def tie(self):
        list = []
        for x in self.board:
            if type(x) != int:
                list.append(x)
        
        if len(list) == 9:
            return True