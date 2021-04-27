import random
import json
import math
import os

module_dir = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------- #

# The one time Lua beats out Python. Wish I had a rawset(_G, k, v)
with open(os.path.join(module_dir, "data/classes.json")) as f:
    classes = json.load(f)

with open(os.path.join(module_dir, "data/names.json")) as f:
    names = json.load(f)

with open(os.path.join(module_dir, "data/professions.json")) as f:
    professions = json.load(f)

with open(os.path.join(module_dir, "data/races.json")) as f:
    races = json.load(f)

with open(os.path.join(module_dir, "data/equipment.json")) as f:
    equipment = json.load(f)

with open(os.path.join(module_dir, "data/treasure.json")) as f:
    treasure = json.load(f)

with open(os.path.join(module_dir, "data/fluff.json")) as f:
    fluff = json.load(f)


def get_classes() -> list:
    """
    Return a list of possible classes
    """

    return list(classes.keys())


def get_professions() -> list:
    """
    Return a list of possible professions
    """

    low = professions.get("low")
    medium = professions.get("medium")
    high = professions.get("high")

    return low + medium + high


def get_professions_organized() -> dict:
    """
    Return a dict of possible professions organized by ranking
    """

    low = professions.get("low")
    medium = professions.get("medium")
    high = professions.get("high")

    return {"low": low, "medium": medium, "high": high}


def get_races() -> list:
    """
    Return a list of possible races
    """

    return list(races.keys())


def get_equipment() -> dict:
    """
    Return a dictionary with three lists of armor, melee, and ranged equipment
    """

    equip = {"armor": [], "melee": [], "ranged": []}

    def populate(source, category):
        for catergories in source.values():
            for item_name in catergories.keys():
                equip.get(category).append(item_name)

    populate(equipment["armor"], "armor")
    equip["armor"].append("shield")

    populate(equipment["weapons"]["melee"], "melee")
    populate(equipment["weapons"]["ranged"], "ranged")

    return equip


def get_treasure() -> dict:
    """
    Return a dictionary the possible treasure
    """

    low = treasure.get("low")
    medium = treasure.get("medium")
    high = treasure.get("high")

    return {"low": low, "medium": medium, "high": high}


def get_fluff() -> dict:
    """
    Return a dictionary with the fluff data. Very similar to the actual JSON
    format, but I removed the objects with weights in replace with just lists
    of the keys.
    """

    def dict_to_list(d: dict) -> list:
        return [t for t in d.keys() if t != "nothing"]

    basic = {}
    for k, v in fluff["physicalBasic"].items():
        basic[k] = v

    maiming = dict_to_list(fluff["physicalMaiming"])

    scarring = {}
    for k, v in fluff["physicalScarring"].items():
        scarring[k] = dict_to_list(v)

    socialQuirks = dict_to_list(fluff["socialQuirks"])
    vocalQuirks = dict_to_list(fluff["vocalQuirks"])

    return {"physicalBasic": basic, "maiming": maiming, "scarring": scarring,
            "socialQuirks": socialQuirks, "vocalQuirks": vocalQuirks}

# --------------------------------------------------------------------------- #


def set_seed(seed: int) -> None:
    random.seed(seed)
    return


def roll(d: int, n: int, sort: bool = False, reverse: bool = False) -> list:
    """
    Return a list of random numbers generated by the dice-notation. Such as
    "AdX" where A is the number of rolls, and X is the number of faces on a
    dice. Additional parameters will sort the list in ascending or descending
    order.
    """

    rolls = [random.randint(1, n) for x in range(d)]

    if sort:
        rolls.sort(reverse=reverse)

    return rolls


def get_bonus(level) -> int:
    """
    Helper function for gen_saves and gen_skills.
    """

    return math.ceil((level / 4) + 1)


