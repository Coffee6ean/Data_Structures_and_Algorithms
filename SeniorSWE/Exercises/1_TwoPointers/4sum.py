"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], 
nums[d]] such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
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
    
    def four_sum(nums, target):
        sorted_list = Solution.merge_sort(nums)
        result = []
        n = len(sorted_list)
        
        if n < 4: return result
        
        for i in range(n - 3):
            if i > 0 and sorted_list[i] == sorted_list[i-1]:
                continue
                
            for j in range(i + 1, n - 2):
                if j > i + 1 and sorted_list[j] == sorted_list[j-1]:
                    continue
                    
                left, right = j + 1, n - 1
                
                while left < right:
                    current_sum = sorted_list[i] + sorted_list[j] + sorted_list[left] + sorted_list[right]
                    
                    if current_sum < target:
                        left += 1
                    elif current_sum > target:
                        right -= 1
                    else:
                        result.append([sorted_list[i], sorted_list[j], sorted_list[left], sorted_list[right]])
                        
                        while left < right and sorted_list[left] == sorted_list[left + 1]:
                            left += 1
                        while left < right and sorted_list[right] == sorted_list[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                        
        return result

if __name__ == "__main__":
    print(Solution.four_sum([1,0,-1,0,-2,2], 0))
    print(Solution.four_sum([-3,-1,0,2,4,5], 0))