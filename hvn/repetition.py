import __init__ as hvn
from statistics import mode
import math

def runList(lMax):
    pScoreList = []
    for x in range(0,lMax):
        pScoreList.append(hvn.generate_power_score())
    print("Power Score is a random number 1-100")
    print("Number of Times Power Score was Generated:",len(pScoreList))
    pScoreSet = set(pScoreList)
    print(len(pScoreSet),"out of 100 possible different numbers generated")
    print("Lowest Power Score Generated:", min(pScoreSet))
    print("Highest Power Score Generated:", max(pScoreSet))
    print("Average Power Score:", math.floor(sum(pScoreList)/len(pScoreList)))
    print("Most Common Power Score:", mode(pScoreList))

def nameTest(lMax):
    nameList = []
    for x in range(0, lMax):
        race = hvn.generate_race()
        gender = hvn.generate_gender()
        full_name = hvn.generate_full_name(race, gender)
        nameList.append(full_name)
    print("Full Name Generation Testing")
    print("Number of Times a Full Name was Generated:",len(nameList))
    nameSet = set(nameList)
    print("Number of Unique Full Names", len(nameSet), "of", len(nameList))

def characterGenTest():
     power_score = hvn.generate_power_score()
     print("Power Score:", power_score)

     race = hvn.generate_race()
     gender = hvn.generate_gender()
     class_name = hvn.generate_class()
     full_name = hvn.generate_full_name(race, gender)
     profession = hvn.generate_profession(power_score)
     level = hvn.generate_level(power_score)
     hit_dice = hvn.generate_hit_dice(level, class_name)
     ability_scores, ability_mods = hvn.generate_ability_scores(race, class_name)
     saving_throws = hvn.generate_saves(level, class_name, ability_mods)
     skill_throws = hvn.generate_skills(level, class_name, ability_mods)

     print("Name:", full_name[0], full_name[1])
     print("Race:", race)
     print("Gender:", gender)
     print("Profession:", profession)
     print("Level:", level)
     print("Hit Dice:", hit_dice)
     print("Class:", class_name)
     print("Stats:")
     for ability, score in ability_scores.items():
         sign = "+" if ability_mods[ability] >= 0 else ""
         print(f"\t{ability}: {score:2d} ({sign}{ability_mods[ability]})")
     print("Saving Throws:")
     for ability, bonus in saving_throws.items():
         sign = "+" if bonus >= 0 else ""
         print(f"\t{ability}: {sign}{bonus}")
     print("Skill Bonuses:")
     for skill, bonus in skill_throws.items():
         sign = "+" if bonus >= 0 else ""
         print(f"\t{skill}: {sign}{bonus}")

print("Running Power Score Test with 100 Scores")
runList(100)
print("\n")
print("Running Power Score Test with 1000 Scores")
runList(1000)
print("\n")
print("Running Power Score Test with 10000 Scores")
runList(10000)
print("\n")
print("Running Name Test with 100 Names")
nameTest(100)
print("\n")
print("Running Name Test with 1000 Names")
nameTest(1000)
print("\n")
print("Running Name Test with 10000 Names")
nameTest(10000)
print("\n")
print("Generating a Test Character:")
characterGenTest()