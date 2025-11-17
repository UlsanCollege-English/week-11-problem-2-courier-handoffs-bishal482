import pytest
from hw02.main import bfs_path

def g1():
    return {
        'A': ['B','D'],
        'B': ['A','C'],
        'C': ['B','E'],
        'D': ['A','E'],
        'E': ['D','C','F'],
        'F': []
    }

def test_basic_shortest_path():
    g = g1()
    path = bfs_path(g, 'A', 'E')
    assert path in [['A','D','E'], ['A','B','C','E']] and len(path) == 3

def test_s_equals_t():
    g = g1()
    assert bfs_path(g, 'C', 'C') == ['C']

def test_missing_node_returns_none():
    g = g1()
    assert bfs_path(g, 'A', 'Z') is None
    assert bfs_path(g, 'Z', 'A') is None

def test_unreachable_returns_none():
    g = g1()
    assert bfs_path(g, 'F', 'A') is None

@pytest.mark.parametrize("s,t,expected_len", [
    ('A','C', 3),
    ('A','B', 2),
    ('B','E', 3),
])
def test_lengths_param(s, t, expected_len): # <-- Removed 'general' and all default values
    g = g1()
    p = bfs_path(g, s, t)
    assert p is not None and len(p) == expected_len

def test_alternative_shortest_paths_allowed():
    g = {
        'S': ['X','Y'],
        'X': ['S','T'],
        'Y': ['S','T'],
        'T': ['X','Y']
    }
    p = bfs_path(g, 'S', 'T')
    assert p in [['S','X','T'], ['S','Y','T']]

def test_branching_graph():
    g = {
        'A':['B','C','D'],
        'B':['A','E'],
        'C':['A','E'],
        'D':['A'],
        'E':['B','C']
    }
    p = bfs_path(g, 'D','E')
    assert p in [['D','A','B','E'], ['D','A','C','E']]
