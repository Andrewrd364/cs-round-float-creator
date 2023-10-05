from itertools import combinations
import struct


def get_ieee754(value: float) -> float:
    temp = struct.pack('!f', value)
    result = struct.unpack('!f', temp)[0]
    return result


exp_float = 0.5
float_caps = [0.06, 0.8]

lower_bound = exp_float
higher_bound = exp_float
while get_ieee754(lower_bound) == exp_float:
    lower_bound -= 0.000000000001
lower_bound += 0.00000000001
while get_ieee754(higher_bound) == exp_float:
    higher_bound += 0.000000000001
higher_bound -= 0.00000000001

difference = float_caps[1] - float_caps[0]


def read_text():
    with open('input.txt', 'r') as file:
        filtered_text = []
        for i in file.readlines():
            if i.find("Float:") != -1:
                filtered_text.append(get_ieee754(float(i.replace("Float: ", "").replace("\n", ""))))
            if len(filtered_text) == 34:
                break

    with open('input.txt', 'w') as file:
        pass

    return filtered_text


def is_within_bounds(combination):
    outcome = (difference * get_ieee754(sum(combination) / 10)) + float_caps[0]
    return lower_bound < outcome < higher_bound


def main():
    valid_combinations = filter(is_within_bounds, combinations(read_text(), 10))

    for combination in valid_combinations:
        avg = sum(combination) / 10
        outcome = ((float_caps[1] - float_caps[0]) * avg) + float_caps[0]
        print(outcome)
        result_str = " or ".join([f'match(float, "{str(fv)[2:7]}")>=1' for fv in combination])
        print(result_str)


if __name__ == '__main__':
    main()
