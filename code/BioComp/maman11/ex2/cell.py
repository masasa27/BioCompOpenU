import random
from kind import Sea, City, Ice, Wind, EmptyLand, Forest

class Cell:
    def __init__(self, kind='City') -> None:
        # base values
        self.base_temptature = 0
        self.wind = Wind()
        self.height = 0
        self.base_poluation = 0
        self.base_precipitation = 0
        self.kind = eval(f"{kind}()")

        # for update
        self.n_counters = 0
        self.poluation = 0
        self.precipitation = 0

    def compute_cell(self):
        # wind carries data from other cells
        if self.n_counters > 0:
            self.base_precipitation = self.precipitation / \
                self.n_counters + self.kind.precipitation
            self.base_poluation = min(self.poluation / self.n_counters + self.kind.poluation, 1)

        # cell didnt get new infomation,
        else:
            self.base_precipitation = self.kind.precipitation
            # avoding negative polution
            self.base_poluation = max(self.kind.poluation, 0)

        # rainning
        self.base_precipitation = self.base_precipitation if self.base_precipitation < 1 else 0

        # changing tempature by polution, changing base tempature by change over time
        self.tempature = self.base_temptature + \
            (abs(self.base_temptature) / 10) * \
            ((self.base_poluation * 10) // 5)
        self.base_temptature += (self.tempature - self.base_temptature) / 10

        # resting update parameters
        self.reset_update_parameters()

    def reset_update_parameters(self):
        self.n_counters = 0
        self.poluation = 0
        self.precipitation = 0

        self.wind.update_wind()

    def update_from_cell(self, other):
        self._update_cell(other.base_poluation, other.base_precipitation)

    def _update_cell(self, pol, pre):
        self.poluation += pol
        self.precipitation += pre
        self.n_counters += 1

    def get_next_location(self, i, j, s):
        return self.wind.new_location(i, j, s)


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


