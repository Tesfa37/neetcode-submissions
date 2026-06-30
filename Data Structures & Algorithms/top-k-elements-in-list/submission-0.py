class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq ={}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        Listfreq = list(freq.items())
        Listfreq.sort(key=lambda x:x[1], reverse=True)
        finallist = []
        for i in range(k):
            finallist.append(Listfreq[i][0])
        # for i, j in freq.items():
        return finallist
            