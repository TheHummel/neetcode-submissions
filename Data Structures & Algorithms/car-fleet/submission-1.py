class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        times = [(target - position[i]) / speed[i] for i in range(n)]

        position, times = zip(*sorted(zip(position, times), reverse=True))

        stack = []

        for time in times:
            if stack and time > stack[-1] or not stack:
                    stack.append(time)

        return len(stack)

