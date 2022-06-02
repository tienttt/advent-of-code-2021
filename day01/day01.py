import sys

if len(sys.argv) != 3:
    print("Usage: py .\day01.py <windows_size> <depths_path>")
    exit()

depths = []

with open(sys.argv[2], 'r') as f:
    for line in f:
        depths.append(int(line))

def window_sum_increases(window_size, depths):
    number_of_increases = 0
    for i in range(len(depths)-window_size):
        if depths[i+window_size] > depths[i]:
            number_of_increases += 1
    return number_of_increases
    
window_size = int(sys.argv[1])

print("Number of increases:", window_sum_increases(window_size, depths))





