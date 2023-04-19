from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .forms import WordForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def search(request):
    word = request.GET['word']
    source_meaning = requests.get('https://www.dictionary.com/browse/'+word)
    source_synonym_antonym = requests.get('https://www.thesaurus.com/browse/'+word)
    meaning = []
    synonym_list = []
    antonym_list = []
    if source_meaning:
        # meaning = []
        # synonym_list = []
        # antonym_list = []
        soup = BeautifulSoup(source_meaning.text, 'html.parser')
        if soup:
            meaning1 = soup.find_all('div', {'value': '1'})
            if meaning1:
                meaning1 = meaning1[0].get_text(strip=True).split(':')[0]
                meaning.append(meaning1)


                meaning2 = soup.find_all('div', {'value': '2'})
                if meaning2:
                    meaning2 = meaning2[0].get_text(strip=True).split(':')[0]
                    meaning.append(meaning2)


                meaning3 = soup.find_all('div', {'value': '3'})
                if meaning3:
                    meaning3 = meaning3[0].get_text(strip=True).split(':')[0]
                    meaning.append(meaning3)


                meaning4 = soup.find_all('div', {'value': '4'})
                if meaning4:
                    meaning4 = meaning4[0].get_text(strip=True).split(':')[0]
                    meaning.append(meaning4)
                    
                synonym_list = []
                antonym_list = []
                if source_synonym_antonym:
                    soup2 = BeautifulSoup(source_synonym_antonym.text, 'html.parser')

                    # synonym_list = []
                    synonyms = soup2.find_all('a', {'class': 'css-1kg1yv8 eh475bn0'})

                    if synonyms:
                        for i in synonyms:
                            synonym_list.append(i.text)
                    else:
                        synonym_list.append("-1")
        
                    # antonym_list = []
                    antonyms = soup2.find_all('a', {'class': 'css-15bafsg eh475bn0'})

                    if antonyms:
                        for i in antonyms:
                            antonym_list.append(i.text)
                    else:
                        antonym_list.append("-1")
                else:
                    synonym_list.append("-1")
            antonym_list.append("-1")

        else:
            synonym_list.append("-1")
            antonym_list.append("-1")
        
    else:
        # word = 'Sorry, ' + word + ' Is Not Found In Our Database'
        meaning.append("-1")
        
    
    context = {"synonym_list": synonym_list,
               "antonym_list": antonym_list,
               'word': word,
               "meaning": meaning}
    return render(request, "search.html", context)
