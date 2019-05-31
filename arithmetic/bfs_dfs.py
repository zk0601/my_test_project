graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}

"""
广度优先，使用队列（先进先出），最短路径
args：地图， 起始点
out：搜索顺序
"""
def bfs(graph, s):
    queue = []
    queue.append(s)
    has_set = set(s)
    result = []
    while queue:
        p = queue.pop(0)
        result.append(p)
        for node in graph[p]:
            if not node in has_set:
                has_set.add(node)
                queue.append(node)
    return result

"""
深度优先，使用栈（后进先出），最短路径
args：地图， 起始点， 终点
out： 终点到起始点的走法
"""
def dfs(graph, s, ss):
    stack = []
    stack.append(s)
    has_set = set(s)
    result = []
    parents = {}
    while stack:
        p = stack.pop()
        for node in graph[p]:
            if not node in has_set:
                has_set.add(node)
                stack.append(node)
                parents[node] = p
    print(parents)
    while True:
        if s == ss:
            result.append(ss)
            return result
        result.append(ss)
        ss = parents[ss]


graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

"""
最短路径算法，使用带权队列，priority，基于bfs
args：地图， 起始点， 终点
out： 终点到起始点的走法
"""
def Dijkstra(graph, s, ss):
    pri_queue = []
    pri_queue.append((s, 0))
    has_set = set(s)
    parent_distance = {s: [None, 0]}
    result = []
    while pri_queue:
        p = pri_queue.pop(0)
        key = p[0]
        distance = p[1]
        if key not in has_set:
            has_set.add(key)
        for next, pri in graph[key].items():
            if next not in has_set:
                pri_queue.append((next, pri))
                pri_queue.sort(key=lambda x: x[1])
                if next not in parent_distance:
                    parent_distance[next] = [key, graph[key][next] + parent_distance[key][1]]
                elif parent_distance[key][1] + graph[key][next] < parent_distance[next][1]:
                    parent_distance[next][1] = parent_distance[key][1] + graph[key][next]
                    parent_distance[next][0] = key
    print(parent_distance)
    temp = ss
    while True:
        if s == ss:
            result.append(s)
            result.append(parent_distance[temp][1])
            return result
        result.append(ss)
        ss = parent_distance[ss][0]

print(Dijkstra(graph, 'A', 'F'))