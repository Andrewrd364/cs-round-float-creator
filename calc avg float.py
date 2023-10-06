from itertools import combinations
import struct
import time


def get_ieee754(value: float) -> float:
    temp = struct.pack('!f', value)
    result = struct.unpack('!f', temp)[0]
    return result


# Change expected float value of the skin here
exp_float = 0.5
# Change float caps of the expected skin here
float_caps = [0.06, 0.8]

float_caps[0], float_caps[1] = get_ieee754(float_caps[0]), get_ieee754(float_caps[1])
difference = get_ieee754(float_caps[1] - float_caps[0])
exp_float_in_caps = get_ieee754((exp_float - float_caps[0]) / difference)

lower_bound = higher_bound = exp_float_in_caps

while get_ieee754(lower_bound * difference + float_caps[0]) == exp_float:
    lower_bound -= 0.000000000001
lower_bound += 0.000000015
while get_ieee754(higher_bound * difference + float_caps[0]) == exp_float:
    higher_bound += 0.000000000001
higher_bound -= 0.000000015


def read_text():
    with open('input.txt', 'r') as file:
        filtered_text = []
        for i in file.readlines():
            if i.find("Float:") != -1:
                filtered_text.append(get_ieee754(float(i.replace("Float: ", "").replace("\n", ""))))
            if len(filtered_text) == 33:
                break

    with open('input.txt', 'w') as file:
        pass

    return filtered_text


def main():
    time_start = time.perf_counter()

    float_list = read_text()
    combs = combinations(float_list, 10)

    for i in combs:
        outcome = sum(i) / 10
        if lower_bound < outcome < higher_bound:
            print(outcome * difference + float_caps[0])
            result_str = " or ".join([f'match(float, "{str(fv)[2:8]}")>=1' for fv in i])
            print(result_str)
            break

    time_end = time.perf_counter()
    time_duration = time_end - time_start

    print(f'Took {time_duration:.3f} seconds')


if __name__ == '__main__':
    main()
