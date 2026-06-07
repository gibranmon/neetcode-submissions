import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_string = re.sub(r'[^0-9a-zA-Z]', '', s)
        
        normalized_string = normalized_string.lower()
        
        first = 0
        last = len(normalized_string) - 1
        while first < len(normalized_string) // 2:
            if normalized_string[first] != normalized_string[last]:
                return False
            first += 1
            last -= 1

        return True
        