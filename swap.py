swap = [1, 2, 'four', 3]

# swapping easily in python
# order things are = order the way ww want it to be
swap[2], swap[3] = swap[3], swap[2]

# print(swap)

li = [24, 34, 31, 34, 23, 15, 18, 49, 25, 30, 48, 4, 3, 13, 27, 16, 5, 25, 35, 4, 7, 6, 10, 47, 30, 1, 42, 21, 12, 21, 35, 43, 25, 18, 12, 25, 27, 25, 47, 4, 27, 13, 29, 43, 33, 34, 23, 22, 28, 38]
sorted_li = [1, 2, 4, 6, 9, 13, 100, 90000]


def list_sort(li, swap, its=1):
    run = 0
 
    for i in range(len(li) -1):
        if li[i] > li[i + 1]:
            li[i], li[i + 1] = li[i + 1], li[i]
            run += 1
            swap += 1

    if run == 0:
        print(f"sorted list {li}, there were {swap} swaps and there were {its} iterations of the loop")
    else:
        its += 1
        list_sort(li, swap, its)
            
list_sort(li, 0)

# weston's solution
# check if a list is sorted or not
# def is_sorted(li):
#     for  i in range(len(li) - 1):
#         if li[i] > li[i + 1]:
#             return False
#     return True

# def bubble_sort(li):
#     # flag that tells us if the list is sorted
#     has_swapped = True

#     while has_swapped:
#         # assume that no swap will be made
#         has_swapped = False
#         for i in range(len(li) - 1):
#             # check the neighbors values -- if current is > one to the right -- make swap
#             if li[i] > li[i + 1]:
#                 # wrong order -- need to swap
#                 li[i], li[i + 1] = li[i + 1], li[i] 
#                 has_swapped = True

# bubble_sort(li)
# print(is_sorted(li))
# print(li)

# Hoan's udemy solution
# def is_sorted(li):
#     sorted = False
#     for n in range(len(li) - 1, 0, -1):
#         for i in range(n):
#             if li[i] > li[i + 1]:
#                 sorted = True
#                 li[i], li[i + 1] = li[i + 1], li[i]
#     if not sorted:
#         return  

