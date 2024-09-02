'''Given two strings ransomNote and magazine, return true 
if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_list=list(magazine)
        for char in ransomNote:
            if char in m_list:
                m_list.remove(char)
            else:
                return False
        return True

            

        
ransomNote = "baa"
magazine = "aab"
res=Solution()
result=res.canConstruct(ransomNote,magazine)
print(result)


# st=set(ransomNote)
#         for i in st:
#             if magazine.count(i)<ransomNote.count(i):
#                 return False
#                 break
#         return True