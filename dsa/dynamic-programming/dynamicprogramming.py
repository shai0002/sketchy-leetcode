class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     dp = []
    def trap(self, height: List[int]) -> int:
        '''
        we'll build two arrays one will have max of all elements to the right of current index
        other will have max of all elements to the left of curr index'''
        l_max, r_max = [0], [0] * len(height)
        res_sum = 0
        for i in range(1, len(height)):
            if height[i - 1] > l_max[-1]:
                l_max.append(height[i - 1])
            else:
                l_max.append(l_max[-1])

        for i in range(len(height) - 2, -1, -1):
            if height[i + 1] > r_max[i + 1]:
                r_max[i] = height[i + 1]
            else:
                r_max[i] = r_max[i + 1]

        for i in range(len(height)):
            diff = min(l_max[i], r_max[i]) - height[i]
            if diff > 0:
                res_sum += diff

        return res_sum