"""
@Author: Time
@Time: 2020-11-05
"""
nums = [1,2,3,1,7,1,55,41,4,6]


# def bubbleSort(list):
#     for j in range(len(list) - 1):
#         for i in range(len(list) - j -1):
#             if list[i] > list[i + 1]:
#                 list[i],list[i + 1] = list[i + 1], list[i]
#     return list

# def dbubbleSort(list):
#
#     for j in range(len(list) - 1):
#         swapped = False
#         for i in range(len(list) -1):
#             if list[i] > list[i + 1]:
#                 list[i],list[i + 1] = list[i + 1], list[i]
#                 swapped = True
#         if swapped:
#             swapped = False
#             for i in range(len(list) - 2, 0, -1):
#                 if list[i] < list[i - 1]:
#                     list[i], list[i - 1] = list[i - 1], list[i]
#                     swapped = True
#         if not swapped:
#             break
#     return list

# def select_sort(list):
#     item = list[:]
#     for i in range(len(item) - 1):
#         min_index = i
#         for j in range(i + 1, len(item)):
#             if item[min_index] > item[j]:
#                 min_index = j
#         item[i],item[min_index] = item[min_index],item[i]
#     return item


# def merge_sort(list):
#     item = list[:]
#     if len(item) < 2:
#         return item
#     mid = len(item) // 2
#     item_left = merge_sort(item[:mid])
#     item_right = merge_sort(item[mid:])
#     return merge(item_left,item_right)
#
# def merge(item1,item2):
#     item = []
#     index1, index2 = 0, 0
#     while index1 < len(item1) and index2 < len(item2):
#         if item1[index1] < item2[index2]:
#             item.append(item1[index1])
#             index1 += 1
#         else:
#             item.append(item2[index2])
#             index2 += 1
#     item += (item1[index1:])
#     item += (item2[index2:])
#     return item

# def quick_sort(list, l, r):
#     if l < r:
#         mid = partition(list, l, r)
#         quick_sort(list, l, mid - 1)
#         quick_sort(list, mid + 1, r)
#
# def partition(list, l, r):
#     pivot = list[r]
#     mid = l
#     for j in range(l, r):
#         if pivot > list[j]:
#             list[mid], list[j] = list[j], list[mid]
#             mid += 1
#     list[mid], list[r] = list[r], list[mid]
#     return mid


# list = quick_sort(nums,0, len(nums) - 1)
#
# print(nums)
N =2
arr = [0] * (N + 1)
arr[0], arr[1] = 0, 1
for i in range(2, N + 1):
    arr[i] = arr[i - 1] + arr[i - 2]
print(arr[N])