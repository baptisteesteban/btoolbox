from btoolbox.structures import BinaryHeap


def test_binary_heap_sorting_elements():
    REF = [8, 5, 3, 3, 7]
    q = BinaryHeap()
    q.push(5, 4)
    q.push(3, 9)
    q.push(7, 12)
    q.push(3, 5)
    q.push(8, 3)

    cnt = 0
    while not q.empty():
        v, _ = q.top()
        q.pop()
        assert v == REF[cnt]
        cnt += 1
    assert cnt == len(REF)


def test_binary_heap_sorting_update_elements():
    REF = [5, 3, 3, 7, 8]
    q = BinaryHeap()
    q.push(5, 4)
    q.push(3, 9)
    q.push(7, 12)
    q.push(3, 5)
    q.push(8, 3)
    q.update(1, 1)
    q.update(1, 14)

    cnt = 0
    while not q.empty():
        v, _ = q.top()
        q.pop()
        assert v == REF[cnt]
        cnt += 1
    assert cnt == len(REF)


def test_binary_heap_sorting_remove_elements():
    REF = [8, 3, 3, 7]
    q = BinaryHeap()
    q.push(5, 4)
    q.push(3, 9)
    q.push(7, 12)
    q.push(3, 5)
    q.push(8, 3)
    q.remove(1)

    cnt = 0
    while not q.empty():
        v, _ = q.top()
        q.pop()
        assert v == REF[cnt]
        cnt += 1
    assert cnt == len(REF)
