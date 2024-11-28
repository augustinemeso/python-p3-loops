#!/usr/bin/env python3

# 1. Happy New Year - Countdown from 10 to 1, and then print "Happy New Year!"
def happy_new_year():
    i = 10  # Start at 10
    while i > 0:
        print(i)
        i -= 1  # Decrease i by 1 after each iteration
    print("Happy New Year!")  # After the loop ends, print this message

# 2. Square Integers - Takes a list of integers and returns a new list with squared values
def square_integers(int_list):
    squared_numbers = []  # List to hold squared values
    for num in int_list:
        squared_numbers.append(num ** 2)  # Square the number and append to the list
    return squared_numbers  # Return the list of squared numbers

# 3. FizzBuzz - Prints numbers from 1 to 100 with specific rules
def fizzbuzz():
    for num in range(1, 101):  # Loop through numbers 1 to 100
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")  # If divisible by both 3 and 5
        elif num % 3 == 0:
            print("Fizz")  # If divisible by 3
        elif num % 5 == 0:
            print("Buzz")  # If divisible by 5
        else:
            print(num)  # Otherwise, just print the number

# Function calls for testing
if __name__ == "__main__":
    print("Testing happy_new_year:")
    happy_new_year()  # This will print numbers from 10 to 1, then "Happy New Year!"
    
    print("\nTesting square_integers:")
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = square_integers(numbers)
    print(squared_numbers)  # Expected output: [1, 4, 9, 16, 25]

    print("\nTesting fizzbuzz:")
    fizzbuzz()  # This will print the FizzBuzz sequence from 1 to 100
