from hmac import digest


input_file_path = "input.txt"

def read_input(input_file_path):
    diagnostic_report = []
    with open(input_file_path) as f:
        for line in f:
            diagnostic_report.append(line)
    return diagnostic_report

def rotate_input(input_file_path):
    diagnostic_report_rotated = None
    with open(input_file_path, 'r') as f:
        for line in f:
            binary = line.strip()
            if diagnostic_report_rotated == None:
                diagnostic_report_rotated = ['']*len(binary)
            for i in range(len(binary)):
                diagnostic_report_rotated[i] += binary[i]
    return diagnostic_report_rotated


# Find the most common bit at the position index
def find_the_most_common_bit(list_of_binary, index):
    number_of_0 = 0
    number_of_1 = 0
    for binary in list_of_binary: 
        if (binary[index] == '0'):
            number_of_0 += 1
        else:
            number_of_1 +=1
    if (number_of_0 == number_of_1):
        return "1"
    elif (number_of_1 > number_of_0):
        return '1'
    else:
        return '0'

def Task01(diagnostic_report_rotated):
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(len(diagnostic_report[0])-1):
        print(i)
        the_most_common_bit = find_the_most_common_bit(diagnostic_report, i)
        gamma_rate += the_most_common_bit
        epsilon_rate += str(1 - int(the_most_common_bit))

    return int(gamma_rate, 2) * int(epsilon_rate, 2)

# Get the binary string has the most common bit at position x
def get_the_list_of_binary_has_bit_y_at_position_x(binary_list, bit_y, x):
    most_common_binary_list = []
    for binary in binary_list:
        if binary[x] == bit_y:
            most_common_binary_list.append(binary)
    return most_common_binary_list


def Task02(diagnostic_report):
    oxygen_list = diagnostic_report
    CO2_list = diagnostic_report
    #for each bit from the begining to the one before the last one, check the most common bit for each position
    #and create a new list contains binary string with common bits at each position
    for i in range(len(diagnostic_report[0]) - 1):
        if(len(oxygen_list)>1):
            the_most_common_bit_oxygen_list = find_the_most_common_bit(oxygen_list, i)
            oxygen_list = get_the_list_of_binary_has_bit_y_at_position_x(oxygen_list, the_most_common_bit_oxygen_list, i)
        if (len(CO2_list) > 1):
            the_less_common_bit_CO2_list = str(1 - int(find_the_most_common_bit(CO2_list, i)))
            CO2_list = get_the_list_of_binary_has_bit_y_at_position_x(CO2_list, the_less_common_bit_CO2_list, i)

    oxygen_generator_rate = int(oxygen_list[0], 2)
    CO2_generator_rate = int(CO2_list[0], 2)

    return oxygen_generator_rate * CO2_generator_rate    

diagnostic_report = read_input(input_file_path)
power_consumption = Task01(diagnostic_report)
print(power_consumption)

life_support_rate = Task02(diagnostic_report)
print(life_support_rate)
