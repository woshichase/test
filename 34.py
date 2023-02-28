def judge(nums,target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = int((left+right)/2)
        guess = nums[mid]
        if guess == target:
            right = mid
        elif guess > target:
            right = mid-1
        else:
            left = mid + 1
    result_l = left

    left = 0 # or left
    right = len(nums) - 1
    while left <= right: #here must add =
        mid = int((left+right)/2)
        guess = nums[mid]
        if guess == target:
            left = mid+1 # +1?
        elif guess > target:
            right = mid -1
        else:
            left = mid + 1
    result_r = right
    return [result_l,result_r]


nums = [5,5,6]
target = 5
print(judge(nums,target))

