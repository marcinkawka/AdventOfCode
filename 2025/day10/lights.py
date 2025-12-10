
import numpy as np
import pulp
from scipy.optimize import milp

bulb_dict = {'.': 0, '#': 1}
total_presses = 0

def solve_machine(pattern, buttons):
    """
    pattern: string like '.##.#'
    buttons: list of tuples of indices, e.g. [(3,), (1,3), (2,), (2,3), (0,2), (0,1)]
    returns (min_presses, chosen_buttons) where chosen_buttons is list of indices of buttons to press
    """

    n_lights = len(pattern)
    n_buttons = len(buttons)

    # Binary vars: x_j = 1 if button j is pressed once, else 0
    x = pulp.LpVariable.dicts("x", range(n_buttons), 0, 1, cat="Binary")

    # Problem: minimize total presses
    model = pulp.LpProblem("lights", pulp.LpMinimize)
    model += pulp.lpSum(x[j] for j in range(n_buttons))

    # For each light i: sum of presses of buttons that touch i ≡ target_i (mod 2)
    # Encode mod-2 as equality in {0,1}: sum(...) - 2 * y_i = target_i
    y = pulp.LpVariable.dicts("y", range(n_lights), lowBound=0, cat="Integer")

    for i in range(n_lights):
        target = 1 if pattern[i] == "#" else 0
        involved = [j for j, btn in enumerate(buttons) if i in btn]
        model += pulp.lpSum(x[j] for j in involved) - 2 * y[i] == target

    model.solve(pulp.PULP_CBC_CMD(msg=False))

    chosen = [j for j in range(n_buttons) if pulp.value(x[j]) > 0.5]
    return len(chosen), chosen


with open('input.txt') as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
    
        ll =line.split(' ')
        bulbs = ll[0][1:-1]
        xors = []
        for button_set in ll[1:-1]:
            buttons = tuple(map(int, button_set[1:-1].split(',')))
            xors.append(buttons)

        min_presses, chosen_buttons = solve_machine(bulbs,xors)
        print("Minimum button presses:", min_presses)
        total_presses += min_presses
        
print("Total minimum button presses for all machines:", total_presses)