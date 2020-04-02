from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from .models import Movie


class MovieUserTestCase(TestCase):
    def setUp(self):
        self.passsword = ''

        self.test_user = get_user_model().objects.create_user(
            email='',
            password=self.passsword)

        self.client.login(email=self.test_user.email, password=self.passsword)

class TestMovieCreateView(MovieUserTestCase):

    def test_create_movie_success(self):
        params = {'title': 'テストタイトル',
                  'setsumei': 'テスト説明',
                  'samune': 'サムネ',
                  'upload': '', }
        response = self.client.post(reverse_lazy('movie_site: movie_upload'),params)
        self.assertRedirects(response, reverse_lazy('movie_site:movie_top'))
        self.assertEqual(Movie.objects.filter(title='タイトルテスト').count(), 1)

    def test_create_movie_failure(self):
        response = self.client.post(reverse_lazy('movie_site:movie_upload'))
        self.assertFormError(response, 'form', 'タイトル', 'このフィールドは必須です。')


class TestMovieUpdateView(MovieUserTestCase):
    def test_update_movie_success(self):
        movie = Movie.objects.create(user=self.test_user, title='タイトル編集前')
        params = {'title': 'タイトル編集前'}
        response = self.client.post(reverse_lazy('movie_site:movie_update', kwargs={'pk': movie.pk}), params)
        self.assertRedirects(response, reverse_lazy('movie_site:movie_detail', kwargs={'pk': movie.pk}))
        self.assertEqual(Movie.objects.get(pk=movie.pk).title, 'タイトル編集後')

    def test_update_movie_failure(self):
        response = self.client.post(reverse_lazy('movie_site:movie_update', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)


class TestMovieDeleteView(MovieUserTestCase):
    def test_delete_movie_success(self):
        movie = Movie.objects.create(user=self.test_user, title='タイトル')
        response = self.client.post(reverse_lazy('movie_site:movie_delete', kwargs={'pk': movie.pk}))
        self.assertRedirects(response, reverse_lazy('movie_site:movie_top'))
        self.assertEqual(Movie.objects.filter(pk=movie.pk).count(), 0)

    def test_delete_movie_failure(self):
        response = self.client.post(reverse_lazy('movie_site:movie_delete', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)
