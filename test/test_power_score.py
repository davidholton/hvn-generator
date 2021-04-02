from . import hvn


def test_power_score():
    """
    Assert power score is [1, 100]
    """
    power_score = hvn.generate_power_score()

    assert(1 <= power_score <= 100)


def test_level():
    """
    Verify that the level intervals are correct based off of a power level
    """

    # Level 1 interval
    assert(hvn.generate_level(1) == 1)
    assert(hvn.generate_level(20) == 1)

    # Level 2 interval
    assert(hvn.generate_level(21) == 2)
    assert(hvn.generate_level(40) == 2)

    # Level 3 interval
    assert(hvn.generate_level(41) == 3)
    assert(hvn.generate_level(60) == 3)

    # Level 4 interval
    assert(hvn.generate_level(61) == 4)
    assert(hvn.generate_level(80) == 4)

    # Level 5 interval
    assert(hvn.generate_level(81) == 5)
    assert(hvn.generate_level(100) == 5)
