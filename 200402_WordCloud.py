"""Bildung einer WordCloud."""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open("AmAnfangschufGottHimmelundErde.txt") as f:
    text = f.read()

wordcloud = WordCloud(width=1920, height=1200)

STOPWORDS.add('und')
STOPWORDS.add('der')
STOPWORDS.add('die')
STOPWORDS.add('das')
STOPWORDS.add('da')
STOPWORDS.add('sie')
STOPWORDS.add('er')
STOPWORDS.add('daß')
STOPWORDS.add('den')
STOPWORDS.add('es')
STOPWORDS.add('ein')

wordcloud.generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
