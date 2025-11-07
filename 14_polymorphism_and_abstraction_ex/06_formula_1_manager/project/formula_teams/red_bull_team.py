from project.formula_teams.formula_team import FormulaTeam


sponsors = {
    1: 1_520_000,
    2: 820_000,
    3: 20_000,
    4: 20_000,
    5: 20_000,
    6: 20_000,
    7: 20_000,
    8: 20_000,
    9: 20_000,
    10: 10_000
}


class RedBullTeam(FormulaTeam):
    EXPENSES_PER_RACE = 250_000

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos > 10:
            revenue = -self.EXPENSES_PER_RACE
        else:
            revenue = sponsors[race_pos] - self.EXPENSES_PER_RACE

        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
