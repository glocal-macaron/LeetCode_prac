class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned    and word ]


        counts = collections.defaultdict(int)

        for word in words:
            counts[word] += 1

        return max(counts, key = counts.get)


        

            






        


