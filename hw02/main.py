from collections import deque

def bfs_path(graph: dict, start_node, target_node):
    """
    Finds the shortest path between a start node and a target node 
    in an unweighted graph using Breadth-First Search (BFS).

    :param graph: A dictionary representing the graph (adjacency list).
    :param start_node: The starting node.
    :param target_node: The target node.
    :return: A list representing the shortest path, or None if no path exists 
             or if one of the nodes is missing.
    """

    # 1. Handle missing nodes (per test_missing_node_returns_none)
    if start_node not in graph or target_node not in graph:
        return None

    # 2. Handle start equals target (per test_s_equals_t)
    if start_node == target_node:
        return [start_node]

    # Initialize BFS data structures
    # A queue for nodes to visit
    queue = deque([start_node])
    
    # A dictionary to store the 'parent' of each node in the shortest path
    # This is used to reconstruct the path later
    # Format: {child_node: parent_node}
    parent = {start_node: None}
    
    # Run BFS
    while queue:
        current_node = queue.popleft()

        # Check neighbors
        for neighbor in graph.get(current_node, []):
            # If the neighbor has not been visited yet (i.e., not in parent dict)
            if neighbor not in parent:
                parent[neighbor] = current_node
                
                # Check if we found the target
                if neighbor == target_node:
                    # Path found! Reconstruct it and return
                    return _reconstruct_path(parent, start_node, target_node)
                
                # Add the neighbor to the queue for further exploration
                queue.append(neighbor)

    # 3. Handle unreachable target (per test_unreachable_returns_none)
    # If the queue is empty and the target was not found, no path exists
    return None

def _reconstruct_path(parent_map, start_node, target_node):
    """
    Helper function to reconstruct the path from the parent map.
    """
    path = []
    current = target_node
    
    # Trace back from target to start using the parent map
    while current is not None:
        path.append(current)
        current = parent_map.get(current)
    
    # The path is constructed backwards, so reverse it
    path.reverse()
    
    # This check ensures we don't return an incomplete path 
    # (e.g., if target was unreachable, though the main function handles this)
    if path[0] == start_node:
        return path
    else:
        # Should not happen if called correctly from bfs_path
        return None

# The rest of the test code (g1, test functions, etc.) would go here for a complete run.