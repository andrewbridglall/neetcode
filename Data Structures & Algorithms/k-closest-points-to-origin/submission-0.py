class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calc distance
        data = []
        distances = []
        for point in points:
            d = (point[0]**2 + point[1]**2)**0.5
            data.append((d, point))
            distances.append(d)
        # build arr to store pair(distance, point)
        # sort distance
        res = []
        distances.sort()
        for i in range(k):
            d = distances[i]
            for ind, val in enumerate(data):
                dist, point = val
                if dist == d:
                    res.append(point)
                    break
            data.pop(ind)
        return res


        # pop k times. for each pop find point and append to res
        # return res