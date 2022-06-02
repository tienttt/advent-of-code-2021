depths = []
number_of_increases = 0
with open('input.txt', 'r') as f:
    for line in f:
        depths.append(int(line))
window_size = 3
for i in range(len(depths)-window_size):
    if depths[i+window_size] > depths[i]:
        number_of_increases += 1
    
print(number_of_increases)


