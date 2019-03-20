import os
from board import Board

class Tictactoe():

    b = Board()
    choicePlayer1 = ''
    choucePlayer2 = ''
    corretChoice = False
    correctPlayer1 = False
    correctPlayer2 = False


    def runGame(self):
        os.system('clear')

        #Resets the game when a new game is started
        #Is necessary if the players wish to play more than 1 game
        resetGame(self)

        #Makes sure the game only starts if player1 picks X or O
        while self.corretChoice == False:
            
            self.choicePlayer1 = input('Do you want to play X or O? ')
            print()
            if self.choicePlayer1 == 'X':
                self.choicePlayer2 = 'O'
                self.corretChoice = True
                print('Starting player selected X')

            elif self.choicePlayer1 == 'O':
                self.choicePlayer2 = 'X'
                self.corretChoice = True
                print('Starting player selected O')
            else:
                print('ERROR - input has to be either X or O!')
                continue

        os.system('clear')
        self.b.drawboard()

        while self.b.GameOver == False:
            self.correctPlayer1 = False
            self.correctPlayer2 = False
            
            #For player1
            while self.correctPlayer1 == False:
                while True:
                    try:
                        x = int(input(self.choicePlayer1 + ' Where do you want to place your piece? '))
                        break
                    except:
                        print('Input has to be a number, try again')

                if x > 0 and x < 10 and type(self.b.board[x]) != str:
                    self.b.update(x, self.choicePlayer1)
                    self.correctPlayer1 = True
                elif x == 10:
                    quit()
                else: 
                    print('Spot is taken, try again: ')

                if self.b.GameOver == True:
                    self.correctPlayer2 = True

                if self.b.tie() == True:
                    self.correctPlayer2 = True
                    self.b.GameOver = True
                    print('Game is a tie')
            #For player2
            while self.correctPlayer2 == False:
                while True:
                    try:
                        x = int(input(self.choicePlayer2 + ' Where do you want to place your piece? '))
                        break
                    except:
                        print('Input has to be a number, try again')

                if x > 0 and x < 10 and type(self.b.board[x]) != str:
                    self.b.update(x, self.choicePlayer2)
                    self.correctPlayer2 = True
                elif x == 10:
                    quit()
                else: 
                    print('Spot is taken, try again: ')
                
                if self.b.tie() == True:
                    self.b.gameOver = True
                    print('Game is a tie')

#Resets the game if the players wishes to play again
def resetGame(self):
    self.b = Board()
    self.choicePlayer1 = ''
    self.choucePlayer2 = ''
    self.corretChoice = False
    self.correctPlayer1 = False
    self.correctPlayer2 = False
    self.b.resetBoard()