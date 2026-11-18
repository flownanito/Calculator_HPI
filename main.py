from combinatorial import combinatorial
from factorial import calculate_factorial
from greatest_common_divisor import greatest_common_divisor
from log import logarithm
from solve_cuadratic_ecuations import solve_equation

def show_menu():
    """Displays the main menu of the advanced calculator."""
    print("\n========================================")
    print("         ADVANCED CALCULATOR            ")
    print("========================================")
    print("1. Calculate Factorial")
    print("2. Combinatorics (n choose k)")
    print("3. Greatest Common Divisor (GCD)")
    print("4. Logarithm")
    print("5. Solve Quadratic or Linear Equation")
    print("========================================")

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            print("\n--- Factorial ---")
            result = calculate_factorial()
            if result is not None:
                print(f"Result: {result}")

        elif choice == "2":
            print("\n--- Combinatorics ---")
            result = combinatorial(0, 0)
            print(f"Result: {result}")

        elif choice == "3":
            print("\n--- Greatest Common Divisor ---")
            result = greatest_common_divisor()
            print(f"Result: {result}")

        elif choice == "4":
            print("\n--- Logarithm ---")
            try:
                result = logarithm()
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "5":
            print("\n--- Quadratic / Linear Equations ---")
            result = solve_equation()
            print(f"Result: {result}")

        else:
            print("\n Invalid option. Please enter a number between 1 and 5.")
            continue  # Restarts the loop if the option is invalid

        # Ask if the user wants to exit after a calculation
        exit_choice = input("\nDo you want to exit? (y/n): ").strip().lower()
        if exit_choice == 'y' or exit_choice == 'yes':
            print("\nThank you for using our calculator!")
            break

if __name__ == "__main__":
    main()
