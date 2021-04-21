from . import hvn
from collections import Counter
import math


def test_positive_scores():
    """
    Assert that all scores are non-negative
    """

    char = hvn.HVNGenerator()

    char.race, char.class_name = "human", "commoner"

    ability_scores, _ = char.gen_ability_scores()
    for ability, score in ability_scores.items():
        assert(score >= 0)


def test_score_distribution():
    """
    Makes sure that the specified distribution of ability scores are correct.
    If three scores are priorities this accounts for the case that the third
    score is still in the top three generated scores if the fourth score has
    an equal value.
    """

    char = hvn.HVNGenerator()

    char.race, char.class_name = "human", "commoner"
    # Commoner order: con, str, wis

    ability_scores, _ = char.gen_ability_scores()
    largest_scores = [v for k, v in Counter(ability_scores).most_common(3)]

    expected_scores = ["con", "str", "wis"]
    for index, ability in enumerate(expected_scores):
        assert(ability_scores[ability] == largest_scores[index])


def test_modifiers():
    """
    Verifies that the final score modifiers are correct
    """

    char = hvn.HVNGenerator()

    char.race, char.class_name = "human", "commoner"

    ability_scores, mods = char.gen_ability_scores()
    for ability, score in ability_scores.items():
        assert(mods[ability] == math.floor((score - 10) / 2))
