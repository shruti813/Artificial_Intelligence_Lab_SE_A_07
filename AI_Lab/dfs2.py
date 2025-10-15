def dfs(maze, start, end):
    stack = [(start, [start])]  # Initialize stack with start position and path
    visited = set()  # Track visited positions

    while stack:
        position, path = stack.pop()  # Get current position and path
        x, y = position

        # Check if we've reached the end
        if position == end:
            return path  # Return the path to the solution

        # Mark the current cell as visited
        visited.add((x, y))

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy

            # Check bounds and if the cell is already visited or is a wall
            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                    maze[new_x][new_y] == 0 and (new_x, new_y) not in visited):
                stack.append(((new_x, new_y), path + [(new_x, new_y)]))

    return None  # Return None if no path is found

# Example maze: 0 -> open path, 1 -> wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Start and end positions
start = (0, 0)
end = (4, 4)

# Solve the maze and print the path
path = dfs(maze, start, end)
if path:
    print("Path found:", path)  # Output: the path from start to end
else:
    print("No path found")
