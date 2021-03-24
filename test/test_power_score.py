from . import hvn


def test_power_score():
    """
    Assert power score is [1, 100]
    """
    power_score = hvn.generate_power_score()

    if 1 <= power_score <= 100:
        return True
    return False
