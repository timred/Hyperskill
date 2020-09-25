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


def variable(regex, char):
    if match(regex, char):
        return True
    elif len(regex) < len(char):
        return variable(regex, char[1:])
    else:
        return False



r, c = input().split("|")
print(variable(r, c))
