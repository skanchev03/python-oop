def print_row_of_rhombus(spaces: int, stars: int):
    print(f"{' ' * spaces}{'* ' * stars}")


def print_top_part_of_rhombus(n: int):
    for row in range(1, n+1):
        print_row_of_rhombus(n-row, row)


def print_bottom_part_of_rhombus(n: int):
    for row in range(1, n):
        print_row_of_rhombus(row, n-row)


def print_rhombus(n: int):
    print_top_part_of_rhombus(n)
    print_bottom_part_of_rhombus(n)


n = int(input())
print_rhombus(n)
