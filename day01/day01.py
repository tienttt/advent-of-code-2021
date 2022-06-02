depths = []

with open('input.txt', 'r') as f:
    for line in f:
        depths.append(int(line))

def window_sum_increases(window_size, depths):
    number_of_increases = 0
    for i in range(len(depths)-window_size):
        if depths[i+window_size] > depths[i]:
            number_of_increases += 1
    return number_of_increases
    
window_size = 3

print(f"part 1: {window_sum_increases(1, depths)}")
print("part 2:", window_sum_increases(3, depths))



