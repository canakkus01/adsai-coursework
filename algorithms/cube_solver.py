# Can Akkus - Assignment 2: Cube Solver
# Data Structures and Algorithms

import collections

solved = tuple("WWWWRRRRBBBBOOOOGGGGYYYY")

moves = {
    "U": [2, 0, 3, 1, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 4, 5, 6, 7, 20, 21, 22, 23],
    "R": [0, 9, 2, 11, 4, 5, 6, 7, 8, 21, 10, 23, 14, 12, 15, 13, 3, 17, 1, 19, 20, 16, 22, 18],
    "F": [0, 1, 5, 6, 4, 21, 20, 7, 10, 8, 11, 9, 2, 3, 14, 15, 16, 17, 18, 19, 12, 13, 22, 23],
}

def apply_move(state, move_name):
    perm = moves[move_name]
    return tuple(state[i] for i in perm)

def solve_cube(start_state):
    if start_state == solved:
        return "Solved!"

    queue = collections.deque([(start_state, [])])
    visited = {start_state}

    print("Searching...")

    while queue:
        current_state, path = queue.popleft()

        if len(path) >= 14:
            continue

        for move in ["U", "R", "F"]:
            # clockwise
            next_state = apply_move(current_state, move)

            if next_state == solved:
                return " ".join(path + [move])

            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [move]))

            # counter-clockwise (prime) = move applied 3 times
            state_x2 = apply_move(current_state, move)
            state_x3 = apply_move(state_x2, move)
            state_prime = apply_move(state_x3, move)

            move_prime = move + "'"

            if state_prime == solved:
                return " ".join(path + [move_prime])

            if state_prime not in visited:
                visited.add(state_prime)
                queue.append((state_prime, path + [move_prime]))

    return "No solution found."


if __name__ == "__main__":
    my_cube = solved

    my_cube = apply_move(my_cube, "F")
    my_cube = apply_move(my_cube, "U")

    print(f"Scrambled State: {my_cube}")
    print("-" * 30)

    result = solve_cube(my_cube)
    print("Solution:", result)

