import copy

def get_most_connected_node(nodes):
    #max_list = [x for x in nodes if len(x) == max(map(len,nodes))]
    #max_list = [x for x in nodes if len(x) > 0]
    max_list = [x for x in nodes if len(x) > 1]
    if len(max_list) == 0:
        max_list =     max_list = [x for x in nodes if len(x) > 0]
    return [nodes.index(x) for x in max_list]

def remove_node(nodes, node_index):
    nodes[node_index] = []
    for node in nodes:
        if node_index in node:
            node.remove(node_index)
    return nodes

def get_loose_nodes(nodes, removed):
    return sum([1 for index in range(len(nodes)) if len(nodes[index]) == 0 and index not in removed])

def break_rings_links(nodes, removed):
    num_rings = len(nodes)
    new_nodes = copy.deepcopy(nodes)
    # Break rings until there are no linked ones
    while any(map(len,new_nodes)):
        # First search for the rings with one link only
        one_link_list = [new_nodes.index(x) for x in new_nodes if len(x) == 1]
        while len(one_link_list) != 0:
            remove_node(new_nodes,new_nodes[one_link_list[0]][0])
            removed += [one_link_list[0]]
            one_link_list = [new_nodes.index(x) for x in new_nodes if len(x) == 1]

	if not any(map(len,new_nodes)):
            return len(removed)
  
        most_connected = get_most_connected_node(new_nodes)
        if len(most_connected) > 1:
            less_broken = 99999
            less_ring = 99999
            for ring_try in most_connected:
                try_nodes = copy.deepcopy(new_nodes)
                remove_node(try_nodes, ring_try)
                try_removed = removed + [ring_try]
                try_result =  break_rings_links(try_nodes, try_removed)
                if try_result < less_broken:
                    less_broken = try_result
                    less_ring = ring_try
            remove_node(new_nodes, less_ring)
            removed.append(less_ring)
        else:
            remove_node(new_nodes, most_connected[0])
            removed.append(most_connected[0])

    return len(removed)

def break_rings(rings):
    num_rings = max(reduce(set.union, rings))
    nodes = [[] for x in range(num_rings)]
    for (p,c) in rings:
        nodes[p-1].append(c-1)
        nodes[c-1].append(p-1)
    removed = []
    return break_rings_links(nodes, removed)
    

assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"

assert break_rings(({3,4},{5,6},{2,7},{1,5},{2,6},{8,4},{1,7},{4,5},{9,5},{2,3},{8,2},{2,4},{9,6},{5,7},{3,6},{1,3},)) == 5, "5th example"
assert break_rings(({1,2},{2,3},{3,4},{4,5},{5,2},{1,6},{6,7},{7,8},{8,9},{9,6},{1,10},{10,11},{11,12},{12,13},{13,10},{1,14},{14,15},{15,16},{16,17},{17,14},)) == 8, "6th example"

assert break_rings(({4,6},{4,12},{2,4},{12,5},{12,14},{12,7},{9,13},{1,10},{9,18},{17,19},{4,13},{2,20},{10,14},{11,12},{11,15},{16,2},{8,5},{3,12},{17,11},{10,19},)) == 8, "8th example"

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"