skill_to_ability = {
    "athletics": "str",
    "acrobatics": "dex",
    "sleightHand": "dex",
    "stealth": "dex",
    "arcana": "int",
    "history": "int",
    "investigation": "int",
    "nature": "int",
    "religion": "int",
    "animalHandling": "wis",
    "insight": "wis",
    "medicine": "wis",
    "perception": "wis",
    "survival": "wis",
    "deception": "cha",
    "intimidation": "cha",
    "performance": "cha",
    "persuasion": "cha"
}


# --------------------------------------------------------------------------- #


class HVNGenerator():
    fields = ["power_score", "level", "race", "gender", "class_name",
              "first_name", "last_name", "full_name", "profession",
              "abilities", "modifiers", "saving_throws", "skill_bonuses",
              "equipment", "armor", "armor_class", "hit_dice", "hit_points",
              "feature", "treasure", "person_wealth", "home_wealth",
              "physical_traits"]

    def __init__(self, custom_data: dict = {}):
        self.custom_data = set()
        for field in self.fields:
            setattr(self, field, None)

        self.set_custom_data(custom_data)

    def set_custom_data(self, data: dict):
        self.custom_data = set()

        for k, v in data.items():
            assert k in self.fields, f"{k} is not a field in HVNGenerator!"
            self.custom_data.add(k)
            setattr(self, k, v)

    def gen_power_score(self) -> int:
        """
        Creates the character's internal power score [1, 100]. Power score is
        used to determine how interesting a character information will be. The
        higher score means a character that has a higher potential
        """

        rolls = roll(3, 100, True)
        self.power_score = rolls[0]

        return self.power_score

    def gen_level(self) -> int:
        """
        Returns a character level [1, 5] based off of a power score [1, 100]
        """

        # TODO(dave): maybe rewrite? too weighted towards low levels
        self.level = max(1, math.ceil(self.power_score / 20))

        return self.level

    def gen_race(self) -> str:
        """
        From the race JSON file make two lists. One for the population and the
        weights associated. Use random.choices to make a weighted choice.
        """

        population = []
        weights = []

        for race in races.items():
            population.append(race[0])
            weights.append(race[1]["weight"])

        # Subscripted to pull out from returned list
        self.race = random.choices(population, weights)[0]

        return self.race

    def gen_gender(self) -> str:
        """
        Pick a random string from the genders list. Only "male" and "female".
        Uncertain if that will change. Good enough for now.
        """

        genders = ["male", "female"]
        self.gender = random.choice(genders)

        return self.gender

    def gen_class(self) -> str:
        """
        Same idea as gen_races. See that for details.
        """

        population = []
        weights = []

        for class_name in classes.items():
            population.append(class_name[0])
            weights.append(class_name[1]["weight"])

        # Subscripted to pull out from returned list
        self.class_name = random.choices(population, weights)[0]

        return self.class_name

    def gen_first_name(self) -> str:
        """
        Pick a random first name based on gender and potentially race. If the
        race has race based names pick one of those 85% of the time
        (determined by `chance_of_generic_name`). Otherwise pick a generic name
        """

        name_lookup = None

        if self.race == "dwarf":
            name_lookup = "dwarf"
        elif self.race in {"elf", "half-elf"}:
            name_lookup = "elf"
        elif self.race in {"orc", "half-orc"}:
            name_lookup = "orc"

        # 15% chance if a character has a race-specific name that we use a
        # generic name instead, 85% chance for race-specific.
        if name_lookup:
            chance_of_generic_name = 0.15

            if random.random() <= chance_of_generic_name:
                name_lookup = "generic"
        else:
            name_lookup = "generic"

        valid_names = names[name_lookup + "First"].get(self.gender)
        self.first_name = random.choice(valid_names)

        return self.first_name

    def gen_last_name(self) -> str:
        """
        Same procedure as `gen_first_name` except that last names do not have
        gendered variants.
        """

        name_lookup = None

        if self.race == "dwarf":
            name_lookup = "dwarf"
        elif self.race in {"elf", "half-elf"}:
            name_lookup = "elf"
        elif self.race in {"orc", "half-orc"}:
            name_lookup = "orc"

        # 15% chance if a character has a race-specific name that we use a
        # generic name instead, 85% chance for race-specific.
        if name_lookup:
            chance_of_generic_name = 0.15

            if random.random() <= chance_of_generic_name:
                name_lookup = "generic"
        else:
            name_lookup = "generic"

        valid_names = names[name_lookup + "Last"]
        self.last_name = random.choice(valid_names)

        return self.last_name

    def gen_full_name(self) -> tuple:
        """
        Does what it do
        """

        self.gen_first_name()
        self.gen_last_name()

        return (self.first_name, self.last_name)

    def gen_profession(self) -> str:
        """
        Takes power score translates that into a "profession bracket". High
        power score means a rarer profession. Check "professions.json" for the
        minimum threshold for each bracket.
        """

        bracket = "low"
        thresholds = professions["thresholds"]

        # Get the profession bracket
        for level in thresholds:
            if self.power_score >= thresholds.get(level):
                bracket = level
                break

        # From the bracket get the valid professions and pick a random one
        valid_professions = professions.get(bracket)
        self.profession = random.choice(valid_professions)

        return self.profession

    def gen_ability_scores(self) -> tuple:
        """
        Generate the ability scores and their modifiers based off of race
        modifiers and proper class distributions.
        """

        abilities = {
            "str": 0, "dex": 0, "con": 0,
            "int": 0, "wis": 0, "cha": 0,
        }

        modifiers = {}

        A = 4
        X = 6
        # Grabs the three highest rolls from a AdX roll six times
        rolls = [sum(roll(A, X, True)[-3:]) for i in range(6)]
        # To ensure randomness for non distributed classes we do NOT sort rolls

        # Apply the class distribution
        distribution = classes.get(self.class_name)["distribution"]
        for ability in distribution:
            # Pop the largest roll
            largest = rolls.pop(rolls.index(max(rolls)))
            abilities[ability] += largest

        # Apply non-specified ability scores
        for ability in set(abilities) - set(distribution):
            score = rolls.pop()
            abilities[ability] += score

        # Adjust for race modifiers
        race_modifiers = races.get(self.race)["modifiers"]
        for ability in race_modifiers:
            abilities[ability] += race_modifiers[ability]

        # Create the final modifiers after race modifers are applied
        for ability, score in abilities.items():
            modifiers[ability] = math.floor((score - 10) / 2)

        self.abilities = abilities
        self.modifiers = modifiers

        return (self.abilities, self.modifiers)

    def gen_saves(self) -> tuple:
        """
        Generate the saving throw bonuses for each ability. Each bonus is the
        ability modifier. If the character class is proficient in the ability
        then add an additional bonus to that ability.
        """

        # Calculate the saving throw bonus per level
        bonus = get_bonus(self.level)
        prof_abilities = classes.get(self.class_name)["saveProf"]

        # Saving throw for each ability is the modifier + the bonus if they are
        # proficient in the ability
        saving_throws = {}
        for ability, modifier in self.modifiers.items():
            saving_throws[ability] = modifier
            if prof_abilities.get(ability):
                saving_throws[ability] += bonus

        self.saving_throws = saving_throws
        return self.saving_throws

    def gen_skills(self) -> dict:
        """
        For each skill (in skill_to_ability) get the modifier based on its
        associated ability. If class is proficient in the skill add the level
        bonus
        """

        bonus = get_bonus(self.level)
        prof_skills = classes.get(self.class_name)["skillProf"]

        skills = {}
        for skill, ability in skill_to_ability.items():
            skills[skill] = self.modifiers[ability]
            if prof_skills.get(skill):
                skills[skill] += bonus

        self.skill_bonuses = skills
        return self.skill_bonuses

    def gen_equipment(self) -> dict:
        """
        Generate the characters equipment based off of their class and level.
        Returns a dict filled with the weapons. If a weapon is one-handed we
        also might add a shield in the return dictionary if you also generate
        the armor. Weapons with a sister weapon will also get that variant.
        Ranged weapons are also given to randomly based off a chance.
        """

        # Get the dictionary of proficient weapons by the character class
        prof_weaps = classes.get(self.class_name)["equipProf"]["weapons"]
        prof_weaps = list(prof_weaps.keys())

        # Decide if the melee weapon will be either "simple" or "martial"
        # * Assuming the character is proficient in both *
        weapon_type = prof_weaps[random.randrange(len(prof_weaps))]

        # Pick a random melee weapon
        weapons = equipment["weapons"]["melee"].get(weapon_type)
        weapon_name, weapon = random.choice(list(weapons.items()))

        # If the weapon has a sister weapon be sure to add that one as well
        char_equipment = {weapon_name: weapon}
        if weapon.get("sister"):
            sister = weapons.get(weapon["sister"])
            char_equipment[weapon["sister"]] = sister

        # Generate a ranged weapon
        ranged_chance = min(1, 0.25 * self.level)
        if random.random() <= ranged_chance:
            # Chance of having a ranged weapon goes up by 25% per level
            weapon_type = prof_weaps[random.randrange(len(prof_weaps))]

            weapons = equipment["weapons"]["ranged"].get(weapon_type)
            weapon_name, weapon = random.choice(list(weapons.items()))

        self.equipment = char_equipment
        return self.equipment

    def gen_armor(self) -> dict:
        """
        Generate the characters armor and armor class. If a character generates
        a shield we also add it to their equipment dictionary. Returns a tuple
        of the armor name, armor, and armor class.
        """

        prof_armor = classes.get(self.class_name)["equipProf"]["armor"]

        # Create a list of the proficient armors that the character can use
        # Weights are decided off of power score
        population = []
        weights = []

        # Scuffed thresholds. What are you going to do?
        if prof_armor.get("light"):
            population.append("light")
            weights.append(2 if self.power_score <= 20 else 1)

        if prof_armor.get("medium"):
            population.append("medium")
            weights.append(1 if self.power_score <= 20 else 2)

        if prof_armor.get("heavy"):
            population.append("heavy")
            weights.append(2 if self.power_score <= 50 else 3)

        # Pick the armor level
        armor_level = random.choices(population, weights)[0]
        # Get the possible armors from that level
        armors = list(equipment["armor"].get(armor_level))

        # Pick a random armor from that armor level
        # If we are picking from the heavy armor level and it happens to be a
        # full-plate armor make sure the character is at least level three
        while True:
            armor_name = random.choice(armors)

            if self.level >= 3 or armor_name != "plate":
                break

        armor = equipment["armor"].get(armor_level).get(armor_name)
        ac = armor["ac"]

        # Add dex modifier if applicable
        if armor["dex"]:
            ac += min(self.modifiers["dex"], armor["dexMax"])

        # Check if the character has a one-handed weapon
        one_handed = False
        for item in self.equipment.values():
            if item["oneHand"]:
                one_handed = True
                break

        # Generate a shield if the character has a one-handed weapon and they
        # are proficient with a shield
        if prof_armor.get("shield") and one_handed:
            # Chance of having a shield increases by 25% per level
            # Max of 100% of course
            shield_chance = min(1, 0.25 * self.level)
            if random.random() <= shield_chance:
                self.equipment["shield"] = equipment["shield"]
                ac += equipment["shield"]["acBonus"]
                # NOTE(dave): unsure if we actually add the ac bonus to the ac
                # as shields seem to be situational

        armor["name"] = armor_name
        self.armor = armor
        self.armor_class = ac
        return (self.armor, self.armor_class)

    def gen_hit_dice(self) -> str:
        """
        Returns a string that follows dice-notation. Where rolls is the
        characters level and the dice is the predefined class hit dice.
        """

        dice = classes.get(self.class_name)["hdMax"]
        self.hit_dice = str(self.level) + "d" + str(dice)

        return self.hit_dice

    def gen_hit_points(self) -> int:
        """
        Calculates the hit points for a character. Based on constitution
        modifier plus highest value on the class assigned hit dice.
        """

        dice = classes.get(self.class_name)["hdMax"]
        self.hit_points = dice + self.modifiers["con"]

        return self.hit_points

    def gen_feature(self) -> str:
        """
        Generate a random feature from the class's features list. Features are
        only generated based on a predefined class feature chance value.
        """

        feature_chance = classes.get(self.class_name)["featureChance"]

        if random.random() <= feature_chance:
            valid_features = classes.get(self.class_name)["features"]
            self.feature = random.choice(valid_features)
        else:
            self.feature = None

        return self.feature

    def gen_treasure(self):
        """
        Generate three categories of treasure, gems, trinkets, and junk. Power
        score determines what categories are picked from. Level increases
        chances to generate that category. Multiple gems can be generated based
        on power level
        """

        # Helper function to pick an item from each category
        def pick_treasure(category):
            level = random.choice(options)
            item = random.choice(treasure[level][category])
            loot.append(item)

        options = []
        thresholds = treasure["thresholds"]

        # Get the possible loot tables from the power score
        for level in thresholds:
            if self.power_score >= thresholds.get(level):
                options.append(level)

        loot = []

        # Calculate the number of gems to generate
        num_gems = 0
        if self.power_score > 5:
            gem_chance = 0.1 + min(self.level * 0.05, 0.25)
            if random.random() <= gem_chance:
                if self.power_score < 10:
                    num_gems = 1
                else:
                    num_gems = self.power_score // 10

        # Pick the gem(s)
        for x in range(num_gems):
            pick_treasure("gems")

        # Pick the trinket
        trinket_chance = 0.5 + min(self.level * 0.10, 0.50)
        if random.random() <= trinket_chance:
            pick_treasure("trinkets")

        # Pick the junk
        junk_chance = 0.5 + min(self.level * 0.10, 0.50)
        if random.random() <= junk_chance:
            pick_treasure("junk")

        self.treasure = loot
        return loot

    def gen_wealth(self) -> dict:
        """
        Generate wealth (gold pieces, silver pieces, and copper pieces) for the
        characters on-person wealth and at-home wealth. On person wealth is
        based on power score, and at-home wealth is scaled off the
        corresponding on-person wealth.
        """

        person_wealth = {"gp": 0, "sp": 0, "cp": 0}
        home_wealth = {"gp": 0, "sp": 0, "cp": 0}

        person_wealth["gp"] = self.power_score // 2
        person_wealth["sp"] = self.power_score + random.randint(0, 10)
        person_wealth["cp"] = (self.power_score + 1) * 3

        def calc_home(key):
            scale_factor = 4.35
            home_wealth[key] = int((person_wealth[key] + 2) * scale_factor)

        calc_home("gp")
        calc_home("sp")
        calc_home("cp")

        self.person_wealth = person_wealth
        self.home_wealth = home_wealth
        return self.person_wealth, self.home_wealth

    def gen_physical_traits(self) -> dict:
        """
        Return a dictionary that defines how a character should look. The keys
        are eyes, hairColor, hairStyle, skin, and maiming whose values are
        strings and. Then the key scarring is a sub-dictionary with key, string
        pairs describing locations of where scars are.

        The maiming and scarring are chosen off of weights/
        """

        # Helper to pick a single random element from a weighted population
        def weighted_choice(d: dict):
            population = []
            weights = []

            for key, weight in d.items():
                population.append(key)
                weights.append(weight)

            return random.choices(population, weights)[0]

        traits = {}

        # Basic character traits
        basic = ["eyes", "hairColor", "hairStyle", "skin", "frame"]
        for trait in basic:
            options = fluff["physicalBasic"].get(trait)
            traits[trait] = random.choice(options)

        # Maiming
        maiming = weighted_choice(fluff["physicalMaiming"])
        maiming = None if maiming == "nothing" else maiming

        traits["maiming"] = maiming

        # Scarring is a dictionary
        traits["scarring"] = {}
        for place, options in fluff["physicalScarring"].items():
            choice = weighted_choice(options)
            choice = None if choice == "nothing" else choice

            traits["scarring"][place] = choice

        self.physical_traits = traits
        return self.physical_traits

    def generate(self):
        def protect(key: str, f):
            """
            Scuffed fix, but all this does is make sure that the function does
            not overwrite whatever pre-existing / custom data.
            """
            if key not in self.custom_data:
                f()
                # print(f"{key} is not defined")

        protect("power_score", self.gen_power_score)
        protect("level", self.gen_level)

        protect("race", self.gen_race)
        protect("gender", self.gen_gender)
        protect("class_name", self.gen_class)

        protect("first_name", self.gen_first_name)
        protect("last_name", self.gen_last_name)
        protect("profession", self.gen_profession)

        protect("abilities", self.gen_ability_scores)
        protect("saving_throws", self.gen_saves)
        protect("skill_bonuses", self.gen_skills)

        protect("equipment", self.gen_equipment)
        protect("armor", self.gen_armor)

        protect("hit_dice", self.gen_hit_dice)
        protect("hit_points", self.gen_hit_points)

        protect("feature", self.gen_feature)
        protect("treasure", self.gen_treasure)
        protect("person_wealth", self.gen_wealth)

        protect("physical_traits", self.gen_physical_traits)

    def __repr__(self):
        hr = "=" * 12 + "\n"
        out = ""

        out += hr
        out += f"Power Score: {self.power_score}\n"
        out += hr
        out += f"Full Name: {self.first_name} {self.last_name}\n"
        out += f"Gender: {self.gender}\n"
        out += f"Race: {self.race}\n"
        out += f"Class: {self.class_name}\n"
        out += f"Profession: {self.profession}\n"
        out += hr
        out += f"Level: {self.level}\n"
        out += f"AC: {self.armor_class}\n"
        out += f"HP: {self.hit_points}\n"
        out += f"Hit Dice: {self.hit_dice}\n"
        out += hr
        out += "Abilities:\n"
        if self.abilities:
            for ability, score in self.abilities.items():
                sign = "+" if self.modifiers[ability] >= 0 else ""
                modifier = f"{sign}{self.modifiers[ability]}"
                out += (f"\t{ability}: {score:2d} ({modifier})\n")

        out += "Saving Throws:\n"
        if self.saving_throws:
            for ability, bonus in self.saving_throws.items():
                sign = "+" if bonus >= 0 else ""
                out += f"\t{ability}: {sign}{bonus}\n"

        out += "Skill Bonuses:\n"
        if self.skill_bonuses:
            for skill, bonus in self.skill_bonuses.items():
                sign = "+" if bonus >= 0 else ""
                out += f"\t{skill}: {sign}{bonus}\n"
        out += hr

        if self.feature:
            out += "Feature:\n"
            out += self.feature + "\n"

        out += "Treasures:\n"
        if self.treasure:
            for treasure in self.treasure:
                out += treasure + "\n"

        out += "On-person Wealth:\n"
        if self.person_wealth:
            for k, v in self.person_wealth.items():
                out += f"{v}{k}\n"

        out += "At-home Wealth:\n"
        if self.home_wealth:
            for k, v in self.home_wealth.items():
                out += f"{v}{k}\n"
        out += hr

        out += "Physical traits:\n"
        for trait, value in self.physical_traits.items():
            if type(value) is dict:
                for x, v in value.items():
                    if v:
                        out += f"{x} scarring: {v}\n"
            elif value:
                out += f"{trait}: {value}\n"
        out += hr

        return out


# --------------------------------------------------------------------------- #


# if __name__ == "__main__":

#     gen = HVNGenerator()

#     gen.set_custom_data({"power_score": 10})
#     gen.generate()

#     print(gen)
