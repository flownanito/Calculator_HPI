import typing

def solve_equation() -> typing.Optional[typing.Union[typing.Tuple[float, float], float, str]]:
    """Solves quadratic (ax^2 + bx + c = 0) or linear equations."""
    # Collect coefficients from user input (supports decimals)
    a = float(input("Enter 'a': "))
    b = float(input("Enter 'b': "))
    c = float(input("Enter 'c': "))
    
    # Handle cases where 'a' is 0 (missing quadratic term, becomes linear)
    if a == 0:
        if b == 0:
            return "No solution" if c != 0 else "Infinite solutions"
        return -c / b  # Solve simple linear equation: bx + c = 0
        
    # Calculate discriminant (b^2 - 4ac)
    disc = (b ** 2) - (4 * a * c)
    if disc < 0:
        return None  # Imaginary numbers
        
    # Compute square root and denominator (2a)
    s, d = disc ** 0.5, 2 * a
    
    # Return both roots for the quadratic equation
    return ((-b + s) / d, (-b - s) / d)

print(solve_equation())
