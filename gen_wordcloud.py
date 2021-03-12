import os
import sys
from wordcloud import WordCloud

if len(sys.argv) != 2:
    print("usage: python pq_gen_wordcloud.py TEXTFILE")
    exit(0)

whole_text = None
#with open("copy-total-words", "r") as i_f:
with open(sys.argv[1], "r") as i_f:
    whole_text = i_f.read()

whole_text = whole_text.replace("cid:", "")

#wordcloud = WordCloud().generate(whole_text)

import matplotlib.pyplot as plt
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")

wordcloud = WordCloud(background_color="white",
                    colormap="winter",
                    font_path="Source_Sans_Pro/SourceSansPro-Bold.ttf",
                    height=800,
                    width=800,
                    min_font_size=10,
                    max_font_size=120,
                    prefer_horizontal=3.0).generate(whole_text)

plt.figure(figsize=(10.0, 10.0))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("wordcloud-final.png")

# Now let's do word frequency
word_dict = dict()
split_words = whole_text.split(" ")
total_number_of_words = len(split_words)
print(total_number_of_words)
total_sorted = 0
for w in split_words:
    total_sorted += 1
    if w in word_dict:
        word_dict[w] = word_dict[w] + 1
    else:
        word_dict[w] = 1
print("Total sorted: %d"%(total_sorted))

listed_word_dict = []
for key,value in word_dict.items():
    listed_word_dict.append((key, value, ))

print("Length of listed word %d"%(len(listed_word_dict)))
listed_word_dict.sort(key=lambda x:x[1])
listed_word_dict.reverse()
sorted_list = listed_word_dict
print(sorted_list)


# https://www.espressoenglish.net/the-100-most-common-words-in-english/
avoid_words = { "the", "at", "there", "some", "my", "of", "be", "use", "her", "than", "and", "this", "an", "would", "first", "a", "have", "each", "make", "water", "to", "from", "which", "like", "been", "in", "or", "she", "him", "call", "is", "one", "do", "into", "who", "you", "had", "how", "time", "oil", "that", "by", "their", "has", "its", "it", "word", "if", "look", "now", "he", "but", "will", "two", "find", "was", "not", "up", "more", "long", "for", "what", "other", "write", "down", "on", "all", "about", "go", "day", "are", "were", "out", "see", "did", "as", "we", "many", "number", "get", "with", "when", "then", "no", "come", "his", "your", "them", "way", "made", "they", "can", "these", "could", "may", "I", "said", "so", "people", "part" }

avoid_words.add("=")
avoid_words.add(".")
avoid_words.add(" ")
avoid_words.add("")
avoid_words.add(",")

words = []
freqs = []
for key, value in sorted_list:
    if key.lower() in avoid_words:
        continue
    words.append(key)
    freqs.append(value)
for i in range(140):
    print("sorted_list: %s"%(str(sorted_list[i])))

Data = { "words: " : words, "freqs" : freqs }

plt.clf()
plt.figure(figsize=(10.0, 10.0))
plt.barh(words[:50], freqs[:50])

plt.title("Word frequency")
#plt.show()
plt.savefig("barplot.png")
