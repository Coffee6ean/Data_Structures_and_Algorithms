"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each 
unique element appears only once. The relative order of the elements should be kept the same. Then return 
the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the unique elements in the order they 
were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
- Return k.
"""

class Solution:

    def remove_duplicates_from_sorted_array(nums:list) -> int:
        l_idx, r_idx = 0, len(nums)-1

        if len(nums) > 1:
            while l_idx <= r_idx:
                if l_idx == 0:
                    l_idx += 1
                    continue

                if nums[l_idx] == nums[l_idx-1]:
                    nums.pop(l_idx)
                    nums.append("_")
                    r_idx -= 1
                else:
                    l_idx += 1

        print(nums)
        return len(nums)-nums.count("_")
    
    def remove_duplicates_from_sorted_array_improved(nums:list) -> int:
        unique = {}

        for item in nums:
            if item in unique:
                unique[item] += 1
            else:
                unique.setdefault(item, 1)

        unique_list = list(unique.keys())

        for i in range(len(unique_list)):
            print(i)
            nums[i] = unique_list[i]

        print(unique_list)

        return len(unique_list)

if __name__ == "__main__":
    """ print(Solution.remove_duplicates_from_sorted_array([1,1,2]))
    print(Solution.remove_duplicates_from_sorted_array([1,1,1]))
    print(Solution.remove_duplicates_from_sorted_array([1,1]))
    print(Solution.remove_duplicates_from_sorted_array([1]))
    print(Solution.remove_duplicates_from_sorted_array([0,0,1,1,1,2,2,3,3,4])) """

    print(Solution.remove_duplicates_from_sorted_array_improved([1,1,2]))
    print(Solution.remove_duplicates_from_sorted_array_improved([1,1,1]))
    print(Solution.remove_duplicates_from_sorted_array_improved([1,1]))
    print(Solution.remove_duplicates_from_sorted_array_improved([1]))
    print(Solution.remove_duplicates_from_sorted_array_improved([0,0,1,1,1,2,2,3,3,4]))