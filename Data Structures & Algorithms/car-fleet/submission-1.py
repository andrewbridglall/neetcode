class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # add pos and speed of cars to single arr
        n = len(position)
        cars = []
        for i in range(n):
            cars.append([position[i], speed[i]])
        # sort in descending order - limiting factor is speed of car in first position
        cars.sort(reverse=True)
        # for each car, calc time to reach tar
        stack = []
        for car in cars:
            pi, v = car
            t = (target - pi)/v
        # if time of car i <= time stack top - part of same fleet continue
        # else time of car i > time stack top - slower, and thus part of new fleet - add to stack
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)

        # return len of stack