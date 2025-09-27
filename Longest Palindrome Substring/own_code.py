class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 문자열 처리시 없을 때도 항상 처리해야함
        if not s:
            return ""
        pali_dict = collections.defaultdict(int)

        # 슬라이싱 할건지, 인덱스로 검색할 건지에 따른 range의 범위 변화
        # 여기선 첫 반복문이 슬라이싱의 첫부분, 두 번째 반복문이 슬라이싱의 두번째 부분임.
        for i in range(len(s)):
            for k in range(i + 1, len(s) + 1):
                origin = s[i:k]
                palin = origin[::-1]
                if origin == palin:
                    pali_dict[origin] = len(origin)

        cnt = Counter(pali_dict)

        return cnt.most_common(1)[0][0]
