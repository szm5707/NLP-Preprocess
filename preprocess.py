filename = "IWSLT14.TED.dev2010.de-en.en.xml"
fo = open(filename, 'r')
lines = fo.readlines()
newlines = []

for line in lines:
    if line[:8] == "<seg id=":
        newlines.append(line[13:-8])

sentences = ["[CLS] " + query + " [SEP]" for query in newlines]
print(sentences[0])
