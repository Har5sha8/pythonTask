def print_pattern(rows, columns):
    for i in range(rows):
        for j in range(columns):
            print("*", end=" ")
        print()

# Sample usage
rows = 4
columns = 7
print_pattern(rows, columns)

rows = 3
columns = 5
print_pattern(rows, columns)