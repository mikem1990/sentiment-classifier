# remove punctuation
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    for i in s:
        if i in punctuation_chars:
            s = s.replace(i, "")
    return s

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# count positive words
def get_pos(s):
    total_pos = 0
    s = strip_punctuation(s)
    s = s.lower()
    s = s.split()

    for i in s:
        if i in positive_words:
            total_pos += 1
    return total_pos

# list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# count negative words           
def get_neg(s):
    total_neg = 0
    s = strip_punctuation(s)
    s = s.lower()
    s = s.split()
    
    for i in s:
        if i in negative_words:
            total_neg += 1
    return total_neg

# open data
fileref = open("project_twitter_data.csv", "r")
data = fileref.readlines()

# create csv with headers
outfile = open("resulting_data.csv","w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write("\n")

# process and format data
for i in data[1:]:
    res_row = ""
    splt = i.strip().split(",")           
    res_row = ("{},{},{},{},{}".format(splt[1], splt[2], get_pos(splt[0]), get_neg(splt[0]), (get_pos(splt[0])-get_neg(splt[0]))))
    outfile.write(res_row)
    outfile.write("\n")

outfile.close()