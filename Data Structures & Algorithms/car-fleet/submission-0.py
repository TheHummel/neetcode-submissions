class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        times = [(target - position[i]) / speed[i] for i in range(n)]

        position, times = zip(*sorted(zip(position, times), reverse=True))

        print(position, times)

        stack = []

        for time in times:
            if stack:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)

        print(stack)

        return len(stack)

