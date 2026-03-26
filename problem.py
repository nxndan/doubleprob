import numpy as np
 
TRANSITION_MATRIX = np.array([  # essentially creating a matrix that multiplies unsolved problems by 2 and adds +1 to solved problems (doubling a problem every time it is solved)
    [2, 0],  
    [1, 1],  
])
 
def get_state_after_steps(steps: int) -> np.ndarray:
    initial_state = np.array([1, 0]) # I'm going to assume the starting point is going to be 1 unsolved problem and 0 solved problem 
    matrix_n = np.linalg.matrix_power(TRANSITION_MATRIX, steps) #this should jsut raise the matrix to a power so if we are running the test once it raises it to the power of one
    return matrix_n @ initial_state
 
def total_problems_solved(steps: int) -> int:
    state = get_state_after_steps(steps)
    return int(state[1]) # returns the problems that were solved 
 
def unsolved_remaining(steps: int) -> int:
    state = get_state_after_steps(steps)
    return int(state[0])  # returns the problems that are still unsolved
 
results = { # idk how to print the results so chatgpt told me to make a dictionary so I did that 
    n: {
        "solved": total_problems_solved(n),
        "remaining": unsolved_remaining(n),
    }
    for n in range(1, 12)
}

print(results) #results mean that the solver will never be able to catch up to the amount of questions being generated because f(x) = 2x - x (not exponentially rising assuming the solver isn't messing stuff up)
