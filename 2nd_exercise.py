import random
import numpy as np

notes = np.zeros((11, 10))
row_length = notes.shape[0]
column_length = notes.shape[1]
start_row = 7
filled_row_index = 0

for j in range(column_length):
    range_min = max(0, start_row - 2)
    range_max = min(10, start_row + 2)
    filled_row_index = random.choice(list(range(range_min, range_max)))
    notes[filled_row_index, j] = 1
    start_row = filled_row_index

# print(notes)

for i in range(notes.shape[0]):
    print("\n", end="")
    for j in range(notes.shape[1]):
        if i % 2 == 0:
            if notes[i, j] == 0:
                print("\t", end="")
            else:
                print("O\t", end="")
        else:
            if notes[i, j] == 0:
                print("-\t", end="")
            else:
                print("O\t", end="")
