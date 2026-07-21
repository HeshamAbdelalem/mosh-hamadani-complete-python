from pprint import pprint

sentence = "This is a common interview question"

sentenceDic = {}

for char in sentence.lower():
    if char in sentenceDic:
        sentenceDic[char] += 1
    else:
        sentenceDic[char] = 1
        
pprint(sentenceDic)


print(sorted(sentenceDic.items(), key=lambda kv:kv[1], reverse=True))