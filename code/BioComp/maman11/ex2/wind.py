class Wind:

    def __init__(self) -> None:
        self.v = 0
        self.dir_x = 0
        self.dir_y = 0
        self.random_counter = 0

        self.randomize_values()

    def new_location(self, i, j, size):
        rel = (i + self.dir_x * self.v) % (size - 1), (j + (self.dir_y * self.v)) % (size - 1)

        return rel

    def update_wind(self):
        if self.random_counter % 4 == 0:
            self.randomize_values()

        else:
            self.random_counter += 1

        if self.random_counter == 100:
            self.random_counter = 0
    
    def _update_wind(self, v, d):
        if d == 'N':
            self.dir_y = -1
            self.dir_x = 0

        elif d == 'W':
            self.dir_x = -1
            self.dir_y = 0

        elif d == 'E':
            self.dir_x = 1
            self.dir_y = 0
        else:
            self.dir_x = 0
            self.dir_y = 1

        self.v = v
    
    def randomize_values(self):
        self._update_wind(random.randint(
            2, 4), random.choice(['N', 'E', 'W', 'S']))

    def __repr__(self) -> str:
        return f"Wind({self.v},{self.dir_x}, {self.dir_y})"


