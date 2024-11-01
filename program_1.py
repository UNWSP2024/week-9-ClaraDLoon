#Program #1: Item Counter
#Clara Riley
#Luke Snell
#10/31/24

def count_names(filename):
    with open(filename, 'r') as file:
        names = file.readlines()
        return len(names)

filename = 'names.txt'
print(f'The number of names in {filename} is {count_names(filename)}')
