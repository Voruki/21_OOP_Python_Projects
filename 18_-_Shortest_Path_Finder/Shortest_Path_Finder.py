import curses
from curses import wrapper
import queue
import time

# Define the maze
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    """
    Prints the maze on the screen using curses.

    Args:
    - maze (list): The maze layout.
    - stdscr: The curses screen object.
    - path (list): The path to highlight in the maze.
    """
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", RED)
            else:
                stdscr.addstr(i, j * 2, value, BLUE)

def find_start(maze, start):
    """
    Finds the starting position in the maze.

    Args:
    - maze (list): The maze layout.
    - start (str): The starting character.

    Returns:
    - tuple: Coordinates of the start position.
    """
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_path(maze, stdscr):
    """
    Finds the path from the start to the end in the maze.

    Args:
    - maze (list): The maze layout.
    - stdscr: The curses screen object.

    Returns:
    - list: The path from start to end.
    """
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.1)  # Reduced sleep time for faster visualization
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        for neighbor in find_neighbors(maze, row, col):
            if neighbor not in visited and maze[neighbor[0]][neighbor[1]] != "#":
                q.put((neighbor, path + [neighbor]))
                visited.add(neighbor)

def find_neighbors(maze, row, col):
    """
    Finds the neighboring cells in the maze.

    Args:
    - maze (list): The maze layout.
    - row (int): The current row position.
    - col (int): The current column position.

    Returns:
    - list: List of neighboring coordinates.
    """
    neighbors = []

    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))

    return neighbors

def main(stdscr):
    """
    Main function to set up curses and run the pathfinding.

    Args:
    - stdscr: The curses screen object.
    """
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()  # Wait for user input before exiting

if __name__ == "__main__":
    wrapper(main)
