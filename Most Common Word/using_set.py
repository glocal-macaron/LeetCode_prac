from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        banned_set = set((b.lower() for b in banned))
        cnt = Counter((s.lower() for s in re.split(r"[!?',;. ]", paragraph) if s.lower() not in banned_set and s))
        return cnt.most_common(1)[0][0]