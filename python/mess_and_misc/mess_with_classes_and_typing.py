class Node:
    def __init__(self):
        pass


class FooNode(Node):
    def __init__(self, arg1: list[Node]):
        super().__init__()
        ...


class BarNode(Node):
    def __init__(self, arg1: Node):
        super().__init__()
        ...
