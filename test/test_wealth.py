from . import hvn


def assert_expected(values, expected):
    """
    Helper function that asserts that two dictionaries are the same
    """

    assert(len(values) == len(expected))
    for k, v in values.items():
        assert(expected[k] == v)


def test_person_wealth():
    """
    Based on a power score test the on-person wealth. The silver pieces have a
    bit of randomness, so we test on range
    """

    char = hvn.HVNGenerator()

    # Low power score test
    char.set_custom_data({"power_score": 1})
    (person, _) = char.gen_wealth()

    assert(person["gp"] == 0)
    assert(0 <= person["sp"] <= 11)
    assert(person["cp"] == 6)

    # Test rounding
    char.set_custom_data({"power_score": 2})
    (person, _) = char.gen_wealth()

    assert(person["gp"] == 1)
    assert(2 <= person["sp"] <= 12)
    assert(person["cp"] == 9)

    # High power score test
    char.set_custom_data({"power_score": 100})
    (person, _) = char.gen_wealth()

    assert(person["gp"] == 50)
    assert(100 <= person["sp"] <= 110)
    assert(person["cp"] == 303)


def test_home_wealth():
    """
    Similiar to the test_person_wealth case but for at-home wealth
    """

    char = hvn.HVNGenerator()

    # Low power score test
    char.set_custom_data({"power_score": 1})
    (_, home) = char.gen_wealth()

    assert(home["gp"] == 8)
    assert(13 <= home["sp"] <= 56)
    assert(home["cp"] == 34)

    # Test rounding
    char.set_custom_data({"power_score": 2})
    (_, home) = char.gen_wealth()

    assert(home["gp"] == 13)
    assert(17 <= home["sp"] <= 60)
    assert(home["cp"] == 47)

    # High power score test
    char.set_custom_data({"power_score": 100})
    (_, home) = char.gen_wealth()

    assert(home["gp"] == 226)
    assert(108.7 <= home["sp"] <= 487)
    assert(home["cp"] == 1326)
