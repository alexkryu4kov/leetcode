def number_of_subarrays(n: int) -> int:
    return int((n * (n+1)) / 2)


def count_subarrays(array: list[int], l: int, r: int) -> int:
    less_elems = 0
    all_elems = 0
    s = 0

    for elem in array:
        if elem < l:
            less_elems += 1
            all_elems += 1
        elif l <= elem < r:
            all_elems += 1
        else:
            print('elem ', elem)
            print(all_elems)
            print(less_elems)
            s += number_of_subarrays(all_elems) - number_of_subarrays(less_elems)
            less_elems = 0
            all_elems = 0
    s += number_of_subarrays(all_elems) - number_of_subarrays(less_elems)
    return s


print(count_subarrays([2, 0, 11, 3, 0], 1, 10))
