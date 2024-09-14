# Playing cards scenario

def insertionSort(nums):

    for i in range(1, len(nums)):
        take = nums[i]
        j = i - 1

        while j >= 0 and take < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = take

    return nums

print(insertionSort([5, 3, 8, 9, 1, 8, 3, 5, 4, 4]))

# Time complexity : O(n^2)
# Space complexity: O(1); Thus Inplace