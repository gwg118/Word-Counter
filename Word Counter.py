from html.parser import HTMLParser
from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = request.urlopen(url)                                          # Connect to web page and use as plain text
    soup = BeautifulSoup(source_code, 'html.parser')                            # Convert to a soup Object.
    for post_text in soup.findAll('a', {'class': 'plp-pod__info'}):      # Grabs all links from page
        content = post_text.string                                              # Remove all HTML
        words = content.lower().split()                                         # entire sentence set to lower case
        for each_word in words:
            print(each_word)
            word_list.append(each_word)


start('https://www.homedepot.com/b/Building-Materials-Insulation-Rigid-Insulation/N-5yc1vZbaxx')
