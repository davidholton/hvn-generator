from . import hvn
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
    ability_scores, modifiers = hvn.generate_ability_scores(race, class_name)
    saving_throws = hvn.generate_saves(level, class_name, modifiers)
    skill_throws = hvn.generate_skills(level, class_name, modifiers)
    hit_points = hvn.generate_hit_points(class_name, modifiers)
    hit_dice = hvn.generate_hit_dice(level, class_name)
    equip = hvn.generate_equipment(level, class_name)
    bonus = hvn.get_bonus(level)
    prof_abilities = hvn.classes.get(class_name)["saveProf"]
    prof_skills = hvn.classes.get(class_name)["skillProf"]
    armor_name, armor, ac = hvn.generate_armor(power_score, level, class_name,
                                             modifiers, equip)
    print("Name:", full_name[0], full_name[1])
    print("Race:", race)
    print("Gender:", gender)
    print("Profession:", profession)
    print("Level:", level)
    print("Hit Points:", hit_points, "(", hit_dice, ")")
    #    print("Hit Dice:", hit_dice)
    print("AC:", ac, " (",armor_name,")")
    #print("Equipment:")
    #for name, item in equip.items():
    #    print(f"\t{name}: {item}")
    print("Archetype:", class_name)
    print("Stats:")
    for ability, score in ability_scores.items():
        sign = "+" if modifiers[ability] >= 0 else ""
        print(f"|{ability}: {score:2d} ({sign}{modifiers[ability]})|", end ='')
    print("")
    print("Saving Throws:")
    for ability, modifier in modifiers.items():
        if prof_abilities.get(ability):
            sign = "+" if modifiers[ability] >= 0 else ""
            print(f"\t{ability}: {sign}{modifiers[ability]}")
        
    print("Skill Bonuses:")
    for skill, bonus in skill_throws.items():
        if prof_skills.get(skill):
            sign = "+" if bonus >= 0 else ""
            print(f"\t{skill}: {sign}{bonus}")

def character_gen_test_verbose():
     power_score = hvn.generate_power_score()
     print("Power Score:", power_score)

     race = hvn.generate_race()
     gender = hvn.generate_gender()
     class_name = hvn.generate_class()
     full_name = hvn.generate_full_name(race, gender)
     profession = hvn.generate_profession(power_score)
     level = hvn.generate_level(power_score)
     ability_scores, modifiers = hvn.generate_ability_scores(race, class_name)
     saving_throws = hvn.generate_saves(level, class_name, modifiers)
     skill_throws = hvn.generate_skills(level, class_name, modifiers)
     hit_points = hvn.generate_hit_points(class_name, modifiers)
     hit_dice = hvn.generate_hit_dice(level, class_name)
     equip = hvn.generate_equipment(level, class_name)
     armor_name, armor, ac = hvn.generate_armor(power_score, level, class_name,
                                            modifiers, equip)

     print("Name:", full_name[0], full_name[1])
     print("Race:", race)
     print("Gender:", gender)
     print("Profession:", profession)
     print("Level:", level)
     print("Hit Points:", hit_points)
     print("Hit Dice:", hit_dice)
     print("AC:", ac)
     print("Class:", class_name)
     print("Stats:")
     for ability, score in ability_scores.items():
         sign = "+" if modifiers[ability] >= 0 else ""
         print(f"\t{ability}: {score:2d} ({sign}{modifiers[ability]})")
     print("Saving Throws:")
     for ability, bonus in saving_throws.items():
         sign = "+" if bonus >= 0 else ""
         print(f"\t{ability}: {sign}{bonus}")
     print("Skill Bonuses:")
     for skill, bonus in skill_throws.items():
         sign = "+" if bonus >= 0 else ""
         print(f"\t{skill}: {sign}{bonus}")
     print("Armor:")
     print(f"\t{armor_name}: {armor}")
     print("Equipment:")
     for name, item in equip.items():
         print(f"\t{name}: {item}")


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

    print("\nGenerating a Verbose Test Character:")
    character_gen_test_verbose()
