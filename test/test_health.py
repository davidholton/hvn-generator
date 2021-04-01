from . import hvn


def test_hit_dice():
    """
    Verifies that fetching the hit dice from the JSON works

    hvn.generate_hit_dice(level: int, class_name: str): str
    """

    # Test on different levels with same class
    assert(hvn.generate_hit_dice(1, "commoner") == "1d6")
    assert(hvn.generate_hit_dice(2, "commoner") == "2d6")
    assert(hvn.generate_hit_dice(3, "commoner") == "3d6")

    # Test with different class
    assert(hvn.generate_hit_dice(1, "warrior") == "1d8")
    assert(hvn.generate_hit_dice(2, "warrior") == "2d8")
    assert(hvn.generate_hit_dice(3, "warrior") == "3d8")


def test_hit_points():
    """
    Test that the correct hit points are generated with a given class and
    consitution modifier

    hvn.generate_hit_points(class_name: str, modifiers: dict): int
    """

    # Only need a dictionary with "con" defined
    assert(hvn.generate_hit_points("commoner", {"con": 0}) == 6)
    assert(hvn.generate_hit_points("commoner", {"con": 1}) == 7)
    assert(hvn.generate_hit_points("commoner", {"con": 2}) == 8)
    assert(hvn.generate_hit_points("commoner", {"con": 3}) == 9)

    # Test with a different class
    assert(hvn.generate_hit_points("warrior", {"con": 0}) == 8)
    assert(hvn.generate_hit_points("warrior", {"con": 1}) == 9)
    assert(hvn.generate_hit_points("warrior", {"con": 2}) == 10)
    assert(hvn.generate_hit_points("warrior", {"con": 3}) == 11)
