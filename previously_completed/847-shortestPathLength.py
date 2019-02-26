import collections


class Solution:

    def solve_shortest_point2point_path(self, graph, point2point_shortest_path, istart, iend):
        if istart == iend:
            return 0
        if len(graph[istart]) == 0:
            return 12
        if iend in graph[istart]:
            return 1

        shortest_path_len = 12
        for interal in graph[istart]:
            interal_shortest_path_len = 1 + self.solve_shortest_point2point_path(graph, point2point_shortest_path, interal, iend)
            if shortest_path_len > interal_shortest_path_len:
                shortest_path_len = interal_shortest_path_len
        return shortest_path_len


    def shortestPathLength1(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """

        # first get point to point, the shortest path length
        point2point_shortest_path = [[12 for x in range(0, len(graph))] for y in range(0, len(graph))]
        for istart in range(0, len(graph)):
            point2point_shortest_path[istart][istart] = 0
            for iend in graph[istart]:
                point2point_shortest_path[istart][iend] = 1

        for istart in range(0, len(graph)):
            for iend in range(0, len(graph)):
                point2point_shortest_path[istart][iend] = \
                    self.solve_shortest_point2point_path(graph, point2point_shortest_path, istart, iend)


        print(point2point_shortest_path)

    def shortestPathLength1(self, graph):
        N = len(graph)
        queue = collections.deque((1 << x, x) for x in xrange(N))
        dist = collections.defaultdict(lambda: N * N)
        for x in xrange(N): dist[1 << x, x] = 0

        while queue:
            cover, head = queue.popleft()
            d = dist[cover, head]
            if cover == 2 ** N - 1: return d
            for child in graph[head]:
                cover2 = cover | (1 << child)
                if d + 1 < dist[cover2, child]:
                    dist[cover2, child] = d + 1
                    queue.append((cover2, child))

    def shortestPathLength(self, graph):
        N = len(graph)
        dist = [[float('inf')] * N for i in xrange(1 << N)]
        for x in xrange(N):
            dist[1 << x][x] = 0

        for cover in xrange(1 << N):
            repeat = True
            while repeat:
                repeat = False
                for head, d in enumerate(dist[cover]):
                    for nei in graph[head]:
                        cover2 = cover | (1 << nei)
                        if d + 1 < dist[cover2][nei]:
                            dist[cover2][nei] = d + 1
                            if cover == cover2:
                                repeat = True

        return min(dist[2 ** N - 1])


if __name__ == '__main__':
    sol = Solution()
    sol.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]])