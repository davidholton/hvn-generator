from . import hvn


def test_power_score():
    """
    Assert power score is [1, 100]
    """

    char = hvn.HVNGenerator()
    power_score = char.gen_power_score()

    assert(1 <= power_score <= 100)


def test_level():
    """
    Verify that the level intervals are correct based off of a power level
    """

    char = hvn.HVNGenerator()

    # Level 1 interval
    char.power_score = 1
    assert(char.gen_level() == 1)
    char.power_score = 20
    assert(char.gen_level() == 1)

    # Level 2 interval
    char.power_score = 21
    assert(char.gen_level() == 2)
    char.power_score = 40
    assert(char.gen_level() == 2)

    # Level 3 interval
    char.power_score = 41
    assert(char.gen_level() == 3)
    char.power_score = 60
    assert(char.gen_level() == 3)

    # Level 4 interval
    char.power_score = 61
    assert(char.gen_level() == 4)
    char.power_score = 80
    assert(char.gen_level() == 4)

    # Level 5 interval
    char.power_score = 81
    assert(char.gen_level() == 5)
    char.power_score = 100
    assert(char.gen_level() == 5)
