"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum 
is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""

class Solution:

    def three_sum(x:int, y:int, z:int) -> int:
        return x+y+z

    def three_sum_closest(nums:list, target:int):
        if len(nums) < 3: return 0
            
        sorted_list = sorted(nums)
        closest_sum = sorted_list[0] + sorted_list[1] + sorted_list[2]
        
        for idx in range(len(sorted_list) - 2):
            l_idx, r_idx = idx + 1, len(sorted_list) - 1
            
            while l_idx < r_idx:
                curr_sum = sorted_list[idx] + sorted_list[l_idx] + sorted_list[r_idx]
                
                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum
                
                if curr_sum < target:
                    l_idx += 1
                elif curr_sum > target:
                    r_idx -= 1
                else:
                    return target
                
        return closest_sum


if __name__ == "__main__":
    print(Solution.three_sum_closest([-1,2,1,-4], 1))
    print(Solution.three_sum_closest([0,0,0], 1))
    print(Solution.three_sum_closest([1,1,1,0], 100))
    print(Solution.three_sum_closest([4,0,5,-5,3,3,0,-4,-5], -2))