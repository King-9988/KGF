def is_valid_assignment(assignment, var, value, neighbors):
    return all(assignment.get(neighbor) != value for neighbor in neighbors[var])

def backtrack(variables, assignment, neighbors, colors):
    if not variables:
        return assignment

    var = variables.pop()
    for color in colors:
        if is_valid_assignment(assignment, var, color, neighbors):
            assignment[var] = color
            result = backtrack(variables, assignment, neighbors, colors)
            if result:
                return result
            assignment.pop(var)
    variables.append(var)
    return None

def map_coloring(variables, neighbors, colors):
    return backtrack(variables.copy(), {}, neighbors, colors)

if __name__ == "__main__":
    variables = ["A", "B", "C"]
    colors = ["R", "G", "B"]
    neighbors = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B"],
    }

    solution = map_coloring(variables, neighbors, colors)

    if solution:
        print("Solution found:")
        print(solution)
    else:
        print("No solution found.")
