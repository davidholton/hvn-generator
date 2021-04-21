from . import hvn


def assert_expected(values, expected):
    """
    Helper function that asserts that two dictionaries are the same
    """
    assert(len(values) == len(expected))
    for k, v in values.items():
        assert(expected[k] == v)


def test_level_bonus():
    """
    Ensure that the level bonus is correct when generating throw bonuses
    """
    count = 2
    for i in range(1, 50, 4):
        for j in range(i, i + 4):
            assert(hvn.get_bonus(j) == count)
        count += 1


def test_saving_throws():
    """
    Check if the saving throws are generated correctly with the right bonuses
    """

    char = hvn.HVNGenerator()

    # Test with a level 1
    char.level, char.class_name = 1, "commoner"
    char.modifiers = {
        "str": 1, "dex": 1, "con": 1,
        "int": 1, "wis": 1, "cha": 1,
    }

    saving_throws = char.gen_saves()
    assert_expected(saving_throws, {
        "str": 1, "dex": 1, "con": 3,
        "int": 1, "wis": 1, "cha": 1,
    })

    # Test level bonus works for same class
    char.level = 10
    saving_throws = char.gen_saves()
    assert_expected(saving_throws, {
        "str": 1, "dex": 1, "con": 5,
        "int": 1, "wis": 1, "cha": 1,
    })

    # Test different classes work
    char.level, char.class_name = 4, "expert"
    char.modifiers = {
        "str": 1, "dex": 2, "con": 2,
        "int": 2, "wis": 4, "cha": -1,
    }

    saving_throws = char.gen_saves()
    assert_expected(saving_throws, {
        "str": 1, "dex": 2, "con": 2,
        "int": 4, "wis": 6, "cha": -1,
    })


def test_skill_throws():
    """
    Check that each skill has the correct bonus for the characters class, level
    and ability modifiers.
    """

    char = hvn.HVNGenerator()

    # Test with a level 1
    char.level, char.class_name = 1, "commoner"
    char.modifiers = {
        "str": 1, "dex": 1, "con": 1,
        "int": 1, "wis": 1, "cha": 1,
    }

    skill_throws = char.gen_skills()
    assert_expected(skill_throws, {
        "athletics": 3, "acrobatics": 1, "sleightHand": 1, "stealth": 1,
        "arcana": 1, "history": 1, "investigation": 1, "nature": 3,
        "religion": 1, "animalHandling": 1, "insight": 1, "medicine": 1,
        "perception": 1, "survival": 3, "deception": 1, "intimidation": 1,
        "performance": 1, "persuasion": 1
    })

    # Test level bonus works for same class
    char.level = 10
    skill_throws = char.gen_skills()
    assert_expected(skill_throws, {
        "athletics": 5, "acrobatics": 1, "sleightHand": 1, "stealth": 1,
        "arcana": 1, "history": 1, "investigation": 1, "nature": 5,
        "religion": 1, "animalHandling": 1, "insight": 1, "medicine": 1,
        "perception": 1, "survival": 5, "deception": 1, "intimidation": 1,
        "performance": 1, "persuasion": 1
    })

    # Test different classes work
    char.level, char.class_name = 4, "expert"
    char.modifiers = {
        "str": 1, "dex": 2, "con": 2,
        "int": 2, "wis": 4, "cha": -1,
    }

    skill_throws = char.gen_skills()
    assert_expected(skill_throws, {
        "athletics": 1, "acrobatics": 2, "sleightHand": 2, "stealth": 2,
        "arcana": 2, "history": 2, "investigation": 2, "nature": 2,
        "religion": 2, "animalHandling": 6, "insight": 6, "medicine": 6,
        "perception": 4, "survival": 4, "deception": -1, "intimidation": -1,
        "performance": -1, "persuasion": -1
    })
