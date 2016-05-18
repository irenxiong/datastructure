#!/usr/bin/env python
# coding=utf-8
import sys
#最大递归深度
sys.setrecursionlimit(5000)

#从有向图graph中获取一条从begin到end的路径, 无路径返回None
def get_one_path(graph, begin, end, one_path=[]):
    one_path = one_path + [begin]
    if begin == end:
        return one_path
    if not graph.has_key(begin):
        return None
    for value in graph[begin]:
        if value not in one_path:
            path = get_one_path(graph, value, end, one_path)
            if path:
                return path
    return None
#从有向图graph中获取所有从begin到end的路径, 无路径返回[]
def get_all_path(graph, begin, end, one_path=[]):
    one_path = one_path + [begin]
    if begin == end:
        return [one_path]
    if not graph.has_key(begin):
        return []
    paths = []
    for value in graph[begin]:
        if value not in one_path:
            cur_paths = get_all_path(graph, value, end, one_path)
            for path in cur_paths:
                paths.append(path)
    return paths
#从有向图graph中获取从begin到end的最短路径, 无路径返回None
def get_shortest_path(graph, begin, end, one_path=[]):
    one_path = one_path + [begin]
    if begin == end:
        return one_path
    if not graph.has_key(begin):
        return None
    result = None
    for value in graph[begin]:
        if value not in one_path:
            cur_path = get_shortest_path(graph, value, end, one_path)
            if cur_path:
                if not result or len(cur_path) < len(result):
                    result = cur_path
    return result
if __name__ == "__main__":
    test_graph = {'A': ['B', 'C'], 
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['B']
            }
    test_one_path = get_one_path(test_graph, 'A', 'D')
    print test_one_path
    test_all_path = get_all_path(test_graph, 'A', 'D')
    print test_all_path
    test_shortest_path = get_shortest_path(test_graph, 'A', 'D')
    print test_shortest_path

