class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)
        matches = 0
        left = 0
        min_len = (0, len(s) + 1)
        for right, c in enumerate(s):
            if c in t_counts:
                t_counts[c] -= 1
                if t_counts[c] == 0:
                    matches += 1
                while s[left] not in t_counts or t_counts[s[left]] < 0:
                    if s[left] in t_counts:
                        t_counts[s[left]] += 1
                    left += 1
            
            if matches == len(t_counts) and right - left < min_len[1] - min_len[0]:
                min_len = (left, right)

        return s[min_len[0]: min_len[1] + 1] if min_len[1] - min_len[0] < len(s) else ""