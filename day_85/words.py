# word list came from: https://edu.gcfglobal.org/en/practicereading/word-list-categories/1/

word_list = set()
# Using readline()
with open('word_list.txt', 'r') as word_file:
    for line in word_file:
        for s in line.split():
            word_list.add(s)

# Writing to file
with open("master_list.txt", "w") as fp:
    for word in word_list:
        fp.write(word + '\t')