from math import floor

def is_prime(num):
    if num < 2:
        return False
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True

def shanks_bot(prime_number):
    value = "0."  # Instantiate the numerical value of (1 / prime_number)
    remainder = 1  # Start with the remainder 1 (as in long division)
    remainder_list = []  # To store remainders seen during division
    result_digits = []  # To store digits of the result

    # Perform long division
    while remainder not in remainder_list:
        remainder_list.append(remainder)

        # Perform the next division step by multiplying the remainder by 10
        remainder *= 10
        digit = floor(remainder / prime_number)  # Get the next digit in the division
        result_digits.append(str(digit))  # Append the digit to the result list
        remainder = remainder % prime_number  # Update the remainder

        if remainder == 0:
            print(f"Reciprocal of {prime_number} is finite: {value}{''.join(result_digits)}")
            return

    # Identify where the repeating part starts
    start_index = remainder_list.index(remainder)
    non_repeating_part = ''.join(result_digits[:start_index])
    repeating_part = ''.join(result_digits[start_index:])

    print(f"Reciprocal of {prime_number} repeats after {len(result_digits) - start_index} figures.")
    
    # Ask the user if they want to see the reciprocal
    show_value = input(f"Enter 1 if you wish to see the reciprocal of {prime_number} before it starts to repeat: ")
    if int(show_value) == 1:
        print(f"Reciprocal: {value}{non_repeating_part}({repeating_part})")

## Test the code
num = int(input("Enter a prime number to find its shank: "))
if is_prime(num):
    shanks_bot(num)
else:
    print(f"{num} is not a prime number. Exiting program.")
