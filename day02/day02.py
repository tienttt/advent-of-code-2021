
dict = {
    "down":0,
    "forward":0,
    "up":0
}
input_file_path = "input.txt"

with open(input_file_path, 'r') as f:
    for line in f:
        list = line.split(" ")
        dict[list[0]] += int(list[1])
print("Final horizontal position: ", dict["forward"]*(dict["down"]-dict["up"]))

dict = {
    "down":0,
    "forward":0,
    "up":0,
    "depth":0
}
aim = 0
with open(input_file_path, 'r') as f:
    for line in f:
        list = line.split(" ")
        dict[list[0]] += int(list[1])
        if list[0] == "down":
            aim += int(list[1])
        if list[0] == "up":
            aim -= int(list[1])
        if list[0] == "forward":
            dict["depth"] += aim * int(list[1])

print("Final horizontal position: ", dict["forward"]*(dict["depth"]))


