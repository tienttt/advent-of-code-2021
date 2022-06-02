depths = []
number_of_increases = 0
with open('input.txt', 'r') as f:
    for line in f:
        depths.append(int(line))


for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        number_of_increases += 1
    

print(number_of_increases)



