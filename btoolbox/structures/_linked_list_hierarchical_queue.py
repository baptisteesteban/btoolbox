import numpy as np


class LinkedListHQueue:
    def __init__(self, nlevels: int, img_size: int):
        self._first = np.ones((nlevels,), dtype=np.int32) * -1
        self._last = np.ones((nlevels,), dtype=np.int32) * -1
        self._queue_size = np.zeros((nlevels), dtype=np.uint32)
        self._next = np.ones((img_size,), dtype=np.int32) * -1
        self._prev = np.ones((img_size,), dtype=np.int32) * -1
        self._cur = nlevels

    def size(self, q: int | None = None) -> int:
        """Return the size of a queue is `q` is not None, or the size of the whole hierarchical queue

        Parameters
        ----------
        q: int | None
            A queue index
        """
        if q is None:
            return np.sum(self._queue_size)
        assert q >= 0 and q < self._queue_size.size
        return self._queue_size[q]

    def empty(self, q: int | None = None) -> bool:
        """Return `True` if the queue `q` is empty (or the whole hierarchical queue if `q` is None), `False` otherwise.

        Parameters
        ----------
        q: int | None
            A queue index
        """
        return self.size(q) < 1

    def print(self):
        """Print the hierarchical queue"""
        print(f"Linked List based HQueue\nSize: {self.size()}")
        for q, e in enumerate(self._first):
            if e >= 0:
                print(f"[{q}]: ", end="")
                while self._next[e] >= 0:
                    print(f"{e}, ", end="")
                    e = self._next[e]
                print(f"{e}")

    def push(self, q: int, p: int):
        """Push a value `p` at the queue indexed by `q`.

        Parameters
        ----------
        q: int
            The queue index in which the new element is pushed
        p: int
            The element to pushed into the queue indexed by `q`
        """
        if self.empty(q):
            self._first[q] = self._last[q] = p
        else:
            self._prev[p] = self._last[q]
            self._next[self._last[q]] = p
            self._last[q] = p
        self._queue_size[q] += 1
        self._cur = min(self._cur, q)

    def top(self) -> int:
        """Return the element at the top of the hierarchical queue"""
        assert not self.empty()
        return self._first[self._cur]

    def pop(self):
        """Pop the first element of the hierarchical queue."""
        assert not self.empty()
        p = self._first[self._cur]
        self._queue_size[self._cur] -= 1
        if self._queue_size[self._cur] < 1:
            self._first[self._cur] = self._last[self._cur] = -1
            self._update_cur()
        else:
            self._first[self._cur] = self._next[p]
            self._prev[self._first[self._cur]] = -1
        self._prev[p] = self._next[p] = -1
        return p

    def update(self, p: int, old_q: int, new_q: int):
        """Change the queue of an element `p` from the queue `old_q` to the queue `new_q`."""
        assert not self.empty(old_q)
        # Complicated to verify in constant time
        assert self._belong_to_q(old_q, p)
        if old_q == new_q:
            return

        if self._last[old_q] == p:
            self._last[old_q] = self._prev[p]
        if self._first[old_q] == p:
            self._first[old_q] = self._next[p]
        if self._next[p] >= 0:
            self._prev[self._next[p]] = self._prev[p]
        if self._prev[p] >= 0:
            self._next[self._prev[p]] = self._next[p]
        self._prev[p] = self._next[p] = -1
        self._queue_size[old_q] -= 1
        self.push(new_q, p)

    def _update_cur(self):
        if self.size() < 1:
            self._cur = self._first.size
            return
        while self._cur < self._first.size and self._queue_size[self._cur] < 1:
            self._cur += 1
        assert self._cur < self._first.size

    # Is only used in assert
    def _belong_to_q(self, q: int, p: int):
        e = self._first[q]
        while e >= 0 and e != p:
            e = self._next[e]
        return e >= 0
