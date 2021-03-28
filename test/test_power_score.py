from . import hvn


def test_power_score():
    """
    Assert power score is [1, 100]
    """
    power_score = hvn.generate_power_score()

    if 1 <= power_score <= 100:
        return True
    return False


def test_level():
    """
    Verify that the level intervals are correct based off of a power level
    """

    # Level 1 interval
    if hvn.generate_level(1) != 1 and hvn.generate_level(20) != 1:
        return False

    # Level 2 interval
    if hvn.generate_level(21) != 2 and hvn.generate_level(50) != 2:
        return False

    # Level 3 interval
    if hvn.generate_level(51) != 3 and hvn.generate_level(80) != 3:
        return False

    # Level 4 interval
    if hvn.generate_level(81) != 4 and hvn.generate_level(90) != 4:
        return False

    # Level 5 interval
    if hvn.generate_level(91) != 5 and hvn.generate_level(100) != 5:
        return False

    return True
