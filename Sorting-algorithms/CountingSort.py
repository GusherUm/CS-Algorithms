# Range of the array elements should be given
# Let's assume all the elements are in the range of 10 (0 to 9) or max element is 9

def CountingSort(nums):

    res, count = [0]*(len(nums)), [0]*(10)   # Count array of size: (max + 1)

    for i in range(len(nums)):
        count[nums[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = len(nums) - 1

    # Traverse from the end of the input array to preserve the order of the equal elements: Stability

    while i >= 0:
        res[count[nums[i]] - 1] = nums[i]
        count[nums[i]] -= 1 
        i -= 1

    return res

# print(CountingSort([5, 3, 8, 9, 1, 8, 3, 5, 4, 4]))

# Time complexity :   O(n + k)
# Space complexity:   O(n)
