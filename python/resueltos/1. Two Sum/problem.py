from typing import List

a = [2, 7, 11, 15]
b = 9


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for pos1, i in enumerate(nums):
            aux = nums[pos1 + 1 :]
            for pos2, j in enumerate(aux):
                if i + j == target:
                    return [pos1, pos1 + pos2 + 1]


if __name__ == "__main__":
    obj = Solution()
    print(obj.twoSum(a, b))
