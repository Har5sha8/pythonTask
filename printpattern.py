# def print_pattern(rows, columns):
#     # Upper part of the pattern
#     for i in range(rows):
#         if i < rows // 2:
#             print(" " * (rows - i - 1), end='')  
#             print("* " * columns)  
#         elif i == rows // 2:
#             print("* " * columns)  
#         else:
#             print(" " * (i - rows // 2), end='')  
#             print("* " * columns)  
def print_pattern(rows, columns):
    for i in range(rows):
        for j in range(columns):
            print("[]", end=" ")
        print()


rows1, columns1 = 4, 7
print("Sample 1:")
print_pattern(rows1, columns1)
print()

rows2, columns2 = 3, 5
print("Sample 2:")
print_pattern(rows2, columns2)
