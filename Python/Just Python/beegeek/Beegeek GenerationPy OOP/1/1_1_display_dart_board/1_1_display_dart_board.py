'''
TODO:
        Let's assume that the playing field for darts is a square matrix.
        That filled with natural numbers arranged in ascending order
        from the edges to the center.

        The side of the playing field is the side of the square matrix
        that this field represents.

        Write a program that creates a darts field of a certain size.

        It's guaranteed that the side of the playing field does'nt exceed 18.

        Input:
            The program receives a single natural number as input — the
            side of the playing field.

        Output:
            The program must create and output a playing field with a
            given side.
'''


def display_dart_board(board: list[list[int]]) -> None:
    """
    Prints the dart board row by row.

    Args:
        board (list[list[int]]): The dart board matrix to display.
    """
    for row in board:
        print(" ".join(map(str, row)))


def calculate_steps_to_edges(row: int, col: int, size: int) -> list[int]:
    return [row, size + 1 - col, size + 1 - row, col]


def create_dart_board(size: int) -> list[list[int]]:
    """
    Creates a square dart board matrix with natural numbers arranged in
    ascending order from the edges to the center.

    Args:
        size (int): The size of the dart board (side of the square matrix).

    Returns:
        list[list[int]]: The generated dart board matrix.
    """
    board = []
    for row in range(1, size + 1):
        row_values = []
        for col in range(1, size + 1):
            # Calculate the minimum distance to the edge
            min_distance = min(calculate_steps_to_edges(row, col, size))
            row_values.append(min_distance)
        board.append(row_values)
    return board


if __name__ == "__main__":
    size = int(input("Enter the size of the dart board: "))
    darts = create_dart_board(size)
    display_dart_board(darts)
