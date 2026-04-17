class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        base = [0] * 26
        
        # Count chars frequency
        for ch in chars:
            base[ord(ch) - ord('a')] += 1
        
        total = 0
        
        for word in words:
            freq = [0] * 26
            good = True
            
            for ch in word:
                idx = ord(ch) - ord('a')
                freq[idx] += 1
                
                if freq[idx] > base[idx]:
                    good = False
                    break
            
            if good:
                total += len(word)
        
        return total
        