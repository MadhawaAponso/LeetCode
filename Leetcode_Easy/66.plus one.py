class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s= ""
        for x in digits:
            s+=str(x)
        new_s = str(int(s)+1)
        return [int(x) for x in new_s]