def compare(regex, char):
    if not regex or regex == ".":
        return True

    if not char:
        return False

    return regex == char


r, c = input().split("|")
print(compare(r, c))
