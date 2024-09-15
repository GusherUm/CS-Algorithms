def RecurInsertionSort(nums, n):
    
    if n > len(nums) - 1:
        return

    take = nums[n]
    j = n - 1

    while j >= 0 and take < nums[j]:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = take

    RecurInsertionSort(nums, n + 1)

nums = [6, 3, 8, 4, 8, 8, 3, 8, 8, 4]

RecurInsertionSort(nums, 1)
print(nums)