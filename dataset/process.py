filepath = 'train.tags.de-en.en'

newfilepath = 'train_en'
fp_write = open(newfilepath, 'w')
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
    #    print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       print(line[0])
       if line[0] != '<':
           fp_write.write("[CLS] " + line[:-1].lower() + " [SEP]\n")
       cnt += 1
