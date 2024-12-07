class HQueue:
    def __init__(self, n: int, nearest_strategy: str = "lower_first"):
        self._data: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        self._n = n
        self._cur: int = n
        self._size: int = 0
        self._find_nearest_func = lambda v: 0  # Only for Mypy
        if nearest_strategy == "lower_first":
            self._find_nearest_func = self._find_nearest_lower_first
        elif nearest_strategy == "distance":
            self._find_nearest_func = self._find_nearest
        else:
            raise ValueError("Invalid find nearest strategy")

    def empty(self) -> bool:
        return self._size == 0

    def push(self, v: int, p: tuple[int, int]):
        assert v < self._n
        self._data[v].append(p)
        self._cur = min(self._cur, v)
        self._size += 1

    def pop(self) -> tuple[int, tuple[int, int]]:
        assert not self.empty()
        p = self._data[self._cur].pop(0)
        v = self._cur
        self._size -= 1
        self._update_current()
        return v, p

    def pop_nearest(self, v: int) -> tuple[int, tuple[int, int]]:
        assert not self.empty()
        res_v = self._find_nearest_func(v)
        res_p = self._data[res_v].pop(0)
        self._size -= 1
        self._update_current()
        return res_v, res_p

    def _find_nearest(self, v: int) -> int:
        assert not self.empty()
        if len(self._data[v]) > 0:
            return v
        d = 1
        res = 0
        while v + d < self._n or v - d >= 0:
            if v - d >= 0 and len(self._data[v - d]) > 0:
                res = v - d
                break
            if v + d < self._n and len(self._data[v + d]) > 0:
                res = v + d
                break
            d += 1
        return res

    def _find_nearest_lower_first(self, v: int) -> int:
        lvl = v
        while lvl < self._n and len(self._data[lvl]) == 0:
            lvl += 1
        if lvl < self._n:
            return lvl
        lvl = v
        while lvl >= 0 and len(self._data[lvl]) == 0:
            lvl -= 1
        assert lvl >= 0
        return lvl

    def _update_current(self):
        if self._size == 0:
            self._cur = self._n
            return

        while self._cur < self._n and len(self._data[self._cur]) == 0:
            self._cur += 1
