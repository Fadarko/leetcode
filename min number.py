class Solution:
    def minPartitions(self, n: str) -> int:
        max = 0
        for st in n:
            if int(st) > max :
                max = int(st)
        return(max)
