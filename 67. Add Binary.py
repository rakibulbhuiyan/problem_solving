class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=bin(int(a,2)+int(b,2))
        return c[2:]


a = "11"
b = "1"
res=Solution()
print(res.addBinary(a,b))