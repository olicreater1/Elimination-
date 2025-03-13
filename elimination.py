def solve_system_of_equations(a1, b1, c1, a2, b2, c2):
    # Ensure that neither (a1, b1) nor (a2, b2) are zero to avoid division by zero
    if a1 == 0 or a2 == 0:
        raise ValueError("Coefficients a1 and a2 must be non-zero.")

    # Multipliers to align coefficients of y (or x)
    m1 = a2
    m2 = a1

    # Multiply both equations by each others first value coefficient to make the first values of each equation equal for simplified subtraction in elimination system solving
    eq1 = [m1 * a1, m1 * b1, m1 * c1]
    eq2 = [m2 * a2, m2 * b2, m2 * c2]

    # Subtract eq2 from eq1 to eliminate x
    diff = [eq1[i] - eq2[i] for i in range(3)]
    _, b_diff, c_diff = diff

    # Solve for y and check for solution type
    if  b_diff == 0 and c_diff == 0:
        #check for and print statement for infinitely many solutions 
        x = "Infinitely Many Solutions"
        y = _
    elif b_diff == 0 and c_diff != 0:
        #check for and print statement for no solutions 
        x = "No Solutions"
        y = _    
   
    y = c_diff / b_diff
    # Substitute y into one of the original equations to find x
    x = (c1 - b1 * y) / a1
   
    #return values from function
    return x, y

def main():
    # ask user for values
    print("Enter the coefficients and constants for the system of equations:")
    print("Equation 1: a1*x + b1*y = c1")
    a1 = float(input("a1: "))
    b1 = float(input("b1: "))
    c1 = float(input("c1: "))

    print("\nEquation 2: a2*x + b2*y = c2")
    a2 = float(input("a2: "))
    b2 = float(input("b2: "))
    c2 = float(input("c2: "))
    

    # input values into the solve_system_of_equations function to output x and y
    x, y = solve_system_of_equations(a1, b1, c1, a2, b2, c2)

    #check if x and y are intagers to have different print statements for No Solution and Infinitely Many Solutions
    
    #print statement for output as an ordered pair
    print(f"\nSolution: x = {x}, y = {y}")
    
if __name__ == "__main__":
    main()