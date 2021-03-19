def get_input():
    lines = []
    while True:
        line = input()

        if line:
            lines.append(line)
        else:
            break

    return lines


def app():
    print('Task - Pokemon types')
    lines = get_input()

    print(lines)
