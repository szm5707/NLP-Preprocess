filename = "bert_sentences.txt"
fow = open(filename, 'w')
filenames = ['IWSLT14.TED.dev2010.de-en.de.xml', 'IWSLT14.TED.tst2011.de-en.de.xml', 'IWSLT14.TED.tst2012.de-en.en.xml', 'IWSLT14.TED.tst2010.de-en.de.xml', 'IWSLT14.TED.tst2011.de-en.en.xml', 'IWSLT14.TEDX.dev2012.de-en.de.xml', 'IWSLT14.TED.tst2010.de-en.en.xml', 'IWSLT14.TED.tst2012.de-en.de.xml', 'IWSLT14.TEDX.dev2012.de-en.en.xml']

for file in filenames:
    fo = open("dataset/"+file, 'r')
    lines = fo.readlines()
    newlines = []

    for line in lines:
        if line[:8] == "<seg id=":
            sentence = "[CLS] " + line[13:-8] + " [SEP]"
            fow.write(sentence+"\n")
    fo.close()

fow.close()


