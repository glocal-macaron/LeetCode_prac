class Solution:
    def trap(self, height: List[int]) -> int:
        volumes = 0
        stack = []

        for i in range(len(height)):

            while stack and height[i] > height[stack[-1]]:
                
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                waters = min(height[stack[-1]], height[i]) - height[top]

                volumes += distance * waters

            stack.append(i)
        return volumes