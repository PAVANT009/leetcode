def canConstruct(ransomNote, magazine):
    # mag -> ra
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    seen = {}

    for x in magazine:
        if x in seen:
            seen[x] += 1
            continue
        seen[x] = 1
    for y in ransomNote:
        if y in seen and seen[y] > 0:
            seen[y] -= 1
        else:
            return False


canConstruct(ransomNote="a", magazine="b")
