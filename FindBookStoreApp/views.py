from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import pandas as pd

# Create your views here.

def searchBook(keyword):
    keyword_url = 'https://www.googleapis.com/books/v1/volumes?q=' + keyword
    response = requests.get(keyword_url).json()
    return response

def searchfunc(request):
    if request.method == 'POST':
        title = request.POST['title']
        BooksData = searchBook(title)

        print(BooksData['items'])

        """Booksdf = pd.DataFrame({
            'items': BooksData['items'],
            'isbn' : BooksData['industryIdentifiers']
        })

        print(Booksdf)"""

        
        for con in BooksData['items']:
            print('-----------------------------------')
            print(con['volumeInfo']['title'])
            print(con['volumeInfo']['industryIdentifiers'])
            
            print('-----------------------------------\n')

        
        #print(json_str)
        return HttpResponse(BooksData)
    else:
        # https://api.openbd.jp/v1/get?isbn={ISBN}
        return render(request, 'index.html')
    return HttpResponse('output')