class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        n=len(citations)
        count=0
        for i in range(1,n):
            if citations[i] >= i:
                count =i+1
        return count



paper=[3,0,6,1,5]
r=Solution()
ans=r.hIndex(paper)
print(ans)