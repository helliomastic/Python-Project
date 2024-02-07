import random

def generate_puzzle(size):
    numbers = list(range(1, size * size))
    numbers.append(None)  # Represent an empty space with None
    random.shuffle(numbers)
    puzzle = [numbers[i:i+size] for i in range(0, len(numbers), size)]
    return puzzle

def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(cell).rjust(2) if cell is not None else "  " for cell in row))

def get_empty_position(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] is None:
                return i, j

def is_solvable(puzzle):
    # Count inversions
    inversions = 0
    numbers = [num for row in puzzle for num in row if num is not None]
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                inversions += 1

    # For an N x N puzzle, it is solvable if N is odd and inversions is even
    # or if N is even and the empty cell is on an even row counting from the bottom and inversions is odd.
    empty_row, _ = get_empty_position(puzzle)
    size = len(puzzle)
    if size % 2 == 1:
        return inversions % 2 == 0
    else:
        return (empty_row % 2 == 0) == (inversions % 2 == 1)

def is_solved(puzzle):
    size = len(puzzle)
    return all(puzzle[i][j] == i*size + j + 1 if puzzle[i][j] is not None else puzzle[i][j] is None
               for i in range(size) for j in range(size))

def move(puzzle, direction):
    empty_row, empty_col = get_empty_position(puzzle)
    size = len(puzzle)

    if direction == 'up' and empty_row > 0:
        puzzle[empty_row][empty_col], puzzle[empty_row - 1][empty_col] = \
            puzzle[empty_row - 1][empty_col], puzzle[empty_row][empty_col]
    elif direction == 'down' and empty_row < size - 1:
        puzzle[empty_row][empty_col], puzzle[empty_row + 1][empty_col] = \
            puzzle[empty_row + 1][empty_col], puzzle[empty_row][empty_col]
    elif direction == 'left' and empty_col > 0:
        puzzle[empty_row][empty_col], puzzle[empty_row][empty_col - 1] = \
            puzzle[empty_row][empty_col - 1], puzzle[empty_row][empty_col]
    elif direction == 'right' and empty_col < size - 1:
        puzzle[empty_row][empty_col], puzzle[empty_row][empty_col + 1] = \
            puzzle[empty_row][empty_col + 1], puzzle[empty_row][empty_col]

def play_puzzle(size):
    puzzle = generate_puzzle(size)
    print("Welcome to the Number Puzzle Game!")
    print("Move the empty space to arrange the numbers in order.")
    print("Enter 'up', 'down', 'left', or 'right' to move the empty space.")
    print("Enter 'quit' to exit the game.")

    if not is_solvable(puzzle):
        print("This puzzle configuration is unsolvable. Generating a new one.")
        return

    while not is_solved(puzzle):
        print_puzzle(puzzle)
        move_input = input("Enter your move: ").lower()

        if move_input == 'quit':
            print("Thanks for playing!")
            return

        if move_input in ['up', 'down', 'left', 'right']:
            move(puzzle, move_input)
        else:
            print("Invalid move. Please enter 'up', 'down', 'left', 'right', or 'quit'.")

    print("Congratulations! You solved the puzzle!")
    print_puzzle(puzzle)

if __name__ == "__main__":
    play_puzzle(3)  # You can adjust the size of the puzzle here.

