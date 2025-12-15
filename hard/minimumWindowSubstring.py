from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ===== SETUP PHASE =====
        # Create a frequency map of characters we need to find in t
        d = defaultdict(int)
        for char in t:
            d[char] += 1
        # Example: if t = "ABC", d = {'A': 1, 'B': 1, 'C': 1}
        # Example: if t = "AABC", d = {'A': 2, 'B': 1, 'C': 1}
        
        # formed: counts how many UNIQUE characters have met their required frequency
        # total: number of unique characters we need to satisfy (len of dictionary)
        formed, total = 0, len(d)
        
        # Two pointers for our sliding window
        l = r = 0
        
        # Track the minimum window length found so far
        lens_ans = float('inf')
        
        # Track the actual substring indices for the answer
        subl, subr = 0, 0
        
        # ===== EXPANDING WINDOW (move right pointer) =====
        while r < len(s):
            char = s[r]
            
            # If this character is needed (exists in t)
            if char in d:
                d[char] -= 1  # Decrement count (we "consumed" one occurrence)
                
                # If we've now satisfied this character's requirement
                # (d[char] goes from 1 to 0 or from 2 to 1, etc.)
                if d[char] == 0:
                    formed += 1  # One more unique character is fully satisfied
            
            # ===== CONTRACTING WINDOW (move left pointer) =====
            # Try to shrink window while we still have a valid window
            # Valid window = all required characters are present (formed == total)
            while l <= r and total == formed:
                # Check if this window is smaller than our best so far
                curr_len = r - l + 1
                if curr_len < lens_ans:
                    lens_ans = curr_len
                    subl, subr = l, r + 1  # Save window boundaries (subr is exclusive)
                
                # Try to shrink from left
                char = s[l]
                if char in d:
                    # If this character count is exactly 0, removing it breaks validity
                    if d[char] == 0:
                        formed -= 1  # We're about to lose this character's requirement
                    d[char] += 1  # "Return" this character (increase need count)
                
                l += 1  # Move left pointer right (shrink window)
            
            r += 1  # Always expand right pointer
        
        # ===== RETURN RESULT =====
        # If we never found a valid window, return empty string
        return "" if lens_ans == float("inf") else s[subl:subr]