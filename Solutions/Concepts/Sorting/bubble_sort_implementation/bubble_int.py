def sort(nums):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                current = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = current
                swaps += 1
        
    return nums