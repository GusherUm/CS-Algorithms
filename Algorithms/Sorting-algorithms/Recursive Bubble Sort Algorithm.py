# def bubbleSort(nums):
#     # Compares each adjacent element

#     for i in range(len(nums)):
#         swap = False
#         for j in range(len(nums) - 1):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#                 swap = True
#         if not swap:
#             break

#     return nums

# print(bubbleSort([6, 3, 8, 4, 8, 8, 3, 8, 8, 4]))

def RecurBubbleSort(nums, n):

    if n == 1:
        return

    swap = False

    for j in range(n - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swap = True

    if not swap:
        return

    RecurBubbleSort(nums, n - 1)

nums = [6, 3, 8, 4, 8, 8, 3, 8, 8, 4]
RecurBubbleSort(nums, 10)

print(nums)