from typing import List


def remove_duplicates(lst: List[int]) -> List[int]:
    cleaned_list = []
    for item in lst:
        if item not in cleaned_list:
            cleaned_list.append(item)
    return cleaned_list


def remove_duplicates_v2(lst: List[int]) -> List[int]:
    return list(set(lst))

without_duplicates = remove_duplicates([1, 2, 3, 2, 1, 4, 5, 4])
print(without_duplicates)  # Output [1, 2, 3, 4, 5]

without_duplicates = remove_duplicates_v2([1, 2, 3, 2, 1, 4, 5, 4])
print(without_duplicates)  # Output [1, 2, 3, 4, 5]
