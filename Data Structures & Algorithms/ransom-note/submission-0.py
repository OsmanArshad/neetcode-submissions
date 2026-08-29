class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hash = collections.defaultdict(int)

        for c in magazine:
            magazine_hash[c] += 1
        
        for c in ransomNote:
            if c not in magazine_hash:
                return False
            magazine_hash[c] -= 1
            if magazine_hash[c] < 0:
                return False
        return True