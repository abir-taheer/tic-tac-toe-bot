from sys import argv

# If any player has their mark on all of the locations in a certain array they have won
wins = [
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

Positions = (
    "Top-left",
    "Top-center",
    "Top-right",
    "Middle-left",
    "Middle-center",
    "Middle-right",
    "Bottom-left",
    "Bottom-center",
    "Bottom-right",
)


def main():
    outfile = argv[1]
    board = argv[2]
    bot_mark = "o" if board.count("x") > board.count("o") else "x"
    opponent_mark = "o" if bot_mark == "x" else "x"

    opponent_winning_index = None
    bot_winning_index = None

    possible_tiles = set()

    for grid in wins:
        empty_tiles = set()
        opponent_tiles = set()
        for index in grid:
            if board[index] == opponent_mark:
                opponent_tiles.add(index)
            elif board[index] == "_":
                empty_tiles.add(index)

        if len(empty_tiles) == 1 and len(opponent_tiles) == 0:
            bot_winning_index = empty_tiles.pop()

        if len(opponent_tiles) == 2 and len(empty_tiles) > 0:
            opponent_winning_index = empty_tiles.pop()

        if len(opponent_tiles) > 0:
            for tile in empty_tiles:
                possible_tiles.add(tile)

    if board[4] == "_":
        best_place = 4
    else:
        best_place = possible_tiles.pop()

    winner = (
        "No winner" if len(possible_tiles) < 7 else "Too early to determine a winner"
    )

    if opponent_winning_index is not None:
        best_place = opponent_winning_index
        winner = opponent_mark + " in 1 move"

    if bot_winning_index is not None:
        best_place = bot_winning_index
        winner = bot_mark + " in 1 move"

    s = "%d\n" % best_place
    s += "%s\n" % Positions[best_place]
    s += "%s\n" % winner
    print(s)
    print(board)
    f = open(outfile, "w")
    f.write(s)
    f.close()


main()
