class Kind:
    def __init__(self) -> None:
        self.poluation = 0
        self.precipitation = 0

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.poluation}, {self.precipitation})"


class Ice(Kind):
    def __init__(self) -> None:
        super().__init__()
        self.precipitation = 0.1
        self.t = -10


class Sea(Kind):
    def __init__(self) -> None:
        super().__init__()
        self.precipitation = 0.1
        self.poluation = -0.001
        self.t = 15


class Forest(Kind):
    def __init__(self) -> None:
        super().__init__()
        self.precipitation = 0.1
        self.poluation = -0.0001
        self.t = 20


class EmptyLand(Kind):
    def __init__(self) -> None:
        super().__init__()
        self.precipitation = 0.1
        self.t = 20


class City(Kind):
    def __init__(self) -> None:
        super().__init__()
        self.precipitation = 0.05
        self.poluation = 0.05
        self.t = 25


