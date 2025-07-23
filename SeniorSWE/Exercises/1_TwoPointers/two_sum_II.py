"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers 
such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of 
length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""

class Solution:

    def two_sum(numbers:list, target:int) -> list:
        l_idx, r_idx = 0, len(numbers)-1

        while l_idx < r_idx:
            if (numbers[l_idx] + numbers[r_idx]) > target:
                r_idx -= 1
            elif (numbers[l_idx] + numbers[r_idx]) < target:
                l_idx += 1
            else:
                return [l_idx+1, r_idx+1]
            
        return []


if __name__ == "__main__":
    print(Solution.two_sum([1,3,4,5,7,10,11], 9))

    """
    Problem: Two Sum II (167) - Two Pointers
    Pattern: Opposite Direction Two Pointers
    Key Insight: Sorted array + target sum = move pointers based on current sum
    Template: left = 0, right = n-1; while left < right: adjust based on sum
    Recognition: "Sorted array" + "find pair/target" = Two Pointers
    """