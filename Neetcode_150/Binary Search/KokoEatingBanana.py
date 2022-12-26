"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
"""

#TC=O(log(max(piles))*len(piles)) SC=O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       
        min_bananas=max(piles)
        start=1 #cannot have 0 bananas
        end=min_bananas

        if h==len(piles):#cause if we have length=hours then it has to eat all piles on eby one, and max it has to eat is the maximum value in piles
            return min_bananas
        while(start<=end):
            mid=(start+end)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/mid)#hours taken to eat p banans if she eats mid no of bananas/ h
            if hours<=h:#it if takes less than 8 hours then add minmum no of bananas to be eaten as minimum of min_bananas and middle value
                min_bananas=min(min_bananas,mid)
                end=mid-1
            else:
                start=mid+1
        return min_bananas


