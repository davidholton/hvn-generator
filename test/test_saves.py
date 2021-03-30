from . import hvn


def assert_expected(values, expected):
    """
    Helper function that asserts that two dictionaries are the same
    """
    assert(len(values) == len(expected))
    for k, v in values.items():
        assert(expected[k] == v)


def test_saving_throws():
    """
    Check if the saving throws are generated correctly with the right bonuses
    """

    # Test with a level 1
    level, class_name = 1, "commoner"
    modifiers = {
        "str": 1, "dex": 1, "con": 1,
        "int": 1, "wis": 1, "cha": 1,
    }

    saving_throws = hvn.generate_saves(level, class_name, modifiers)
    assert_expected(saving_throws, {
        "str": 1, "dex": 1, "con": 3,
        "int": 1, "wis": 1, "cha": 1,
    })

    # Test level bonus works for same class
    level = 10
    saving_throws = hvn.generate_saves(level, class_name, modifiers)
    assert_expected(saving_throws, {
        "str": 1, "dex": 1, "con": 5,
        "int": 1, "wis": 1, "cha": 1,
    })

    # Test different classes work
    level, class_name = 4, "expert"
    modifiers = {
        "str": 1, "dex": 2, "con": 2,
        "int": 2, "wis": 4, "cha": -1,
    }

    saving_throws = hvn.generate_saves(level, class_name, modifiers)
    assert_expected(saving_throws, {
        "str": 1, "dex": 2, "con": 2,
        "int": 4, "wis": 6, "cha": -1,
    })
