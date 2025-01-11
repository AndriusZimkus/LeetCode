class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        i = 2
        length = len(cost)
        ##Cumulative logic
        while i < length:
            cost[i] = cost[i]+min(cost[i-2],cost[i-1])
            i+=1
        return(min(cost[length-1],cost[length-2]))

cost = [10,15,20]
sol = Solution()
print(sol.minCostClimbingStairs(cost))

##cost = [10,15,20]
##
##print(minCostClimbingStairs(cost))
##
##cost = [1,100,1,1,1,100,1,1,100,1]
##
##print(minCostClimbingStairs(cost))
##
##cost = [0,0,0,1]
##
##print(minCostClimbingStairs(cost))
##
##cost = [0,1,1,1]
##print(minCostClimbingStairs(cost))
##
##cost = [0,1,2,2]
##print(minCostClimbingStairs(cost))
##
##cost = [1,2,2,2]
##print(minCostClimbingStairs(cost))
##
##cost = [1,0,2,2]
##print(minCostClimbingStairs(cost))
