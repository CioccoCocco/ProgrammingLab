def countWord(doc, word):
    cnt = 0
    with open(doc, "r") as file:
        content = file.read()
        cnt += content.count(word)
    return cnt

def countAllWords(doc):
    cnt = {}
    with open(doc, "r") as file:
        content = file.read()
        words = content.split()
        for word in words:
            cnt[word] = countWord(doc, word)
    return cnt

def countStartingLetters(doc):
    #TODO: conta frasi che iniziano con ogni determinata lettera
    print("TODO")
    
def cutDuobleLines(doc):
    with open(doc, "r") as file:
        uniqueLines = set(file.readlines())
    
        with open("unique.txt", "w") as uniqueFile:
            uniqueFile.writelines(uniqueLines)