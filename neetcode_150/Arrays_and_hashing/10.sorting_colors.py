colors = [0, 1, 0, 2, 0, 0, 2, 0, 1]


def sort_colors(colors):
    count = [0] * 3

    for val in colors:
        count[val] += 1
    index = 0
    for clr in range(3):
        for _ in range(count[clr]):
            colors[index] = clr
            index += 1
    return colors


print(sort_colors(colors))
