import sys


def load_coords_radius(file1):
    with open(file1, 'r') as file:
        x, y = map(float, file.readline().split())
        r = float(file.readline())
    return x, y, r


def point_position(x, y, r, a, b):
    d = r ** 2
    p = (x - a) ** 2 + (y - b) ** 2
    if p > d:
        return 2
    elif p == d:
        return 0
    elif p < d:
        return 1


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    x, y, r = load_coords_radius(file1)

    with open(file2, 'r') as file:
        for points in file:
            a, b = map(float, points.strip().split())
            print(point_position(x, y, r, a, b))
