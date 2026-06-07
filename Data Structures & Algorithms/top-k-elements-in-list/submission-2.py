class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        result=[]
        for x in nums:
            d[x]=d.get(x,0)+1
        buckets=[[] for _ in range(len(nums)+1)]
        for num, freq in d.items():
            buckets[freq].append(num)
        for f in range(len(buckets)-1,0,-1):
            for num in buckets[f]:
                result.append(num)
                if len(result)==k:
                    return result
