class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        result = []
        for num in nums:
            tracker[num] = 1 + tracker.get(num, 0)
        track = [[num,freq] for num, freq in tracker.items()]
        track.sort(key=lambda x:x[1], reverse=True)
        result = [item[0] for item in track[:k]]
        return result