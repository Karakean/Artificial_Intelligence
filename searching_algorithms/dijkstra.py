import math
import queue
import sys
import maze


def path_from(node):
    path = [node]
    while node.parent is not None:
        node = node.parent
        path.append(node)
    return path


def L1(A, B):
    return abs(A.x - B.x) + abs(A.y - B.y)


def L2(A, B):
    return math.sqrt((A.x - B.x)**2 + (A.y - B.y)**2)


def dijkstra(maze):
    pq = queue.PriorityQueue(0)
    start_node = maze.find_node('S')
    start_node.cost = 0
    pq.put((0, start_node))
    while pq.not_empty:
        tuple = pq.get()
        node = tuple[1]
        if node.type == 'E':
            return path_from(node)
        children = maze.get_possible_movements(node)
        for child in children:
            new_cost = node.cost + maze.move_cost(node, child)
            if new_cost < child.cost:
                child.cost = new_cost
                child.parent = node
                pq.put((child.cost, child))
    return None


maze = maze.Maze.from_file(sys.argv[1])
maze.draw()
maze.path = dijkstra(maze)
print()
maze.draw()
print('path length: ', len(maze.path))
for node in maze.path:
    print(f'({node.x}, {node.y})', end=' ')
print()
