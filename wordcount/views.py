from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def chicken(request):
    return HttpResponse("100 grams of Chiken breast has 30 grams of protein")

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase the counter
            worddictionary[word] += 1
        
        else:
            #add the word to the dictionary
            worddictionary[word] = 1
            sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':sortedwords})

def about(request):
    return render(request, 'about.html')