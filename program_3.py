#Program #3: Average Numbers
#Clara Riley
#Luke Snell
#10/31/24

def read_and_sum_numbers(filename):
    total = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    total += int(line.strip())
                except ValueError:
                    print(f"Skipping non-integer value: {line.strip()}")
    except IOError:
        print(f"An error occurred trying to read the file: {filename}")

    return total

filename = 'numbers.txt'
sum_of_numbers = read_and_sum_numbers(filename)
print(f"The total is: {sum_of_numbers}")
