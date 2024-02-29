from collections import defaultdict, deque


def ternary_search(elements, key):
    all_outcomes = {}
    l = 0
    r = len(elements) - 1
    mid1 = 0
    mid2 = 9999999
    n = 0
    while mid1 != mid2:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        n += 1
        if elements[mid1] == key:
            all_outcomes[n] = f"Index: {mid1}"
            i = mid1 - 1
            while i >= 0 and elements[i] == key:
                n += 1
                all_outcomes[n] = f"Index: {i}"
                i -= 1
            break
        if elements[mid2] == key:
            all_outcomes[n] = f"Index: {mid2}"
            i = mid2 + 1
            while i < len(elements) and elements[i] == key:
                n += 1
                all_outcomes[n] = f"Index: {i}"
                i += 1
            break
        if key < elements[mid1]:
            r = mid1 - 1
        elif key > elements[mid2]:
            l = mid1 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1
    if not all_outcomes:
        all_outcomes[n] = "Not Found"
    return all_outcomes


def binary_search(elements: list, target):
    low, high = 0, len(elements) - 1
    mid = int((low + high) / 2)

    while low <= high:
        if elements[mid] == target:
            return f"Element: {target} Index: {mid}"
        elif target > elements[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = int((low + high) / 2)


def front_back_search(elements: list, target):
    front = 0
    back = len(elements) - 1
    for _ in elements:
        if elements[front] == target:
            return f"Element: {target} Index: {front}"
        elif elements[back] == target:
            return f"Element: {target} Index: {back}"
        front += 1
        back -= 1


class BFS_Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Stores the graph for traversing

    def edge(self, u, v):
        self.graph[u].append(v)
        # print(self.graph)

    def bfs(self, start):
        path = ''
        visited = [False] * (max(self.graph) + 1)  # initialize all the nodes to be unvisited
        queue = []
        queue.append(start)
        visited[start] = True  # marking start position as visited
        while queue:
            start = queue.pop(0)
            path += f'{start} '
            for i in self.graph[start]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True
        return path

def bfs_search(elements: list, target:any):
    queue = deque(elements)
    visited = set()
    while queue:
        current = queue.popleft()
        if current == target:
            return elements.index(current)
        if current not in visited:
            visited.add(current)
            neighbors = [current - 1, current + 1]
            queue.extend(neighbor for neighbor in neighbors if 0 <= neighbor < len(elements))
    return -4004  # Not Found


class DFS_Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.path = ''

    def edge(self, u, v):
        self.graph[u].append(v)

    def recursion(self, start, visited):
        visited.add(start)
        self.path += f'{start} '
        for neighbour in self.graph[start]:
            if neighbour not in visited:
                self.recursion(neighbour, visited)

    def dfs(self, start) -> str:
        visited = set()
        self.recursion(start, visited)
        return self.path


def dfs_search(elements: list[str], target: str):
    stack = [elements]
    visited = set()
    while stack:
        current = stack.pop()
        if current == target:
            return elements.index(target)
        if not isinstance(current, list):
            if current not in visited:
                visited.add(current)
                neighbors = [current - 1, current + 1]
                stack.extend(neighbor for neighbor in neighbors if 0 <= neighbor < len(elements))
        else:
            if tuple(current) not in visited:
                visited.add(tuple(current))
                neighbors = []
                for i in range(len(current)):
                    new_neighbor = current[:i] + [x for x in current[i+1:] if x not in current[i]] + [current[i]]
                    neighbors.append(new_neighbor)
                stack.extend(neighbors)
    return -1  # Not Found



if __name__ == '__main__':
    ele = [1, 2, 3, 4, 5, 6, 7]
    tar = 7
    # g = BFS_Graph()
    # g.edge(0, 1)
    # g.edge(0, 2)
    # g.edge(1, 2)
    # g.edge(2, 0)
    # g.edge(2, 3)
    # g.edge(3, 3)
    # print(g.bfs(2))
    # g = DFS_Graph()
    # g.edge(0, 1)
    # g.edge(0, 2)
    # g.edge(1, 2)
    # g.edge(2, 0)
    # g.edge(2, 3)
    # g.edge(3, 3)
    # print(g.dfs(2))
    pass
