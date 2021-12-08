import random
from kind import Sea, City, Ice, Wind, EmptyLand, Forest

class Cell:
    def __init__(self, kind='City') -> None:
        # base values
        self.base_temptature = 0
        self.current_tempature = self.base_temptature
        self.wind = Wind()
        self.height = 0
        self.current_poluation = 0
        self.current_precipitation = 0
        self.kind = eval(f"{kind}()")

        # for update
        self.n_counters = 0
        self.poluation = 0
        self.precipitation = 0

    def compute_cell(self):
        # wind carries data from other cells
        if self.n_counters > 0:
            self.current_precipitation = self.precipitation / \
                self.n_counters + self.kind.precipitation
            self.current_poluation = min(self.poluation / self.n_counters + self.kind.poluation, 1)

        # cell didnt get new infomation,
        else:
            self.current_precipitation = self.kind.precipitation
            # avoding negative polution
            self.current_poluation = max(self.kind.poluation, 0)

        # rainning
        self.current_precipitation = self.current_precipitation if self.current_precipitation < 1 else 0

        # changing tempature by polution, changing base tempature by change over time
        self.current_tempature = self.base_temptature + \
            max((abs(self.base_temptature) / 10) * \
            ((self.current_poluation * 10) // 5) , 2)
        self.base_temptature += (self.tempature - self.base_temptature) / 10

        # resting update parameters
        self.reset_update_parameters()

    def reset_update_parameters(self):
        self.n_counters = 0
        self.poluation = 0
        self.precipitation = 0

        self.wind.update_wind()

    def update_from_cell(self, other):
        self._update_cell(other.current_poluation, other.current_precipitation)

    def _update_cell(self, pol, pre):
        self.poluation += pol
        self.precipitation += pre
        self.n_counters += 1

    def get_next_location(self, i, j, s):
        return self.wind.new_location(i, j, s)


