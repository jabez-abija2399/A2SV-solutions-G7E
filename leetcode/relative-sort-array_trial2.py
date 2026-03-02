class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result = []
        for num in arr2:
            while num in arr1:
                result.append(num)
                arr1.remove(num)
        
        arr1.sort()
        result.extend(arr1)
        
        return result
            


        
        