# Divide and conquer approach

def mergeSort(nums):

    if len(nums) > 1:

        m = len(nums)//2
        l, r = nums[:m], nums[m:]

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                nums[k] = l[i]
                i += 1
            else:
                nums[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            nums[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            nums[k] = r[j]
            j += 1
            k += 1

    return nums

# print(mergeSort([5, 3, 8, 9, 1, 8, 3, 5, 4, 4]))