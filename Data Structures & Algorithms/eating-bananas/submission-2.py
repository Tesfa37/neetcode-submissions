class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxk = max(piles)
        left = 1
        res = float('infinity')
        while left <= maxk:
            middle = (left + maxk)//2
            sumit = 0
            for i in piles:
                div = math.ceil(i/middle)
                sumit += div
            if sumit <= h:
                res = min(res, middle)
                maxk = middle - 1
            else:
                left = middle + 1
        return res
        