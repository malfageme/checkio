class Friends:
    def __init__(self, connections):
        self.connections = set([])
        for connection in connections:
            self.connections.add(frozenset(connection))

    def add(self, connection):
        len_before=len(self.connections)
        self.connections.add(frozenset(connection))
        return True if len(self.connections)>len_before else False

    def remove(self, connection):
        try:
            self.connections.remove(frozenset(connection))
            return True
        except KeyError:
            return False

    def names(self):
        return set([el for connection in self.connections for el in connection])

    def connected(self, name):
        connections = [connection for connection in self.connections if name in connection]
        return set([el for connection in connections for el in connection if el != name])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"

