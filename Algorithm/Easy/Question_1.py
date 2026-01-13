# Remove Duplicates from Sorted Array
nums = []

nums.append(1)
nums.append(2)
nums.append(3)
nums.append(3)
nums.append(4)
print(nums)  # Output: [1, 2, 3, 3, 4]

def remove_duplicates(nums):
    if not nums:
        return 0 
    elif len(nums) == 1:
        return 1
    else:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
length = remove_duplicates(nums)
print(length)  # Output: 4
print(nums[:length])  # Output: [1, 2, 3, 4]

#time complexity: O(n)
#space complexity: O(1)