board = [None] * 9

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
