from project.formula_teams.formula_team import FormulaTeam


sponsors = {
    1: 1_100_000,
    2: 600_000,
    3: 600_000,
    4: 100_000,
    5: 100_000,
    6: 50_000,
    7: 50_000
}


class MercedesTeam(FormulaTeam):
    EXPENSES_PER_RACE = 200_000

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos > 7:
            revenue = -self.EXPENSES_PER_RACE
        else:
            revenue = sponsors[race_pos] - self.EXPENSES_PER_RACE

        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
