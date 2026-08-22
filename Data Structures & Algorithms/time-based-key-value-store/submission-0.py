class TimeMap:

    def __init__(self):
        # init hashmap
        self.tmap = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        # create hashed key
        # key#timestamp -> value
        hkey = key + "#" + str(timestamp)
        self.tmap[hkey] = value

    def get(self, key: str, timestamp: int) -> str:
        # given n = timestamp
        # iter from n .... 1 and check if key exists in hashmap
        for n in range(timestamp, 0, -1):
        # if found return else return empty str
            hkey = key + "#" + str(n)
            if hkey in self.tmap:
                return self.tmap[hkey]
        return ""
