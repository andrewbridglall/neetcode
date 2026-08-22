class CountSquares:

    def __init__(self):
        # init hashset
        self.points = {}
        # init mapx mapy
        self.mapX = defaultdict(list)
        self.mapY = defaultdict(list)

    def add(self, point: List[int]) -> None:
        # add point to all three ds
        x, y = point
        if (x,y) not in self.points:
            self.points[(x,y)] = 0
        self.points[(x,y)] +=1
        self.mapX[x].append(y) # along same vertical
        self.mapY[y].append(x) # along same horizontal

    def count(self, point: List[int]) -> int:
        # given point x,y
        x,y = point
        countSquares = 0
        # find all verticals, ie x constant
        for b in self.mapX[x]:
            if b == y:
                continue
            # find all horizontals, ie y constant
            for a in self.mapY[y]:
                if a == x:
                    continue
                # if vertical distance = horizontal distance
                # check if new point exists in set of all points
                # if so incr count 1
                if abs(y-b) == abs(x-a) and (a,b) in self.points:
                    countSquares += self.points[(a,b)]
        # ret count
        return countSquares
