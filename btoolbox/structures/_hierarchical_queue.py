from typing import Any


class HQueue:
    """Class modeling a priority queue as a hierarchical queue."""

    def __init__(self, n: int, nearest_strategy: str = "lower_first"):
        """Initialize the hierarchical queue.

        Parameters
        ----------
        n: int
            The number of queue to initialize in the hierarchical queue
        nearest_strategy: str
            The strategy to use to find the nearest non-empty queue for a given value `v`. Such strategy is used in the
            `pop_nearest` method.
            The parameters may take one of the following values:
            * `lower_first`: First look for a non-empty queue with an index value `k ≥ v`, and if not found,
            look for the non-empty queue with an index value `k < v`.
            * `distance`: look for the non-empty queue with the distance at both side of the specified queue.

        Raises
        ------
        ValueError
            If the `nearest_strategy` parameter value is invalid.
        """
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
        """Check if the hierarchical queue has no elements pushed.

        Returns
        -------
        bool
            `True` if the hierarchical queue is empty, `False` otherwise.
        """
        return self._size == 0

    def push(self, p: int, v: Any):
        """Push an element in the hierarchical queue.

        Parameters
        ----------
        p: int
            The priority of the value to push.
        v: Any
            The value to push.
        """
        assert p < self._n
        self._data[p].append(v)
        self._cur = min(self._cur, p)
        self._size += 1

    def pop(self) -> tuple[int, Any]:
        """Pop the first element of the hierarchical queue.

        Returns
        -------
        p: int
            The priority of the first element in the hierarchical queue.
        v: Any
            The value of the first element in the hierarchical queue.
        """
        assert not self.empty()
        p = self._data[self._cur].pop(0)
        v = self._cur
        self._size -= 1
        self._update_current()
        return v, p

    def pop_nearest(self, p: int) -> tuple[int, Any]:
        """Pop the nearest element of `p` in the hierarchical queue according to the `nearest_strategy`.

        Parameters
        ----------
        p: int
            The priority desired.

        Returns
        -------
        p_res: int
            The nearest priority from `p` according to the `nearest_strategy`.
        v_res: Any
            The value at priority `p_res`.
        """
        assert not self.empty()
        res_p = self._find_nearest_func(p)
        res_v = self._data[res_p].pop(0)
        self._size -= 1
        self._update_current()
        return res_p, res_v

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
