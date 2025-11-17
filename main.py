from collections import deque

def bfs_path(graph, s, t):
    # missing nodes
    if s not in graph or t not in graph:
        return None

    # same start/end
    if s == t:
        return [s]

    visited = set([s])
    parent = {s: None}
    q = deque([s])

    while q:
        u = q.popleft()

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                q.append(v)

                if v == t:
                    # reconstruct path
                    path = []
                    cur = t
                    while cur is not None:
                        path.append(cur)
                        cur = parent[cur]
                    return path[::-1]

    return None
