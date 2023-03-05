def twentyTwentithNumber(puzzleInput):
    numFreq = {} # remember you only need to keep last two turn numbers
    for index, item in enumerate(puzzleInput):
        numFreq[item] = index
    while len(puzzleInput) < 2021:
        turn = len(puzzleInput) + 1
        lastNum = puzzleInput[-1]
        if lastNum not in numFreq:
            numFreq[lastNum] = turn
        else:
            puzzleInput.append(numFreq[lastNum][-1] - numFreq[lastNum][-2])
    return puzzleInput[-1]


puzzleInput = [19,20,14,0,9,1]
print(twentyTwentithNumber(puzzleInput))