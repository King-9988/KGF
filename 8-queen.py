import heapq

def heuristic(state):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

def solve_8_queens():
    initial_state = tuple([-1] * 8)
    frontier = [(heuristic(initial_state), 0, initial_state)]
    explored = set()

    while frontier:
        _, cost, current_state = heapq.heappop(frontier)
        if current_state in explored:
            continue

        if cost == 8:
            return current_state

        explored.add(current_state)

        for next_col in range(8):
            next_state = list(current_state)
            next_state[cost] = next_col
            next_state = tuple(next_state)

            if next_state not in explored:
                h = heuristic(next_state)
                g = cost + 1
                f = g + h
                heapq.heappush(frontier, (f, g, next_state))

    return None

def print_solution(solution):
    for row in range(8):
        line = ""
        for col in range(8):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)

if __name__ == "__main__":
    solution = solve_8_queens()
    if solution:
        print_solution(solution)
    else:
        print("No solution found.")
