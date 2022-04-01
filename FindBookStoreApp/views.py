from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from bs4 import BeautifulSoup
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

        #print(BooksData['items'])

        """Booksdf = pd.DataFrame({
            'items': BooksData['items'],
            'isbn' : BooksData['industryIdentifiers']
        })

        print(Booksdf)"""

        
        books_data = {}
        id = 0

        for con in BooksData['items']:
            print('-----------------------------------')

            try:
                print(con['volumeInfo']['industryIdentifiers'])

                if len(con['volumeInfo']['industryIdentifiers']) == 2:
                    """isbn = {con['volumeInfo']['industryIdentifiers'][0]['type']: con['volumeInfo']['industryIdentifiers'][0]['identifier'],
                            con['volumeInfo']['industryIdentifiers'][1]['type']: con['volumeInfo']['industryIdentifiers'][1]['identifier']}
                    """  
                    if con['volumeInfo']['industryIdentifiers'][0]['type'] == "ISBN_13":
                        isbn = int(con['volumeInfo']['industryIdentifiers'][0]['identifier'])
                    else:
                        isbn = int(con['volumeInfo']['industryIdentifiers'][1]['identifier'])
                else:
                    isbn = '000'

                print(isbn)
                     
            except:
                print('null')
                isbn = 'null'
            print(con['volumeInfo']['title'])
    
            try:
                print(con['volumeInfo']['imageLinks']['smallThumbnail'])
                img_data = con['volumeInfo']['imageLinks']['smallThumbnail']
            except:
                img_data = "null"
                print("null")

            books_data[id] = {'img_data':img_data, 'title':con['volumeInfo']['title'], 'isbn':isbn}
            id += 1
            print('-----------------------------------\n')

        
        #print(json_str)
        #return HttpResponse(BooksData)
        return render(request, 'index.html', {'books_data':books_data})
    else:
        # https://api.openbd.jp/v1/get?isbn={ISBN}
        return render(request, 'index.html')
    return HttpResponse('output')

def storefunc(request):

    keyword_url = 'https://honto.jp/netstore/pd-store_0630360105.html'
    isbn_10 = '4798062219'
    isbn_13 = '9784798062211'

    #keyword_url = "http://ck.jp.ap.valuecommerce.com/servlet/referral?sid=2088108&amp;pid=884062438&amp;vc_url=http%3a%2f%2fhonto.jp%2fisbn%2f" + str(isbn)
    keyword_url = 'https://honto.jp/netstore/pd-store_0630360105.html'



    book_stores = {'kinokuniya': 'https://www.kinokuniya.co.jp/f/dsg-01-' + isbn_13,
                    'amazon': 'https://www.amazon.co.jp/exec/obidos/ASIN/'+ isbn_10 +'/honnoinfo-22/',
                    'yodobasi': 'https://www.yodobashi.com/?word=' + isbn_13
    }

    """r = requests.get(keyword_url)
    print(r.text)
    
    soup = BeautifulSoup(r.content, "lxml")

    p = soup.find('script', {'type':'application/ld+json'})
    print (p)
    """
    #response = json.dumps(requests.get(keyword_url).json(), indent=2)
    #remindId

    return render(request, 'store.html', {'book_stores':book_stores})


def storesfinc(request, pk):

    
    book_stores = {'kinokuniya': 'https://www.kinokuniya.co.jp/f/dsg-01-' + str(pk),
                'amazon': 'https://www.amazon.co.jp/exec/obidos/ASIN/'+ str(pk) +'/honnoinfo-22/',
                'yodobasi': 'https://www.yodobashi.com/?word=' + str(pk)
    }
    return render(request, 'store.html', {'book_stores':book_stores})