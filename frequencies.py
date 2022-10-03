"""Frequencies function."""

def frequencies(items):
    frequencies = {}
    checked_items = []

    for i in range(len(items)):
        if str(items[i]) not in checked_items:
            checked_items.append(str(items[i]))

    for i in range(len(checked_items)):
        count = 0 #count for each string
        for j in range(len(items)):
            if checked_items[i] == str(items[j]):
                count += 1
        frequencies[checked_items[i]] = count

    print(checked_items)

    return frequencies

print( frequencies([100, 'Hello', '100', '100', 100]) )
