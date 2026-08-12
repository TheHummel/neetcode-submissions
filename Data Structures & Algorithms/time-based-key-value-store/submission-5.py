class TimeMap:

    def __init__(self):
        self.tm = {}     # key -> list of tuples (ts, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tm:
            self.tm[key].append((timestamp, value))
        else:
            self.tm[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ""

        values = self.tm[key]
        l, r = 0, len(values)
        while l<r:
            m = (r+l)//2
            if timestamp >= values[m][0]:
                l = m+1
            else:
                r = m

        return values[l - 1][1] if l > 0 else ""
        
