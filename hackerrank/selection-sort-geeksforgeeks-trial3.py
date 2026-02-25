class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        
        for i in range(n-1):
            minNum = i
            
            for j in range(i+1, n):
                if arr[j] < arr[minNum]:
                    minNum = j
            arr[i], arr[minNum] = arr[minNum], arr[i]
        return arr
