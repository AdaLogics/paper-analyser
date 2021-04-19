import yake
import matplotlib.pyplot as plt
from pymongo import MongoClient
from wordcloud import WordCloud

from base import Article


def find_keywords(articles, top_n=80, ngram_size=1):
    text = " ".join([a.text.lower() for a in articles])

    return yake.KeywordExtractor(top=top_n, n=ngram_size).extract_keywords(text)

def wordcloud(articles, dst=None):
    # Get keywords.
    keywords, importance = zip(*find_keywords(articles))
    # Reverse importance.
    importance = map(lambda x: 1-x, importance)
    keywords = dict(zip(keywords, importance))

    wordcloud = WordCloud(background_color="white",
                    colormap="winter",
                    #font_path="Source_Sans_Pro/SourceSansPro-Bold.ttf",
                    height=800,
                    width=800,
                    min_font_size=10,
                    max_font_size=120,
                    prefer_horizontal=3.0).generate_from_frequencies(keywords)

    plt.figure(figsize=(10.0, 10.0))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    if dst:
        plt.savefig(dst)
    

if __name__ == "__main__":
    client = MongoClient("localhost", 27017) 
    db = client.alexandria
    articles = list(map(Article.from_dict, db.articles.find()))

    print(f"Fetched {len(articles)} articles.")

    keywords, _ = zip(*find_keywords(articles, top_n=5, ngram_size=2))
    print(f"Top 5 keywords: {keywords}")

    wordcloud(articles, "examples/wordcloud-final.png")
