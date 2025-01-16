from btoolbox.structures import HQueue


def test_hierarchical_queue_default():
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
    v3, p3 = q.top()
    assert v3 == 2 and p3[0] == 0 and p3[1] == 1

    ref = [(2, (0, 1)), (3, (2, 1)), (8, (2, 0)), (9, (1, 1))]
    i = 0
    while not q.empty():
        v, p = q.pop()
        ref_v, ref_p = ref[i]
        assert v == ref_v and p[0] == ref_p[0] and p[1] == ref_p[1]
        i += 1
    assert i == len(ref)


def test_hierarchical_queue_greater_comp():
    q = HQueue(10, cmp="greater")
    q.push(7, 0)
    q.push(3, 1)
    q.push(5, 2)
    q.push(6, 3)
    p, v = q.top()
    assert p == 7 and v == 0
    q.pop()

    REF_P = [6, 5, 3]
    REF_V = [3, 2, 1]
    i = 0
    while not q.empty():
        p, v = q.pop()
        assert p == REF_P[i] and v == REF_V[i]
        i += 1
    assert i == len(REF_P)
