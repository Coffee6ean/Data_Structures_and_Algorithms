"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
 of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution:

    def maxArea(heights:list):
        l_idx, r_idx = 0, len(heights)-1
        result = 0

        while l_idx < r_idx:
            width = r_idx - l_idx
            threshold_height = min(heights[l_idx], heights[r_idx])
            area = (width*threshold_height)

            result = max(result, area)
            
            if (heights[l_idx] > heights[r_idx]):
                r_idx -= 1
            else:
                l_idx += 1

        
        return result
    

if __name__ == "__main__":
    print(Solution.maxArea([1,8,6,2,5,4,8,3,7]))

    """
    Problem: TContainer With Most Water (11) - Two Pointers
    Pattern: Opposite Direction Two Pointers; shift smaller of two
    Key Insight: Unsorted array + target sum = move pointers based on max area
    Template: left = 0, right = n-1; while left < right: adjust based on max area
    Recognition: "Unsorted array" + "find pair/target" = Two Pointers
    """