# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    tree = {}
    for node, parent in enumerate(parents):
        if parent == -1:
            continue
        if parent not in tree:
            tree[parent] = [node]
        else:
            tree[parent].append(node)
    def height(node):
        if node not in tree:
            return 1
        return max([height(child) for child in tree[node]]) + 1
    root = parents.index(-1)
    return height(root)
def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
