from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

# Create your views here.

def searchBook(keyword):
    params = {'Country': "JP", 'maxResults': 30}
    keyword_url = 'https://www.googleapis.com/books/v1/volumes?q=' + keyword
    response = requests.get(keyword_url, params=params).json()
    return response

def searchfunc(request):
    if request.method == 'POST':
        title = request.POST['title']
        BooksData = searchBook(title)
        
        books_data = {}
        id = 0

        if list(BooksData.keys())[0] == 'error':
            return redirect('search')

        for con in BooksData['items']:
            print('-----------------------------------')

            try:
                print(con['volumeInfo']['industryIdentifiers'])

                if con['volumeInfo']['industryIdentifiers'] == 'null':
                    isbn = 'null'

                if len(con['volumeInfo']['industryIdentifiers']) == 2:
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

        return render(request, 'index.html', {'books_data':books_data, 'query':title})
    else:
        # https://api.openbd.jp/v1/get?isbn={ISBN}
        return render(request, 'index.html')

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
    
    book_stores_online = {'紀伊国屋 オンライン書店': {'URL':'https://www.kinokuniya.co.jp/f/dsg-01-' + str(pk), 'IMG':'images/kinokuniya.jpg'},
                'Amazon': {'URL':'https://www.amazon.co.jp/dp/' + str(jan_to_asin(pk)), 'IMG':'images/amazon.jpg'},
                'ヨドバシカメラ': {'URL':'https://www.yodobashi.com/?word=' + str(pk), 'IMG':'images/yodobashi.jpg'},
                'TSUTAYA' : {'URL':'https://shop.tsutaya.co.jp/book/product/' + str(pk) + '/', 'IMG':'images/tsutaya.jpg'},
    }


    book_stores = {
        '紀伊国屋': {'ISBN': pk, 'TAGNAME':'kinokuniya', 'IMG':'images/kinokuniya.jpg'},
    }

    return render(request, 'store.html', {'book_stores_online':book_stores_online, 'book_stores':book_stores})


def kinokuniya_store_func(request, pk):
    keyword_url = 'https://store.kinokuniya.co.jp/store/?type=json'
    response = requests.get(keyword_url)
    response = response.json()
    import pprint
    #pprint.pprint(response['data'])

    kinokuniya_stores = {}
    count = 0

    for i in response['data']:
        #print('-------------------------')
        #pprint.pprint(i['service_urls'])
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
        count += 1
        #print('-------------------------')

    return render(request, 'kinokuniya.html', {'kinokuniya_stores' : kinokuniya_stores })
