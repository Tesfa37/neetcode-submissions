class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            maxHeap.append(-num)
        heapq.heapify(maxHeap)
        while k > 0:
            x = heapq.heappop(maxHeap)
            k -= 1
        return -x