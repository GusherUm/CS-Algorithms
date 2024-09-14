def quickSort(nums):

    def func(left, right):

        if len(nums[left: right + 1]) == 1 or len(nums[left: right + 1]) == 0:
            return None

        key = nums[right]
        up, down = -1, -1

        up += 1

        while up <= right:

            if nums[up] <= key:
                down += 1

                if up > down:
                    # swap
                    nums[up], nums[down] = nums[down], nums[up]
                    
                up += 1
            else:
                up += 1

        func(left, down - 1)
        func(down + 1, right)

    func(0, len(nums) - 1)
    return nums

# print(quickSort([5, 3, 8, 9, 1, 8, 3, 5, 4, 4]))
