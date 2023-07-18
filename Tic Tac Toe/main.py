


grid = "a-b-c\nd-e-f\ng-h-i"
print("-----")
print(grid)
print("-----")

game_on = True
turn = 0
new_grid = ""
wrong_answer = False

while game_on:
    print("Give coordinates in the form 'a' to place your marker in the square corresponding to a.")
    if turn % 2 == 0:
        answer = input("Player 1. Choose a coordinate: ")
        if answer == "O" or answer == "X":
            wrong_answer = True
            while wrong_answer:
                print("You cannot choose a marker as a coordinate. Try again.")
                answer = input("Player 1. Choose a coordinate: ")
                if not answer == "O" and not answer == "X":
                    new_grid = grid.replace(answer, "O")
                    grid = new_grid
                    print(new_grid)
                    wrong_answer=False

        else:
            new_grid = grid.replace(answer, "O")
            grid = new_grid
            print(new_grid)

    else:
        answer = input("Player 2. Choose a coordinate: ")
        if answer == "O" or answer == "X":
            wrong_answer = True
            while wrong_answer:
                print("You cannot choose a marker as a coordinate. Try again.")
                answer = input("Player 2. Choose a coordinate: ")
                if not answer == "O" and not answer == "X":
                    new_grid = grid.replace(answer, "X")
                    grid = new_grid
                    print(new_grid)
                    wrong_answer = False

        else:
            new_grid = grid.replace(answer, "X")
            grid = new_grid
            print(new_grid)


    if turn == 8:
        print("Game Over.")
        game_on = False
        #1:
    elif grid[0] == "O" and grid[2] == "O" and grid[4] == "O":
        print("Player 1 with marker 'O' is the winner!")
        game_on = False
    elif grid[0] == "X" and grid[2] == "X" and grid[4] == "X":
        print("Player 2 with marker 'X' is the winner!")
        game_on = False
        #2:
    elif grid[4] == "O" and grid[8] == "O" and grid[12] == "O":
        print("Player 1 with marker 'O' is the winner!")
        game_on = False
    elif grid[4] == "X" and grid[8] == "X" and grid[12] == "X":
        print("Player 2 with marker 'X' is the winner!")
        game_on = False
        #3:
    elif grid[4] == "O" and grid[10] == "O" and grid[16] == "O":
        print("Player 1 with marker 'O' is the winner!")
        game_on = False
    elif grid[4] == "X" and grid[10] == "X" and grid[16] == "X":
        print("Player 2 with marker 'X' is the winner!")
        game_on = False
        #4:
    elif grid[0] == "O" and grid[8] == "O" and grid[16] == "O":
        print("Player 1 with marker 'O' is the winner!")
        game_on = False
    elif grid[0] == "X" and grid[8] == "X" and grid[16] == "X":
        print("Player 2 with marker 'X' is the winner!")
        game_on = False
        #5:
    elif grid[12] == "O" and grid[14] == "O" and grid[16] == "O":
        print("Player 1 with marker 'O' is the winner!")
        game_on = False
    elif grid[12] == "X" and grid[14] == "X" and grid[16] == "X":
        print("Player 2 with marker 'X' is the winner!")
        game_on = False
        #6:
    elif grid[0] == "O" and grid[6] == "O" and grid[12] == "O":
        print("Player 1 with marker 'O' is the winner!")
        game_on = False
    elif grid[0] == "X" and grid[6] == "X" and grid[12] == "X":
        print("Player 2 with marker 'X' is the winner!")
        game_on = False
        #7_
    elif grid[6] == "O" and grid[8] == "O" and grid[10] == "O":
        print("Player 1 with marker 'O' is the winner!")
        game_on = False
    elif grid[6] == "X" and grid[8] == "X" and grid[10] == "X":
        print("Player 2 with marker 'X' is the winner!")
        game_on = False
        #8:
    elif grid[2] == "O" and grid[8] == "O" and grid[14] == "O":
        print("Player 1 with marker 'O' is the winner!")
        game_on = False
    elif grid[2] == "X" and grid[8] == "X" and grid[14] == "X":
        print("Player 2 with marker 'X' is the winner!")
        game_on = False


    turn += 1