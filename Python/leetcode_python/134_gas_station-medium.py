class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not list:
            return -1
        
        if sum(gas) < sum(cost):
            return -1
        assert len(gas) == len(cost)
        for i in range(len(gas)):
            if self.isValidStart(gas, cost, i):
                return i
        return -1
        
    def isValidStart(self, gas, cost, start):
        # current gas
        cur = 0
        for i in range(len(gas)):
            idx = (i + start) % len(gas)
            # if cur < 0:
            #     return False
            cur += gas[idx]
            cur -= cost[idx]
            if cur < 0:
                return False
        return True
        
