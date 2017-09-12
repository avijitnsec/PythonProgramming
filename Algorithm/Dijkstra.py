# Library for INT_MAX
import sys


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_arr(self, dist):
        for node in range(self.v):
            print(node, "t", dist[node])

    def min_distance(self, dist, setspt):
        min_num = sys.maxsize

        for i in range(self.v):
            if dist[i] < min_num and setspt[i] is False:
                min_num = dist[i]
                min_index = i
                return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.v
        dist[src] = 0
        setspt = [False] * self.v

        for count in range(self.v):
            u = self.min_distance(dist, setspt)
            setspt[u] = True

            for i in range(self.v):
                if self.graph[u][i] > 0 and setspt[i] is False and dist[i] > dist[u] + self.graph[u][i]:
                    dist[i] = dist[u] + self.graph[u][i]

        self.print_arr(dist)

if __name__ == '__main__':
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dijkstra(0)
