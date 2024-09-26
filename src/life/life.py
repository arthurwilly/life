import collections

class Life:
    """A Python implementation of Game of Life. 

    As part of Big Geodata Processing course.

    Rules:
    - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    - Any live cell with two or three live neighbours lives on to the next generation.
    - Any live cell with more than three live neighbours dies, as if by overpopulation.
    - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """

    def __init__(self, filename: str):
        """Creates a game of life object. 

        Args:
          filename: Input file name. 
        """
        self.filename = filename
        self.live_cells = set()
        
        # Load live cells from the input file, ignoring the first line
        with open(filename) as f:
            lines = f.readlines()
        
        self.grid_size = int(lines[0].strip().split()[0])
        # Load the live cells as tuples of integers
        self.live_cells = {tuple(map(int, line.split())) for line in lines[1:]}  # Ignore first line

    def tick(self): 
        """Applies the rules of Game of Life for one generation."""
        neighbors = (
            (-1, -1),  # Above left
            (-1, 0),   # Above
            (-1, 1),   # Above right
            (0, -1),   # Left
            (0, 1),    # Right
            (1, -1),   # Below left
            (1, 0),    # Below
            (1, 1)     # Below right
        )

        # Dictionary to count the number of neighbors for each cell
        num_neighbors = collections.defaultdict(int)
        
        # Count the neighbors of each live cell
        for row, col in self.live_cells:
            for drow, dcol in neighbors:
                neighbor = (row + drow, col + dcol)
                num_neighbors[neighbor] += 1

        # Determine which live cells will stay alive
        stay_alive = {cell for cell, count in num_neighbors.items() if count in {2, 3}} & self.live_cells
        
        # Determine which dead cells will come alive
        come_alive = {cell for cell, count in num_neighbors.items() if count == 3} - self.live_cells
        
        # Update the set of live cells for the next generation
        self.live_cells = stay_alive | come_alive

    def display_grid(self):
        """Displays the current state of the grid with live and dead cells."""
        print("\n Current grid:")

        # Initialize grid with dead cells ('0')
        grid = [["0" for _ in range(self.grid_size)] for _ in range(self.grid_size)]  

        # Mark live cells with '1'
        for row, col in self.live_cells:
            if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
                grid[row][col] = "1" 

        # Print the updated grid
        print("\n".join("".join(row) for row in grid))