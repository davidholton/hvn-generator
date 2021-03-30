import __init__ as hvn
from statistics import mode
import math


def run_list(n_scores):
    power_scores = []
    for x in range(0, n_scores):
        power_scores.append(hvn.generate_power_score())

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
        race = hvn.generate_race()
        gender = hvn.generate_gender()
        full_name = hvn.generate_full_name(race, gender)
        names.append(full_name)

    print("Full Name Generation Testing")
    print("Number of Times a Full Name was Generated:", n_scores)

    names_set = set(names)
    print(f"Number of Unique Full Names {len(names_set)} of {n_scores}")


def character_gen_test():
    power_score = hvn.generate_power_score()
    print("Power Score:", power_score)

    race = hvn.generate_race()
    gender = hvn.generate_gender()
    class_name = hvn.generate_class()
    full_name = hvn.generate_full_name(race, gender)
    profession = hvn.generate_profession(power_score)
    level = hvn.generate_level(power_score)
    hit_dice = hvn.generate_hit_dice(level, class_name)
    ability_scores, ability_mod = hvn.generate_ability_scores(race, class_name)
    saving_throws = hvn.generate_saves(level, class_name, ability_mod)
    skill_throws = hvn.generate_skills(level, class_name, ability_mod)

    print("Name:", full_name[0], full_name[1])
    print("Race:", race)
    print("Gender:", gender)
    print("Profession:", profession)
    print("Level:", level)
    print("Hit Dice:", hit_dice)
    print("Class:", class_name)
    print("Stats:")
    for ability, score in ability_scores.items():
        sign = "+" if ability_mod[ability] >= 0 else ""
        print(f"\t{ability}: {score:2d} ({sign}{ability_mod[ability]})")
    print("Saving Throws:")
    for ability, bonus in saving_throws.items():
        sign = "+" if bonus >= 0 else ""
        print(f"\t{ability}: {sign}{bonus}")
    print("Skill Bonuses:")
    for skill, bonus in skill_throws.items():
        sign = "+" if bonus >= 0 else ""
        print(f"\t{skill}: {sign}{bonus}")


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

print("\nGenerating a Test Character:")
character_gen_test()
