class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = list()
        digit = list()

        for log in logs:
            # split은 새로운 리스트를 생성함
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        # 람다의 기준을 넘겨줄 때 튜플 사용, -x 로 내림차순 표현 가능
        letter.sort(key = lambda x: (x.split()[1:], x.split()[0]))

        return letter + digit