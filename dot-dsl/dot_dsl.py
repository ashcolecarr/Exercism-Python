NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    nodes = []
    edges = []
    attrs = {}

    def __init__(self, data=[]):
        self.nodes.clear()
        self.edges.clear()
        self.attrs.clear()
        # Leave the default values.
        if not data:
            return

        if not isinstance(data, list):
            raise TypeError('Input data is malformed.')

        for x in data:
            self.__validate_item__(x)

            if x[0] == NODE:
                self.nodes.append(Node(x[1], x[2]))
            elif x[0] == EDGE:
                self.edges.append(Edge(x[1], x[2], x[3]))
            elif x[0] == ATTR:
                self.attrs.update({x[1]: x[2]})
            else:
                raise ValueError('Graph item is unknown.')

    def __validate_item__(self, item):
        if len(item) < 2:
            raise TypeError('Graph item is malformed.')
        elif item[0] == NODE and len(item) != 3:
            raise ValueError('Node is malformed.')
        elif item[0] == EDGE and len(item) != 4:
            raise ValueError('Edge is malformed.')
        elif item[0] == ATTR and len(item) != 3:
            raise ValueError('Attr is malformed.')
