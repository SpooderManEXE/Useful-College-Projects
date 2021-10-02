rows = int(input("Enter Plus Pattern Rows = "))

print("Plus Star Pattern") 

for i in range(1, 2 * rows):
    for j in range(1, 2 * rows):
        if i == rows or j == rows:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
