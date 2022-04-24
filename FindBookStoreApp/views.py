from itertools import count
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

        if list(BooksData.keys())[0] == 'error':
            return HttpResponse('<h1> 検索が一致しませんでした </h1>')

        for con in BooksData['items']:
            print('-----------------------------------')

            try:
                print(con['volumeInfo']['industryIdentifiers'])

                if con['volumeInfo']['industryIdentifiers'] == 'null':
                    isbn = 'null'

                if len(con['volumeInfo']['industryIdentifiers']) == 2:
                    """isbn = {con['volumeInfo']['industryIdentifiers'][0]['type']: con['volumeInfo']['industryIdentifiers'][0]['identifier'],
                            con['volumeInfo']['industryIdentifiers'][1]['type']: con['volumeInfo']['industryIdentifiers'][1]['identifier']}
                    """  
                    # ISBN_13 を取得
                    if con['volumeInfo']['industryIdentifiers'][0]['type'] == "ISBN_13":
                        isbn = int(con['volumeInfo']['industryIdentifiers'][0]['identifier'])
                    else:
                        isbn = int(con['volumeInfo']['industryIdentifiers'][1]['identifier'])
                else:
                    isbn = 'null'

                print('isbn：',isbn)
                     
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
        return render(request, 'index.html', {'books_data':books_data, 'query':title})
    else:
        # https://api.openbd.jp/v1/get?isbn={ISBN}
        return render(request, 'index.html')
    return HttpResponse('output')

"""def storefunc(request):

    keyword_url = 'https://honto.jp/netstore/pd-store_0630360105.html'
    isbn_10 = '4798062219'
    isbn_13 = '9784798062211'

    #keyword_url = "http://ck.jp.ap.valuecommerce.com/servlet/referral?sid=2088108&amp;pid=884062438&amp;vc_url=http%3a%2f%2fhonto.jp%2fisbn%2f" + str(isbn)
    keyword_url = 'https://honto.jp/netstore/pd-store_0630360105.html'



    book_stores = {'kinokuniya': 'https://www.kinokuniya.co.jp/f/dsg-01-' + isbn_13,
                    'amazon': 'https://www.amazon.co.jp/exec/obidos/ASIN/'+ isbn_10 +'/honnoinfo-22/',
                    'yodobasi': 'https://www.yodobashi.com/?word=' + isbn_13
    }

    r = requests.get(keyword_url)
    print(r.text)
    
    soup = BeautifulSoup(r.content, "lxml")

    p = soup.find('script', {'type':'application/ld+json'})
    print (p)
    
    #response = json.dumps(requests.get(keyword_url).json(), indent=2)
    #remindId

    return render(request, 'store.html', {'book_stores':book_stores})"""

def jan_to_asin(jan13):
    s = str(jan13)[3:12]
    a = 10
    c = 0
   
    for i in range(0, len(s)):
        c += int(s[i]) *(a-i)

    d = c % 11
    d = 11 - d 
    if d == 10:
        d = "X"
    return str(s) + str(d)

def storefunc(request, pk):

    # pk = ISBN_13
    
    book_stores = {'kinokuniya_online': 'https://www.kinokuniya.co.jp/f/dsg-01-' + str(pk),
                'amazon': 'https://www.amazon.co.jp/dp/' + str(jan_to_asin(pk)),
                'yodobasi': 'https://www.yodobashi.com/?word=' + str(pk),
                'tutaya' : 'https://shop.tsutaya.co.jp/book/product/' + str(pk) + '/',
    }
    return render(request, 'store.html', {'book_stores':book_stores, 'ISBN':pk})


def kinokuniya_store_func(request, pk):
    keyword_url = 'https://store.kinokuniya.co.jp/store/?type=json'
    response = requests.get(keyword_url)
    response = response.json()
    import pprint
    #pprint.pprint(response['data'])

    kinokuniya_stores = {}
    count = 0

    for i in response['data']:
        print('-------------------------')
        pprint.pprint(i['service_urls'])
        if i['address']['region'] in kinokuniya_stores:
            # 辞書の中に　〜県がある場合
            kinokuniya_stores[i['address']['region']].append({
                "store_id" : i['id'],
                "stock_url" : 'https://www.kinokuniya.co.jp/kinonavi/disp/CKnNvSfGoodsPage.jsp' + i['service_urls'][1]['url'].split('/')[-1] + '&ptk=01&CAT=01&GOODS_STK_NO=' + str(pk),
                "region" : i['address']['region'],
                "store_name" : i['title']
            }) 
        else:
            kinokuniya_stores[i['address']['region']] = [{
                "store_id" : i['id'],
                "stock_url" : 'https://www.kinokuniya.co.jp/kinonavi/disp/CKnNvSfGoodsPage.jsp' + i['service_urls'][1]['url'].split('/')[-1] + '&ptk=01&CAT=01&GOODS_STK_NO=' + str(pk),
                "region" : i['address']['region'],
                "store_name" : i['title']
            }]


        """kinokuniya_stores[count] = {
            'store_id' : i['id'],
            'stock_url' : 'https://www.kinokuniya.co.jp/kinonavi/disp/CKnNvSfGoodsPage.jsp' + i['service_urls'][1]['url'].split('/')[-1] + '&ptk=01&CAT=01&GOODS_STK_NO=' + str(pk),
            'region' : i['address']['region'],
            'store_name' : i['title']
        }"""
        count += 1
        """print('-----------------------------')
        pprint.pprint(i['title'])
        pprint.pprint(i['service_urls'][1]['url'])
        pprint.pprint(i['address']['region'])
        pprint.pprint(i['id'])
        print('-----------------------------')"""

        #pprint.pprint(kinokuniya_stores)
        #print(",".join(list(kinokuniya_stores.keys())))
        print('-------------------------')

    return render(request, 'kinokuniya.html', {'kinokuniya_stores' : kinokuniya_stores })
