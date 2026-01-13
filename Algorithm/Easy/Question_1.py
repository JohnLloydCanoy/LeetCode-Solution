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
    