class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nxGr = {}
        for num in nums2:
            while stack and stack[-1] < num:
                prev = stack.pop()
                nxGr[prev] = num
            stack.append(num)
        
        #  4 3 1
        # -1 -1 4 3
        for num in stack:
            nxGr[num] = -1
        
        return [nxGr[num] for num in nums1]

        