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
        pass

    def pop(self):
        """Remove the value at the top of the binary heap."""
        pass

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

    def _update_down(self, n: int):
        pass

    def _update_up(self, n: int):
        pass
