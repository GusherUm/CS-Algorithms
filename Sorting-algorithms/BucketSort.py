def insertionSort(nums):

    for i in range(1, len(nums)):
        take = nums[i]
        j = i - 1

        while j >= 0 and take < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = take

    return nums

def bucketSort(nums):
    
    bucket = [[] for _ in range(10)]

    for i in range(len(nums)):
        index = int(10*nums[i])
        bucket[index].append(nums[i])

    # Sort each bucket using insertion sort or any sorting algorithm as you wish
        
    for i in range(len(bucket)):
        bucket[i] = insertionSort(bucket[i])

    k = 0

    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            nums[k] = bucket[i][j]
            k += 1
        
    return nums

# print(bucketSort([0.5, 0.3, 0.8, 0.9, 0.1, 0.8, 0.3, 0.5, 0.4, 0.4]))