# Math Assignment No.2

import math   # Import math library

# -------------------------------
# 1. Newton-Raphson Method
# -------------------------------
def newton_raphson():   # Define Newton-Raphson function
    print("\n--- Newton-Raphson Method ---")  # Display title
    
    def f(x):   # Define function f(x)
        return x**3 - x - 2   # Example equation
    
    def df(x):   # Define derivative f'(x)
        return 3*x**2 - 1   # Derivative of equation

    x0 = float(input("Enter initial guess: "))   # Initial approximation
    tolerance = float(input("Enter tolerance: "))   # Accuracy limit
    max_iter = int(input("Enter maximum iterations: "))   # Iteration limit

    for i in range(max_iter):   # Loop for iterations
        x1 = x0 - f(x0)/df(x0)   # Newton-Raphson formula
        print(f"Iteration {i+1}: x = {x1}")   # Print current value

        if abs(x1 - x0) < tolerance:   # Check convergence
            print("Root found:", x1)   # Display root
            return   # Exit function
        
        x0 = x1   # Update value for next iteration

    print("Method did not converge.")   # If no solution found


# -------------------------------
# 2. Newton Forward Interpolation
# -------------------------------
def newton_forward():   # Define interpolation function
    print("\n--- Newton Forward Interpolation ---")   # Display title

    n = int(input("Enter number of data points: "))   # Number of points
    
    x = []   # Empty list for x values
    y = []   # Empty list for y values

    print("Enter x values:")
    for i in range(n):   # Loop to read x
        x.append(float(input()))   # Store x values

    print("Enter y values:")
    for i in range(n):   # Loop to read y
        y.append(float(input()))   # Store y values

    value = float(input("Enter value to interpolate: "))   # Target value

    diff = [y.copy()]   # First difference row

    for i in range(1, n):   # Build difference table
        temp = []   # Temporary list
        for j in range(n - i):   # Compute differences
            temp.append(diff[i-1][j+1] - diff[i-1][j])   # Difference formula
        diff.append(temp)   # Add row to table

    h = x[1] - x[0]   # Step size
    p = (value - x[0]) / h   # Calculate p value

    result = y[0]   # Initialize result
    p_term = 1   # Initialize p term
    factorial = 1   # Initialize factorial

    for i in range(1, n):   # Apply interpolation formula
        p_term *= (p - i + 1)   # Update p term
        factorial *= i   # Update factorial
        result += (p_term * diff[i][0]) / factorial   # Add term

    print("Interpolated value:", result)   # Display result


# -------------------------------
# 3. Euler's Method
# -------------------------------
def euler_method():   # Define Euler function
    print("\n--- Euler's Method ---")   # Display title

    def f(x, y):   # Define differential equation
        return x + y   # Example dy/dx

    x0 = float(input("Enter initial x: "))   # Initial x
    y0 = float(input("Enter initial y: "))   # Initial y
    h = float(input("Enter step size: "))   # Step size
    xn = float(input("Enter final x: "))   # Final x

    x = x0   # Assign starting x
    y = y0   # Assign starting y

    print("\nSteps:")   # Print heading

    while x < xn:   # Loop until final x
        y = y + h * f(x, y)   # Euler formula
        x = x + h   # Increment x
        print(f"x = {x}, y = {y}")   # Display step

    print("Final approximate value:", y)   # Show result


# -------------------------------
# Main Menu
# -------------------------------
def main():   # Main function
    while True:   # Infinite loop
        print("\n===== Numerical Methods Calculator =====")   # Title
        print("1. Newton-Raphson Method")   # Option 1
        print("2. Newton Forward Interpolation")   # Option 2
        print("3. Euler's Method")   # Option 3
        print("4. Exit")   # Exit option

        choice = input("Enter your choice: ")   # User input

        if choice == '1':   # If choice 1
            newton_raphson()   # Call NR method
        elif choice == '2':   # If choice 2
            newton_forward()   # Call interpolation
        elif choice == '3':   # If choice 3
            euler_method()   # Call Euler
        elif choice == '4':   # If choice 4
            print("Exiting program...")   # Exit message
            break   # Stop loop
        else:
            print("Invalid choice.")   # Error message


if __name__ == "__main__":   # Run directly check
    main()   # Call main function