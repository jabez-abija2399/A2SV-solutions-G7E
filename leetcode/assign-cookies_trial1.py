class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
         g.sort()
        s.sort()

        i = 0   # child pointer
        j = 0   # cookie pointer
        satisfied = 0

        # try to satisfy children in order
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:      # cookie satisfies child
                satisfied += 1
                i += 1           # move to next child
                j += 1           # use this cookie
            else:
                j += 1           # cookie too small → try next one
        
        return satisfied

✔ Example Walkthrough
Input:

g = [1,2,3]
s = [1,1]

After sorting:

g = [1,2,3]
s = [1,1]

Steps:

    s[0] = 1 satisfies g[0] = 1 → satisfied = 1

    s[1] = 1 does NOT satisfy g[1] = 2 → skip cookie

    No more cookies → return 1

✔ Why this is BEST?
Method	Time	Space	Why
Greedy (sorting + two pointers)	O(n log n)	O(1)	Optimal, simplest
Brute force	O(n²)	O(1)	Too slow for large inputs
Hashing / DP	❌	❌	Not needed

Greedy is mathematically optimal for this problem.

If you want, I can also show:
✅ brute force approach
✅ diagram explanation
✅ dry run visually

Just tell me!
You said:
1365. How Many Numbers Are Smaller Than the Current Number
Solved
Easy
Topics
premium lock iconCompanies
Hint

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]

 

Constraints:

    2 <= nums.length <= 500
    0 <= nums[i] <= 100

 
ChatGPT said:

Here is a clear explanation of the multiple solution methods for this problem — from brute force to the most efficient.
This is one of the BEST problems to learn different approaches.
🔥 Problem Summary (Simple English)

Given an array nums, for each element nums[i], count how many numbers in the array are strictly smaller than it.

Return an array with those counts.
✅ Solution 1 — Brute Force (Double Loop)
✔ Time: O(n²)
✔ Space: O(1)
Idea:

For each element nums[i], loop through every nums[j] and count how many are smaller.
Steps:

    For each index i

        Set count = 0

        Loop j from 0 to n-1

        If nums[j] < nums[i], increase count

    Store count in result

Code:

def smallerNumbersThanCurrent(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result

👍 Easy to understand
👎 Slow for large arrays
✅ Solution 2 — Sorting + Hash Map (More Efficient)
✔ Time: O(n log n)
✔ Space: O(n)
Idea:

    Sort the array.

    For each number, the first time it appears in sorted array, its index = how many numbers are smaller.

    Store index in a hash map to avoid duplicates.

    Build the answer using the map.

Why it works:

    Sorting puts all smaller elements before larger elements.

    Index in sorted list = count of smaller numbers.

Steps:

If nums = [8,1,2,2,3]:

Sorted → [1,2,2,3,8]

Map becomes:

1 → 0
2 → 1
3 → 3
8 → 4

Code:

def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    map_index = {}

    for i, num in enumerate(sorted_nums):
        if num not in map_index:    # record only first occurrence
            map_index[num] = i

    return [map_index[num] for num in nums]

👍 Efficient
👍 Handles duplicates well
👎 Needs extra space
✅ Solution 3 — Counting Sort / Frequency Array (BEST)
✔ Time: O(n + maxNum) → O(n) because maxNum ≤ 100
✔ Space: O(101) → constant space → O(1)
Why it’s best:

    nums[i] is between 0 and 100 → very small range

    We can count frequencies of all numbers

    Build prefix sum → number of elements smaller than each value

Steps:

    Create a frequency array of size 101
    freq[x] = count of x in nums

    Convert it to prefix sum
    Now freq[x] = total numbers < x

    Build the answer using freq

Example:

nums = [8,1,2,2,3]

freq count:

1 → 1
2 → 2
3 → 1
8 → 1

prefix sum (how many numbers < x):

freq[1] = 0
freq[2] = 1
freq[3] = 3
freq[8] = 4

Code:

def smallerNumbersThanCurrent(nums):
    freq = [0] * 101
    
    # count frequencies
    for num in nums:
        freq[num] += 1
    
    # prefix sum
    for i in range(1, 101):
        freq[i] += freq[i-1]
    
    result = []
    for num in nums:
        if num == 0:
            result.append(0)
        else:
            result.append(freq[num-1])
    
    return result

👍 BEST performance
👍 O(1) extra memory
👍 Fastest for large inputs
✔ Summary Table
Method	Time	Space	Difficulty	Notes
Brute force	O(n²)	O(1)	Easy	Compare every pair
Sorting + Hash Map	O(n log n)	O(n)	Medium	Good practical solution
Frequency Array (Counting Sort)	O(n)	O(1)	Medium	⭐ BEST solution
Want me to:

✅ Explain how counting sort works visually?
✅ Show step-by-step dry run for any method?
Just tell me!


        g.sort()
        s.sort()

        i = 0   
        j = 0   
        satisfied = 0

        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:      
                satisfied += 1
                i += 1           
                j += 1          
            else:
                j += 1          
        return satisfied
