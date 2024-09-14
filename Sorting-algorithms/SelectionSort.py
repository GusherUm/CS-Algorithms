# In bubble sort --> Maximum element goes at last during each iteration
# In selection sort --> Minimum element goes at front during each iteration

def selectionSort(nums):

    for i in range(len(nums)):
        mn = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[mn]:
                mn = j

        nums[i], nums[mn] = nums[mn], nums[i]

    return nums

# print(selectionSort([5, 3, 8, 9, 1, 8, 3, 5, 4, 4]))

# Time complexity: O(n^2)
# Space complexity: O(1)