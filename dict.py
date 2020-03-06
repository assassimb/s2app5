Dict = {'key': 'value'}

with open('test.txt','r') as f:
    for line in f:
        for word in line.split():
            Dict['n'] = word
f.close()


# Creating an empty Dictionary 
#Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  
#i = 1
#Dict = dict(mots = word, frequence = i) 
#print("\nDictionary with the use of dict(): ") 
#print(Dict) 
