'''
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:
Input: nums = [0]
Output: [[],[0]]
'''
class BracktrackingSolutions:
    # Beats 98% users with Python
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(curr_list, curr_i):
            print(f"backtrack({curr_list}, {curr_i})")
            res.append(curr_list.copy())
            # backtrack for every number and incremnet the index
            for i in range(curr_i, len(nums)):
                backtrack(curr_list + [nums[i]], i+1)

        backtrack([], 0)
        return res