import codility.L10.Flags as actual


def test_given():
    assert 3 == actual.solution([1, 6, 3, 6, 5, 6, 5, 6, 3, 2, 6, 1])
    assert 3 == actual.solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])
    assert 4 == actual.solution([0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0])
