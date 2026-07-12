class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # track the postion and speed
        car = [[p,s] for p,s in zip(position,speed)]
        stack = []
        # reverse sorted order
        for p,s  in sorted(car)[::-1]:
            # Append time to the stack for tracking
            stack.append((target - p)/s)
            # if the stack more than 1 element check if they collide
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)