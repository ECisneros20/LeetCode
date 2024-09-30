from typing import List

a = [1, 3]
b = [2]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        pos = (len(nums1) - 1) / 2
        if pos % 1:
            return (nums1[int(pos - 0.5)] + nums1[int(pos + 0.5)]) / 2
        else:
            return nums1[int(pos)]


if __name__ == "__main__":
    obj = Solution()
    print(obj.findMedianSortedArrays(a, b))
