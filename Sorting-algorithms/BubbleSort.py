def bubbleSort(nums):

    # Repeated swapping

    for i in range(len(nums)):
        swap = False
        for j in range(0, len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                swap = True

        if swap is False:
            return nums

    return nums

# print(bubbleSort([5, 3, 8, 9, 1, 8, 3, 5, 4, 4]))