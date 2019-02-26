# Solution 1, not optimal
# class Solution(object):
#     def kClosest(self, points, K):
#         """
#         :type points: List[List[int]]
#         :type K: int
#         :rtype: List[List[int]]
#         """
#         if points is None or len(points) == 0:
#             return []
#         if len(points) < K:
#             K = len(points)
#         return sorted(points, key = lambda x: x[0]**2 + x[1]**2)[:K]

# Solution 2:
# e.g.K maximum elements, minHeap protocal: push: heapq.heappush(res, [key, element]), get: heapq.heappop(res) or peek: res[0][0] or res[0][1]

# maxHeap protocal: e.g. K minimum, push： heapq.heappush(res, [-1*key, element]), get: -1*res[0][0]
# import heapq
# class Solution(object):
#     def kClosest(self, points, K):
#         res = []
#         for p in points:
#             if len(res) < K:
#                 heapq.heappush(res, [-1*self.distance(p), p])
#                 continue
#                 # heapq.heappop(res)
#                 # heapq.heappush(res, [-1*self.distance(p), p])
#             heapq.heappushpop(res, [-1*self.distance(p), p])
#         ret = []
#         while res:
#             ret.append(heapq.heappop(res)[1])
#         return ret
        
#     # we can also write: distance = lambda x: x[0]**2 + x[1]**2
#     # or even distance = lambda n : points[n][0]**2 + points[n][1]**2
#     def distance(self, point):
#         return point[0]**2 + point[1]**2
        
# cleaner version:
import heapq
class Solution(object):
    def kClosest(self, points, K):
        if points is None or len(points) == 0:
            return []
        if len(points) < K:
            K = len(points)
        res = []
        
        dist = lambda p: p[0]**2 + p[1]**2
        for point in points:
            heapq.heappush(res, (-dist(point), point))
            if len(res) > K:
                heapq.heappop(res)
        return [heapq.heappop(res)[1] for _ in range(K)]
        
        
        
        
        
        
        
        
        
        
