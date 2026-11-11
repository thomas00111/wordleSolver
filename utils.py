def frequency(words : list) -> dict:
    total : int = 0
    letterFrequency : dict = {}
    for word in words:
        for letter in word:
            if letterFrequency.get(letter) == None:
                letterFrequency[letter] = 0
            letterFrequency[letter] += 1
            total += 1
    for key in letterFrequency.keys():
        letterFrequency[key] = letterFrequency[key]*100/total
    return letterFrequency

def wordFrenquency(word : str, frequencyDict : dict) -> int:
    total = 0
    for letter in word:
        total += frequencyDict.get(letter)
    return total