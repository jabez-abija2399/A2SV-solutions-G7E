class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """

        if num > 0:
            listNum = [num for num in str(num)]
            listNum.sort()
            
            for i, d in enumerate(listNum):
                if d != '0':
                    listNum[0], listNum[i] = listNum[i], listNum[0]
                    break
                
            return int("".join(listNum))
        else:
            listNum = [num for num in str(-num)]
            listNum.sort(reverse = True)
            return -int("".join(listNum))
                