def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersection = find_intersection(list1, list2)
print(intersection)  # Output: [3, 4]


def find_simetric_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.symmetric_difference(set2))

list1 = [1, 2, 3]
list2 = [1, 5, 3]
difference = find_simetric_difference(list1, list2)
print(difference)  # Output: [2, 5]


print(list1.index(2))  # Output: 1
