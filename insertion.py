li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30, 1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]
sorted_li = [1, 2, 4, 6, 9, 13, 100, 90000]


def insertion_sort(li, swaps, its=0):
    for i in range(1, len(li)):
        j = i
        its+=1
        while j > 0 and li[j - 1] > li[j]:
            li[j-1], li[j] = li[j], li[j-1]
            j -= 1
            swaps += 1
    print(f"sorted list {li}, there were {swaps} swaps and there were {its} iterations of the loop")

insertion_sort(li, 0)
print(li)

# weston's solution
# check if a list is sorted or not
# def is_sorted(li):
#     for  i in range(len(li) - 1):
#         if li[i] > li[i + 1]:
#             return False
#     return True
# iterations = 0
# def insertion_sort(li):
#     global iterations
#     # iterate over the entire list, loop downward when we find a value that is smaller than what is to the left
#     for index in range(len(li)):
#         # we need to know the current number for comparisons
#         current_number = li[index]
#         # the position sliding back down th list 
#         comparison_position = index -1
#         while comparison_position >= 0 and current_number < li[comparison_position]:
#             # swap the values down while both conditions are met
#             li[comparison_position], li [comparison_position + 1] = li [comparison_position + 1], li[comparison_position]
#             iterations += 1

# print(is_sorted(li))
# insertion_sort(li)
# print(li)
# print(iterations)
