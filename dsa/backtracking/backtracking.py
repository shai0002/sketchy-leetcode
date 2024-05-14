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
from typing import List
class BracktrackingSolutions:
    # Beats 98% users with Python
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 78. Subsets
        res = []
        def backtrack(curr_list, curr_i):
            print(f"backtrack({curr_list}, {curr_i})")
            res.append(curr_list.copy())
            # backtrack for every number and incremnet the index
            for i in range(curr_i, len(nums)):
                backtrack(curr_list + [nums[i]], i+1)

        backtrack([], 0)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        # 17. Letter Combinations of a Phone Number
        if not digits:
            return []
        alphanum = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []

        def backtrack(curr_str, i):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            for char in alphanum[digits[i]]:
                backtrack(curr_str + char, i + 1)

        backtrack("", 0)
        return res

    def generateParenthesis(self, n: int) -> List[str]:
        # 22. Generate Parentheses
        def backtrack(res, curr_str, open_p, close_p, n):

            if len(curr_str) == 2 * n:
                res.append(curr_str)
                return
            # Case to add a "("
            if open_p < n:
                backtrack(res, curr_str + "(", open_p + 1, close_p, n)
            # Case to add a ")"
            if close_p < open_p:
                backtrack(res, curr_str + ")", open_p, close_p + 1, n)

        res = []
        backtrack(res, "", 0, 0, n)
        return res
