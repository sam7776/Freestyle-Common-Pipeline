def print_stars():
    s = [
        " *** ",
        "*    ",
        " *** ",
        "    *",
        " *** "
    ]
    o = [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ]
    n = [
        "*   *",
        "**  *",
        "* * *",
        "*  **",
        "*   *"
    ]
    u = [
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ]

    # Combine all letters row by row
    for row in range(5):
        print(s[row] + "  " + o[row] + "  " + n[row] + "  " + u[row])

print_stars()
