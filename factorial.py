def calculate_factorial() -> None:
    user_input = input("Enter a non-negative integer: ")

    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    if number < 0:
        print("Invalid input. The number must be non-negative.")
        return

    result = 1
    for factor in range(2, number + 1):
        result *= factor

    return(result)
