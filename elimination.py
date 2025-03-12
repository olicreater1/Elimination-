def solve_system_of_equations(a1, b1, c1, a2, b2, c2):
    # Ensure that neither (a1, b1) nor (a2, b2) are zero to avoid division by zero
    if a1 == 0 or a2 == 0:
        raise ValueError("Coefficients a1 and a2 must be non-zero.")

    # Multipliers to align coefficients of y (or x)
    m1 = a2
    m2 = a1

    # Multiply both equations
    eq1 = [m1 * a1, m1 * b1, m1 * c1]
    eq2 = [m2 * a2, m2 * b2, m2 * c2]

    # Subtract eq2 from eq1 to eliminate x
    diff = [eq1[i] - eq2[i] for i in range(3)]
    _, b_diff, c_diff = diff

    # Solve for y
    if b_diff == 0:
        raise ValueError("Cannot eliminate variable; equations may be dependent or inconsistent. UNDEFINED OR ALL SOLUTIONS")
    
    y = c_diff / b_diff

    # Substitute y into one of the original equations to find x
    x = (c1 - b1 * y) / a1

    return x, y

def main():
    print("Enter the coefficients and constants for the system of equations:")
    print("Equation 1: a1*x + b1*y = c1")
    a1 = float(input("a1: "))
    b1 = float(input("b1: "))
    c1 = float(input("c1: "))

    print("\nEquation 2: a2*x + b2*y = c2")
    a2 = float(input("a2: "))
    b2 = float(input("b2: "))
    c2 = float(input("c2: "))

    try:
        x, y = solve_system_of_equations(a1, b1, c1, a2, b2, c2)
        print(f"\nSolution: x = {x}, y = {y}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()