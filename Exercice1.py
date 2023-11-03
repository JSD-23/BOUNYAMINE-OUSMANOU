def lengthOfLastWord(s):
    mots = s.split()
    if len(mots) > 0:
        dernier_mot = mots[-1]
        return len(dernier_mot)
    else:
        return 0