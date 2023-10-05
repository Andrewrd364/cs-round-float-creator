from itertools import combinations

lower_bound = 0.594594583
higher_bound = 0.59459459


def read_text():
    with open('input.txt', 'r') as file:
        filtered_text = []
        for i in file.readlines():
            if i.find("Float:") != -1:
                filtered_text.append(round(float(i.replace("Float: ", "").replace("\n", "")), 9))
            if len(filtered_text) == 34:
                break

    with open('input.txt', 'w') as file:
        pass

    return filtered_text


def is_within_bounds(combination):
    avg = sum(combination) / 10
    return lower_bound < avg < higher_bound


def main():
    valid_combinations = filter(is_within_bounds, combinations(read_text(), 10))

    for combination in valid_combinations:
        avg = sum(combination) / 10
        print(avg)
        result_str = " or ".join([f'match(float, "{str(fv)[2:8]}")>=1' for fv in combination])
        print(result_str)


if __name__ == '__main__':
    main()
