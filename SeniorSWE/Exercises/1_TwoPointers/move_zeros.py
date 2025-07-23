"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the 
non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:

    def move_zeros(nums:list) -> None:
        l_idx, r_idx = 0, len(nums)-1
        zeros_found_idx = []

        while l_idx < r_idx:
            if nums[l_idx] == 0:
                zeros_found_idx.append(l_idx)
            
            if nums[r_idx] == 0:
                zeros_found_idx.append(r_idx)
            
            if nums[l_idx] < nums[r_idx]:
                r_idx -= 1
            else:
                l_idx += 1

        zeros_found_idx_reverse = sorted(list(set(zeros_found_idx)))[::-1]

        for idx in zeros_found_idx_reverse:
            nums.append(0)
            nums.pop(idx)
        
        print(nums)

    def move_zeros_improved(nums:list) -> None:
        l_idx, r_idx = 0, len(nums)-1

        while l_idx < r_idx:
            if nums[l_idx] == 0:
                nums.pop(l_idx)
                nums.append(0)
                r_idx -= 1
            else:
                l_idx += 1

        print(nums)


if __name__ == "__main__":
    Solution.move_zeros_improved([0,1,0,3,12])
    Solution.move_zeros_improved([0])