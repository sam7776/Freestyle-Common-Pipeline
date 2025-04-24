def print_sonu():
    s = [
        " SSS ",
        "S     ",
        " SSS ",
        "    S",
        " SSS "
    ]
    o = [
        " OOO ",
        "O   O",
        "O   O",
        "O   O",
        " OOO "
    ]
    n = [
        "N   N",
        "NN  N",
        "N N N",
        "N  NN",
        "N   N"
    ]
    u = [
        "U   U",
        "U   U",
        "U   U",
        "U   U",
        " UUU "
    ]

    # Combine all letters row by row
    for row in range(5):
        print(s[row] + "  " + o[row] + "  " + n[row] + "  " + u[row])

print_sonu()
