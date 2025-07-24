# Shanks Bot - Prime Number Reciprocal Finder

This Python script calculates the reciprocal of a prime number and determines where the repeating sequence (Shanks) begins in the decimal expansion. The program performs long division manually and identifies the repeating part of the reciprocal.

## Features

- Determines if a given number is prime.
- Computes the reciprocal of a prime number.
- Identifies the number of figures after which the reciprocal starts repeating (Shanks).
- Displays the repeating and non-repeating parts of the reciprocal.
- Handles finite reciprocals for non-repeating prime reciprocals.

## Getting Started

### Prerequisites

To run this program, you'll need:

- Python 3.x installed on your machine.

### How to Run

1. Clone or download the script to your local machine.
2. Open a terminal or command prompt in the project directory.
3. Run the script using Python:

   ```bash
   python shanks_bot.py
4. You will be prompted to enter a prime number. The program will compute and display the reciprocal's repeating decimal sequence.

5. Enter a prime number to find its shank: 7
Reciprocal of 7 repeats after 6 figures.
Enter 1 if you wish to see the reciprocal of 7 before it starts to repeat: 1
Reciprocal: 0.(142857)

If the reciprocal doesn't repeat, the program will notify you that the decimal expansion is finite.

Functions
is_prime(num): Checks if a number is prime by performing trial division up to the square root of the number.
shanks_bot(prime_number): Performs long division to find the reciprocal and identifies repeating decimal sequences.
Notes
The input number must be a prime number; otherwise, the program will exit.
The program efficiently handles both finite and repeating decimals.
