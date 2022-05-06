from django.test import TestCase
from django.urls import reverse, resolve
from .views import searchfunc, storefunc, kinokuniya_store_func, searchBook
import unittest



# Create your tests here.


class TestUrls(TestCase):
    def test_post_index_url(self):
        resolve('/')
        resolve('/stores/123456')# 適当な数字
        resolve('/kinokuniya/123456')


    @unittest.skip('Google_books_apiのテスト')
    def check_isbn_api(self):
        self.assertTrue(searchBook('Django'))

    