"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
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

    def three_sum(nums: list) -> list:
        result = []
        sorted_list = Solution.merge_sort(nums)
        
        for idx, item in enumerate(sorted_list):
            if idx > 0 and item == sorted_list[idx-1]:
                continue
            
            l_idx, r_idx = idx+1, len(sorted_list)-1
            
            while l_idx < r_idx:
                threeSum = sorted_list[l_idx] + sorted_list[r_idx] + item
                
                if threeSum > 0:
                    r_idx -= 1
                elif threeSum < 0:
                    l_idx += 1
                else:
                    result.append([item, sorted_list[l_idx], sorted_list[r_idx]])
                    l_idx += 1
                    r_idx -= 1
                    
                    while l_idx < r_idx and sorted_list[l_idx] == sorted_list[l_idx-1]:
                        l_idx += 1
                    while l_idx < r_idx and sorted_list[r_idx] == sorted_list[r_idx+1]:
                        r_idx -= 1
        
        return result
    
    def three_sum_test(nums: list) -> list:
        sorted_list = sorted(nums)
        result = []
        n = len(nums)

        if n < 3 or not sorted_list: return result

        for i in range(n-2):
            if i > 0 and sorted_list[i] == sorted_list[i-1]:
                continue

            l_idx, r_idx = i+1, n-1
            
            while l_idx < r_idx:
                threeSum = sorted_list[l_idx] + sorted_list[r_idx] + sorted_list[i]
                
                if threeSum > 0:
                    r_idx -= 1
                elif threeSum < 0:
                    l_idx += 1
                else:
                    result.append([sorted_list[i], sorted_list[l_idx], sorted_list[r_idx]])
                    l_idx += 1
                    r_idx -= 1
                    
                    while l_idx < r_idx and sorted_list[l_idx] == sorted_list[l_idx-1]:
                        l_idx += 1
                    while l_idx < r_idx and sorted_list[r_idx] == sorted_list[r_idx+1]:
                        r_idx -= 1
        
        return result


if __name__ == "__main__":
    print(Solution.three_sum([-1,0,1,2,-1,-4]))
    print(Solution.three_sum_test([-1,0,1,2,-1,-4]))