
def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b

    return abs(a)


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

result = greatest_common_divisor(first_number, second_number)

print("The greatest common divisor is:", result)
