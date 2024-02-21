import sys


def get_path(n, m):
    path = []
    if n > 0:
        arr = [i for i in range(1, n + 1)]
        i = 0
        j = 0
        while True:
            value = arr[j % n]
            if i == 0:
                path.append(value)
            if value == arr[0]:
                if i == m - 1:
                    break
            i += 1
            j += 1
            if i == m:
                i = 0
                j -= 1
    return path


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    res = get_path(n, m)
    for item in res:
        print(item, end='')
    print()
