from collections import defaultdict, deque
import math
import warnings


def SimpleLinearSearch(iterable: list[str | int] | tuple[str | int], target: str | int) -> int | None:
    len_iterable = len(iterable)
    for i in range(len_iterable):
        if target == iterable[i]:
            return i
    return None

def SentinelLinearSearch(iterable: list[str | int], target: str | int):
    len_iterable = len(iterable)
    iterable.append(target) # adding the sentinel value

    for i in range(len_iterable): # then looping through the new list
        if target == iterable[i]: # if target is found, then
            if i == len_iterable: # check if the target value is the sentinel value
                return None # if so return None
            return i # else we return the index value
    return None # if the loop ends, tha target is not found and return None


def SelfOrganizingSearch(iterable: list[str | int], target: str | int, method: str="mtf") -> tuple[int, list] | tuple[None, list]:
    iterable = iterable.copy()
    method = method.lower()

    if not isinstance(method, str) or method not in ('mtf', 'transpose'):
        warnings.warn(f"Invalid method '{method}'. Choose either 'mtf' or 'transpose'.")
        return None, iterable

    if not isinstance(iterable, list):
        warnings.warn(f"Iterable requires a list but provided {type(list).__name__}")
        return None, iterable

    if len(iterable) == 0:        # If no elements in list, no need of searching
        return None, iterable

    target_index = None   # To store the target index if found

    for i in range(len(iterable)):  # We are searching through the entire list for the target using linear search
        if target == iterable[i]:  # if target is found, we update the target_index and
            target_index = i       # break out of the loop
            break

    if target_index == 0:          # If the target value is at the first index, list modification is not required
        return target_index, iterable

    if target_index is None:       # If we didn't find the target value we return none along with the unmodified list
        return None, iterable

    # Move To Front
    if method == 'mtf':            # If MTF(Move-To-Front) is selected, then we swap the first element of the
        temp = iterable[0]         # list with the target value and return the modified list along with that target_index
        iterable[0] = iterable[target_index]
        iterable[target_index] = temp
        return target_index, iterable

    # Transpose
    temp = iterable[target_index - 1] # For transpose, we swap the target value with its preceding value
    iterable[target_index - 1] = iterable[target_index]   # and return the modified list along with that target_index
    iterable[target_index] = temp
    return target_index, iterable

def Jump_Search(iterable: list[int | str], target: int | str):
    # Check if the iterable is a list and contains sorted integers
    if not isinstance(iterable, list):
        warnings.warn(f"Iterable should be a list but provided {type(iterable).__name__}")
        return None

    # calculating the chunk size which us square root of the list length
    chunk_size = int(math.sqrt(len(iterable)))

    n = len(iterable)
    prev = 0
    current = chunk_size

    # jump through the chunks
    while current < n and iterable[current] < target:
        prev = current
        current += chunk_size

    # then performing a linear search in the identified chunk
    for i in range(prev, min(current, n)):
        if iterable[i] == target:
            return i  # returning the index if the target is found
    # if target is not found
    return None

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
