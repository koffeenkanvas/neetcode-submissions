class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        result=[]
        for x in nums:
            d[x]=d.get(x,0)+1
        
        items = sorted(d.items(), key=lambda x: x[1], reverse=True) 
        for ans in items[:k]:
            result.append(ans[0])
        return result
