from sys import argv

bot_mark = argv[1]  # What the bot plays: X or O
current_board = argv[2]  # A string of 9 characters representing the board O,X,_

opponent_mark = "X" if bot_mark == "O" else "O"

# If any player has their mark on all of the locations in a certain array they have won
winning_grids = [
    # --- Rows ---
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # --- Columns ---
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    # --- Diagonals ---
    [0, 4, 8],
    [2, 4, 6],
]

placement_scores = {}

for x in range(9):
    placement_scores[x] = 0

best_place = 4

for grid in winning_grids:
    risk_score = 0
    for index in grid:
        if current_board[index] == opponent_mark:
            risk_score += 1
    for index in grid:
        if current_board[index] == "_":
            placement_scores[index] += risk_score
            if placement_scores[index] > placement_scores[best_place]:
                best_place = index

# Now we should have a good idea of where to place our own mark
new_board = current_board[0:best_place] + bot_mark + current_board[best_place + 1 :]

print(new_board)