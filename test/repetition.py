from . import hvn
from statistics import mode
import math


def run_list(n_scores):
    power_scores = []
    for x in range(0, n_scores):
        char = hvn.HVNGenerator()
        power_score = char.gen_power_score()

        power_scores.append(power_score)

    print("Power Score is a random number 1-100")
    print("Number of Times Power Score was Generated:", n_scores)

    scores_set = set(power_scores)
    print(len(scores_set), "out of 100 possible different numbers generated")
    print("Lowest Power Score Generated:", min(scores_set))
    print("Highest Power Score Generated:", max(scores_set))
    print("Average Power Score:", math.floor(sum(power_scores) / n_scores))
    print("Most Common Power Score:", mode(power_scores))


def name_test(n_scores):
    names = []
    for x in range(0, n_scores):
        char = hvn.HVNGenerator()
        char.gen_race()
        char.gen_gender()

        full_name = char.gen_full_name()
        names.append(full_name)

    print("Full Name Generation Testing")
    print("Number of Times a Full Name was Generated:", n_scores)

    names_set = set(names)
    print(f"Number of Unique Full Names {len(names_set)} of {n_scores}")


def character_gen_test():
    char = hvn.HVNGenerator()
    char.generate()

    print(char)


def test_repetition():
    print("Running Power Score Test with 100 Scores:")
    run_list(100)

    print("\nRunning Power Score Test with 1000 Scores:")
    run_list(1000)

    print("\nRunning Power Score Test with 10000 Scores:")
    run_list(10000)

    print("\nRunning Name Test with 100 Names:")
    name_test(100)

    print("\nRunning Name Test with 1000 Names:")
    name_test(1000)

    print("\nRunning Name Test with 10000 Names:")
    name_test(10000)

    print("\nGenerating a Clean Test Character:")
    character_gen_test()
