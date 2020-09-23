def compare(regex, char):
    if not regex or regex == ".":
        return True

    if not char:
        return False

    return regex == char


def match(regex, string):
    if not regex:
        return True

    if not string:
        return False

    if compare(regex[0], string[0]):
        return match(regex[1:], string[1:])
    return False


r, c = input().split("|")
print(match(r, c))
