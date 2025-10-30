class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict[str, int] = {}
        self.guild: str = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost) -> str:
        for skill in self.skills.keys():
            if skill == skill_name:
                return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        output = [f"Name: {self.name}",
                  f"Guild: {self.guild}",
                  f"HP: {self.hp}",
                  f"MP: {self.mp}"]
        for skill, mana in self.skills.items():
            output.append(f"==={skill} - {mana}")
        return "\n".join(output)
