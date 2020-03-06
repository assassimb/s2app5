Dict = {}
i = 0

with open('test.txt','r') as f:
    for line in f:
        for word in line.split():
            Dict[i] = word
            i = i + 1
f.close()

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

print("Dictionnaire : ") 
print(Dict) 
#print(Dict[1])
#print(Dict.keys())


fp = open('test.txt')
data = fp.read()
words = data.split()
fp.close()

unwanted_chars = ".,-_ (and so on)"
wordfreq = {}
for raw_word in words:
    word = raw_word.strip(unwanted_chars)
    if word not in wordfreq:
        wordfreq[word] = 0 
    wordfreq[word] += 1

print(wordfreq)
