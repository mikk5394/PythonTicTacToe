from tictac import Tictactoe

run = Tictactoe()

while True:
    run.runGame()
    if input("Play again? (y/n)") == "n":
        quit()
