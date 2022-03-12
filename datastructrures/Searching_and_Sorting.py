from typing import List, Union, Tuple


def binarySearch(search_in: Union[List[int], Tuple[int]], target_value: int) -> int:
    left_ind = 0  # start from 0
    right_ind = len(search_in) - 1  # start from the last index
    mid_ind = 0
    while left_ind <= right_ind:  # as long as the left pointer is less than or at the right pointer keep searching
        mid_ind = (left_ind + right_ind) // 2  # get the mid-point of the array
        mid_value = search_in[mid_ind]  # get the value at the mid-point
        if mid_value == target_value:  # if the value at the mid-point is equal to the target
            return mid_ind  # then return that index
        if mid_value < target_value:  # if value at mid-point is less than the target
            left_ind = mid_ind + 1  # then shift left index to 1 + the mid-index
        else:  # if value at mid-point is more than the target
            right_ind = mid_ind - 1  # then shift right index to 1 - the mid-index
    return -1


if __name__ == "__main__":
    a = [23, 345, 67, 234, 34, 56, 223, 6, 7, 8, 9, 0, 100, 10000]
    a.sort()
    target = 56
    search_index = binarySearch(search_in=a, target_value=target)
    print(f"The index at which the target value resides is {search_index}.")