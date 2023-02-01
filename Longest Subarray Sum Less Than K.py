def longest_sum(nums, target):
    left = 0
    answer = 0
    for right in range(len(nums)):
        if left >= right:
            continue
        if sum(nums[left:right]) <= target:
            temp_answer = right - left
            if temp_answer > answer:
                answer = temp_answer
        else:
            left += 1
    return answer


print(longest_sum([3, 1, 2, 7, 4, 2, 1, 1, 5], 8))
