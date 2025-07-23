"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how 
much water it can trap after raining.
"""

class Solution:

    def merge_sort(arr:list) -> list:
        if len(arr) <= 1:
            return arr
        
        M = len(arr) // 2
        L = arr[:M]
        R = arr[M:]

        L, R = Solution.merge_sort(L), Solution.merge_sort(R)
        i = j = 0
        index = 0
        A = [0] * (len(L) + len(R))

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[index] = L[i]
                i += 1
            else:
                A[index] = R[j]
                j += 1
            index += 1

        while i < len(L):
            A[index] = L[i]
            i += 1
            index += 1

        while j < len(R):
            A[index] = R[j]
            j += 1
            index += 1

        return A

    def trap_rain(heights: list) -> int:
        if not heights: return 0

        l_idx, r_idx = 0, len(heights)-1
        max_height_l, max_height_r = heights[l_idx], heights[r_idx]
        result = 0

        while l_idx < r_idx: 
            if max_height_l < max_height_r:
                l_idx += 1
                max_height_l = max(max_height_l, heights[l_idx])
                result += max_height_l - heights[l_idx]
            else:
                r_idx -= 1
                max_height_r = max(max_height_r, heights[r_idx])
                result += max_height_r - heights[r_idx]

        return result
    
if __name__ == "__main__":
    print(Solution.trap_rain([0,1,0,2,1,0,1,3,2,1,2,1]))