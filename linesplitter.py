def linesplitter(filename): 
    with open(filename) as f:
        content = f.read()
        line_list = content.split("\n")
        for line in line_list:
            if "" in line_list:
                line_list.remove("")
            else:
                break
 
    f2= open(filename.replace(".txt",".tsv"),"w+")
    headline="ID\tTEXT\tLABEL"
    f2.write(headline+"\n")
    counter = 0
    for s in line_list:
        counter += 1
        sentence_id=filename.replace(".txt","")+"-"+str(counter)
        sentence=sentence_id+"\t"+s+"\t"
        print(sentence)
        f2.write(sentence + "\n")
    f2.close()