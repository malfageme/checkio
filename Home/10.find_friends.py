def check_connection(network, first, second):
    connections = {}
    for link in network:
        parent,child = link.split("-")
        if parent not in connections:
            connections[parent] = [child]
        else:
            connections[parent].append(child)
        parent,child = child,parent
        if parent not in connections:
            connections[parent] = [child]
        else:
            connections[parent].append(child)
    
    visited = []
    future = [first]
    actual = first
    while future:
        if actual == second:
            return True
        if actual not in visited:
            if actual in connections:
                future.extend(connections[actual])
            visited.append(actual)
        actual = future.pop()
    return False

        
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."

