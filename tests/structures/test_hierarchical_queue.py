from btoolbox.structures import HQueue


def test_hierarchical_queue():
    q = HQueue(256)
    q.push(7, (0, 0))
    assert q._cur == 7
    q.push(4, (1, 0))
    assert q._cur == 4
    q.push(8, (2, 0))
    assert q._cur == 4
    v1, p1 = q.pop()
    assert v1 == 4 and p1[0] == 1 and p1[1] == 0 and q._cur == 7
    q.push(2, (0, 1))
    q.push(9, (1, 1))
    q.push(3, (2, 1))
    assert q._cur == 2 and q._size == 5
    v2, p2 = q.pop_nearest(4)
    assert v2 == 7 and p2[0] == 0 and p2[1] == 0

    ref = [(2, (0, 1)), (3, (2, 1)), (8, (2, 0)), (9, (1, 1))]
    i = 0
    while not q.empty():
        v, p = q.pop()
        ref_v, ref_p = ref[i]
        assert v == ref_v and p[0] == ref_p[0] and p[1] == ref_p[1]
        i += 1
    assert i == len(ref)
