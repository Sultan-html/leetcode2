class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
       
        neznayu = set(jewels)
        
       
        cant = 0
        
    
        for stone in stones:
            if stone in neznayu:
                cant += 1
                
        return cant

sol = Solution()
print(sol.numJewelsInStones("aA", "aAAbbbb"))
print(sol.numJewelsInStones("z", "ZZ"))     