class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

              
        """
        first last seaat
        first seat add
        last + 1 seat
        dif[1] = seat
        dif[2+1]
        """  
                ans = [0] * (n + 1)      
        for first , last, seat in bookings:
            ans[first - 1] += seat
            ans[last] -= seat

        res = [ans[0]]
        running_sum = ans[0]
        for i in range(1, len(ans)):
            running_sum += ans[i]
            res.append(running_sum)
        
        res.pop()
        return res  