from django.test import TestCase
from django.urls import reverse, resolve
from .views import searchfunc, searchBook
import unittest



# Create your tests here.


class TestUrls(TestCase):
    def test_index_url(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, searchfunc)
        print('OK>>searchfunc')
    
    def test_stores_view(self):
        response = self.client.get(reverse('stores', kwargs={"pk": 12345}))
        self.assertEqual(response.status_code , 200)
        print('OK>>stores_view')

    def test_kinokuniya_view(self):
        response = self.client.get(reverse('kinokuniya', kwargs={"pk": 12345}))
        self.assertEqual(response.status_code , 200)
        print('OK>>kinokuniya_view')

    def test_isbn_api(self):
        data = searchBook('Django')
        if len(data)>=1:
            print('OK>>test_isbn_api')