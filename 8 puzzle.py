import random
initial_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

def misplaced_tiles(state):
    return sum([1 for i, j in zip(state, goal_state) if i != j])

def generate_neighbors(state):
    neighbors = []
    empty_tile_index = state.index(0)
    row, col = empty_tile_index // 3, empty_tile_index % 3

    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = state[:]
            new_empty_tile_index = new_row * 3 + new_col
            new_state[empty_tile_index], new_state[new_empty_tile_index] = new_state[new_empty_tile_index], new_state[empty_tile_index]
            neighbors.append(new_state)

    return neighbors

def hill_climbing(initial_state):
    current_state = initial_state
    current_cost = misplaced_tiles(current_state)

    while True:
        neighbors = generate_neighbors(current_state)

        if not neighbors:
            break

        best_neighbor = min(neighbors, key=misplaced_tiles)
        best_cost = misplaced_tiles(best_neighbor)

        if best_cost >= current_cost:
            break

        current_state = best_neighbor
        current_cost = best_cost

    return current_state

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

if __name__ == "__main__":
    print("Initial State:")
    print_puzzle(initial_state)

    final_state = hill_climbing(initial_state)

    print("\nFinal State (after hill climbing):")
    print_puzzle(final_state)
