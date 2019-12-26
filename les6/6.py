class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        return self.length * self._width


class MassCount(Road):
    def __init__(self, length, width, volume):
        super().__init__(length, width)
        self.volume = volume


r = MassCount(20, 5000, 125)
print(r.mass())