from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from words.models import Words
from django.contrib.auth.models import User
from words.views import (
    WordListView,
    WordDetailView,
    WordCreateView,
    WordUpdateView,
    WordDeleteView,
    PlayerWordListView
)


class TestUrls(SimpleTestCase):
    def test_url_is_resolved(self):

        url_index = reverse('words-index')
        self.assertEquals(url_index, '/')

        url_list = reverse('player-words', args = ['somename'])
        self.assertEquals(resolve(url_list).func.view_class, PlayerWordListView)

        url_detail = reverse('words-detail', args = [1])
        self.assertEquals(resolve(url_detail).func.view_class, WordDetailView)

        url_update = reverse('words-update', args = [2])
        self.assertEquals(resolve(url_update).func.view_class, WordUpdateView)

        url_delete = reverse('words-delete', args = [2])
        self.assertEquals(resolve(url_delete).func.view_class, WordDeleteView)

        url_create = reverse('words-create')
        self.assertEquals(url_create, '/word/new/')

        url_update = reverse('words-about')
        self.assertEquals(url_update, '/about/')

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        # user = User.objects.create(username='RediTest',
        #                          email='RediTest@gmail.com',
        #                          password='glassonion123')
        #
        # print(user)
        # user.save(self)
        # self.word = Words.objects.create(
        #     noun = 'cat',
        #     define = 'domestic animal',
        #     player = user
        # )
        # users = User.objects.all()
        # print("users", users)


    def test_words_model(self):
        # url_detail = reverse('words-detail', args = [1])
        # print(url_detail)

        response = self.client.get(reverse('words-index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'words/index.html', 'words/base.html')

        response = self.client.get(reverse('words-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'words/about.html', 'words/base.html')

        response = self.client.get(reverse('words-create'))
        self.assertEquals(response.status_code, 302)

        response = self.client.get(reverse('words-update', args = [1]))
        self.assertEquals(response.status_code, 302)

        response = self.client.get(reverse('words-delete', args = [1]))
        self.assertEquals(response.status_code, 302)

        # response = self.client.get(reverse('player-words', args = ['somename']))
        # print("response", response)
        # self.assertEquals(response.status_code, 302)

        # response = client.get(reverse('words-detail', args = [1]))
        # print("response", response)
        # self.assertEquals(response.status_code, 200)
        # self.assertTemplateUsed(response, 'words_detail.html', 'words/base.html')
