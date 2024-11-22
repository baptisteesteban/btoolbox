from typing import Any


class BinaryHeap:
    """Class modeling a priority queue as a binary heap."""

    def __init__(self):
        """Initialize the binary heap."""
        self._tree = []
        self._priorities = []
        self._values = []
        self._size = 0

    def push(self, v: Any, p: float):
        """Add a new element in the binary heap.

        Parameters
        ----------
        v : Any
            The value to add in the binary heap.
        p : float
            The priority of this value in the priority queue.
        """
        # Put the value and the priority in the data tables
        ind = self._check_empty_position()
        if ind < 0:
            ind = len(self._values)
            self._values.append(v)
            self._priorities.append(p)
        else:
            self._values[ind] = v
            self._priorities[ind] = p

        self._tree.append(ind)
        self._update_up(self._size)
        self._size += 1

    def pop(self):
        """Remove the value at the top of the binary heap."""
        assert not self.empty()
        self._values[self._tree[0]] = None
        self._priorities[self._tree[0]] = None
        self._tree[0] = self._tree[-1]
        self._tree.pop()
        self._update_down(0)
        self._size -= 1

    def top(self) -> tuple[Any, float]:
        """Return the value at the top of the binary heap as well as its priority.

        Returns
        -------
        value: Any
            The value contained at the top of the binary heap
        priority: int
            The priority of the value at the top of the binary heap
        """
        assert not self.empty()
        i = self._tree[0]
        return self._values[i], self._priorities[i]

    def empty(self) -> bool:
        """Check if the binary heap is empty.

        Returns
        -------
        empty: bool
            True if the binary heap is empty, False otherwise
        """
        return self._size == 0

    def update(self, n: int, new_p: float):
        """Update the priority of the value of the node `n`.

        Parameters
        ----------
        i: int
            The position to update.
        new_p: float
            The updated priority.
        """
        pass

    def remove(self, n: int):
        """Remove a node at position `n` in the tree.

        Parameters
        ----------
        n : int
            The node to remove in the tree.
        """
        pass

    @property
    def size(self) -> int:
        """Return the number of element in the binary heap.

        Returns
        -------
        int
            The number of element in the binary heap.
        """
        return self._size

    def _update_down(self, n: int):
        N = len(self._tree)
        has_swapped = True
        while n < N and has_swapped:
            has_swapped = False
            candidate_swap = None
            c1 = 2 * n + 1
            if c1 < N and self._priorities[self._tree[c1]] < self._priorities[self._tree[n]]:
                candidate_swap = c1
            c2 = 2 * n + 2
            if (
                c2 < N
                and self._priorities[self._tree[c2]] < self._priorities[self._tree[n]]
                and self._priorities[self._tree[c2]] < self._priorities[self._tree[c1]]
            ):
                candidate_swap = c2
            if candidate_swap is not None:
                self._tree[n], self._tree[candidate_swap] = self._tree[candidate_swap], self._tree[n]
                n = candidate_swap
                has_swapped = True

    def _update_up(self, n: int):
        p = (n - 1) // 2
        while n > 0 and self._priorities[self._tree[n]] < self._priorities[self._tree[p]]:
            self._tree[n], self._tree[p] = self._tree[p], self._tree[n]
            n = p
            p = (n - 1) // 2

    def _check_empty_position(self) -> int:
        empty_index = -1
        for i in range(len(self._values)):
            if self._values[i] is None:
                empty_index = i
                break
        return empty_index
