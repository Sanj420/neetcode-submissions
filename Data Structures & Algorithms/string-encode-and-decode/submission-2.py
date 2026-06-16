class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"__43kndgsI#46n__{s}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        return s.split("__43kndgsI#46n__")[1:]
