import codility.L5.GenomicRangeQuery


def test_solution():
    assert codility.L5.GenomicRangeQuery.solution("CAGCCTA", [2, 5, 0], [4, 5, 6]) == [
        2,
        4,
        1,
    ]
