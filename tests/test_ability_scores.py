import hvn
from collections import Counter


def test_positive_scores():
    race_name, class_name = "human", "commoner"

    ability_scores = hvn.generate_ability_scores(race_name, class_name)
    for ability, score in ability_scores.items():
        assert(score >= 0)


def test_score_distribution():
    """
    Makes sure that the specified distribution of ability scores are correct.
    If three scores are priorities this accounts for the case that the third
    score is still in the top three generated scores if the fourth score has
    an equal value.
    """

    race_name, class_name = "human", "wizard"
    # Wizard order: int, con, dex

    ability_scores = hvn.generate_ability_scores(race_name, class_name)
    largest_scores = [v for k, v in Counter(ability_scores).most_common(3)]

    expected_scores = ["int", "con", "dex"]
    for index, ability in enumerate(expected_scores):
        assert(ability_scores[ability] == largest_scores[index])
