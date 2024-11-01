#Program #2: Random Number File Writer
#Clara Riley
#Luke Snell
#10/31/24

import random

def generate_random_numbers(filename, count):
    if count > 1000:
        raise ValueError("Count cannot be over 1000")

    with open(filename, 'w') as file:
        for _ in range(count):
            number = random.randint(1, 500)
            file.write(f"{number}\n")

if __name__ == "__main__":
    try:
        count = int(input("How many numbers would you like generated? (up to 1000): "))
        generate_random_numbers("random_numbers.txt", count)
        print(f"{count} random numbers have been written in 'random_numbers.txt'")
    except ValueError as e:
        print(f"Error: {e}")
