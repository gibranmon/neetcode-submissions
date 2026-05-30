class Solution:

    def encode(self, strs: List[str]) -> str | None:
        if len(strs) == 0:
            return "None"
        encoded_string = "|||".join(strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        original_strings = s.split("|||")
        return original_strings
