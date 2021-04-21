from . import hvn


def test_hit_dice():
    """
    Verifies that fetching the hit dice from the JSON works

    char.gen_hit_dice(): str
    """

    char = hvn.HVNGenerator()

    # Test on different levels with same class
    char.class_name = "commoner"
    char.level = 1
    assert(char.gen_hit_dice() == "1d6")
    char.level = 2
    assert(char.gen_hit_dice() == "2d6")
    char.level = 3
    assert(char.gen_hit_dice() == "3d6")

    # Test with different class
    char.class_name = "warrior"
    char.level = 1
    assert(char.gen_hit_dice() == "1d8")
    char.level = 2
    assert(char.gen_hit_dice() == "2d8")
    char.level = 3
    assert(char.gen_hit_dice() == "3d8")


def test_hit_points():
    """
    Test that the correct hit points are generated with a given class and
    consitution modifier

    hvn.generate_hit_points(class_name: str, modifiers: dict): int
    """

    char = hvn.HVNGenerator()

    # Only need a dictionary with "con" defined
    char.class_name = "commoner"
    char.modifiers = {"con": 0}
    assert(char.gen_hit_points() == 6)
    char.modifiers = {"con": 1}
    assert(char.gen_hit_points() == 7)
    char.modifiers = {"con": 2}
    assert(char.gen_hit_points() == 8)
    char.modifiers = {"con": 3}
    assert(char.gen_hit_points() == 9)

    # Test with a different class
    char.class_name = "warrior"
    char.modifiers = {"con": 0}
    assert(char.gen_hit_points() == 8)
    char.modifiers = {"con": 1}
    assert(char.gen_hit_points() == 9)
    char.modifiers = {"con": 2}
    assert(char.gen_hit_points() == 10)
    char.modifiers = {"con": 3}
    assert(char.gen_hit_points() == 11)
