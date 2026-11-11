import utils

def solver(greens : list, oranges : list, reds : list, words : list, frequencyDict : dict, used : list) -> str:
    possible : list = []
    for word in words:
        if word not in used:
            ok : bool = True
            for i in range(5):
                if greens[i] != "" and greens[i] != word[i]:
                    ok = False
                    break
            for i, orange in enumerate(oranges):
                for letter in orange:
                    if letter == word[i] or letter not in word:
                        ok = False
                        break
            for letter in reds:
                ino : int = 0
                for o in oranges:
                    if letter in o:
                        ino += 1
                if ino == 0 and letter not in greens:
                    if letter in word:
                        ok = False
                        break
                else:
                    if word.count(letter) > ino + greens.count(letter):
                        ok = False
                        break
            if ok:
                possible.append(word)
    best : tuple = (None, 0)
    for w in possible:
        value : int = utils.wordFrenquency(w, frequencyDict)
        if value > best[1]:
            best = (w, value)
    return best[0]

if __name__ == "__main__":
    green = '\033[92m'
    normal = '\033[0m'
    print(f"{green}")
    print("""                                                 
                     _ _     _____     _             
     _ _ _ ___ ___ _| | |___|   __|___| |_ _ ___ ___ 
    | | | | . |  _| . | | -_|__   | . | | | | -_|  _|
    |_____|___|_| |___|_|___|_____|___|_|\_/|___|_|  
    """)
    print(f"{normal}")

    words : list = open("wordList.txt", "r").read().split("\n")
    frequencyDict : dict = utils.frequency(words)
    greens : list = ["", "", "", "", ""]
    oranges : list = [[], [], [], [], []]
    reds : list = []
    used : list = []

    while True:
        word : str = solver(greens, oranges, reds, words, frequencyDict, used)
        print(word)
        used.append(word)
        answer : str = input(">")
        if answer == "ggggg" or answer == "bye":
            break

        for i in range(5):
            if answer[i] == "g":
                greens[i] = word[i]
            elif answer[i] == "o":
                oranges[i].append(word[i])
            elif answer[i] == "r":
                reds.append(word[i])