import re
from sympy import symbols, solve, log

def parse_recurrence(recurrence):
    # Extract the function calls and the theta term
    match = re.match(r'T\(n\) = ([^+]+) \+ ([^+]+) \+ (\Theta\([^()]+\))', recurrence)
    if not match:
        raise ValueError("Recurrence relation format is incorrect.")

    T1, T2, theta_term = match.groups()

    # Extract coefficients and subproblem sizes
    match1 = re.match(r'T\(([^()]+)\)', T1.strip())
    match2 = re.match(r'T\(([^()]+)\)', T2.strip())

    if not match1 or not match2:
        raise ValueError("Subproblem format is incorrect.")

    subproblem1 = float(match1.groups()[0].strip().replace('n', ''))
    subproblem2 = float(match2.groups()[0].strip().replace('n', ''))

    # Extract theta term coefficient
    match_theta = re.match(r'\Theta\(([^()]+)\)', theta_term.strip())
    if not match_theta:
        raise ValueError("Theta term format is incorrect.")

    theta_coefficient = match_theta.groups()[0].strip()

    return subproblem1, subproblem2, theta_coefficient

def solve_recurrence(subproblem1, subproblem2, theta_coefficient):
    n = symbols('n')

    # We need to solve for p in the equation (subproblem1)^p + (subproblem2)^p = 1
    p = symbols('p')
    equation = (subproblem1 ** p) + (subproblem2 ** p) - 1
    p_value = solve(equation, p)[0]

    if p_value > 1:
        return "Theta(n^{})".format(p_value)
    elif p_value == 1:
        return "Theta(n log n)"
    else:
        return "Theta(n^{})".format(p_value)

def main():
    recurrence = input("Enter the recurrence relation: ")
    subproblem1, subproblem2, theta_coefficient = parse_recurrence(recurrence)
    result = solve_recurrence(subproblem1, subproblem2, theta_coefficient)
    print("The solution to the recurrence is:", result)

if __name__ == "__main__":
    main()