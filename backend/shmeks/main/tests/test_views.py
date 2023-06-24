from django.test import TestCase

from main.models import *
from django.urls import reverse
from main.cart import Cart
class ReleasesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_releases = 2
        for release_num in range(number_of_releases):
            Releases.objects.create(name='Gnoj %s' % release_num, image='releases/LZltnFM-vnU.jpg', apple_music=None,
                                    spotify='https://www.spotify.com/int/why-not-available/',
                                    vkontakte='https://vk.com/', youtube='https://www.youtube.com/',
                                    youtube_music='https://music.youtube.com/',
                                    release_description='Новый альбом уже вышел!')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/releases/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('releases'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('releases'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main/releases.html')

class ReleasesDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
            cls.release = Releases.objects.create(name='Gnoj', image='releases/LZltnFM-vnU.jpg', apple_music=None,
                                    spotify='https://www.spotify.com/int/why-not-available/',
                                    vkontakte='https://vk.com/', youtube='https://www.youtube.com/',
                                    youtube_music='https://music.youtube.com/',
                                    release_description='Новый альбом уже вышел!')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/releases/%s/' % self.release.pk)
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('releases_detail', kwargs={'pk':self.release.pk,}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('releases_detail', kwargs={'pk':self.release.pk,}))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main/release_page.html')

class ShopViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_merch = 2
        for merch_num in range(number_of_merch):
            Merch.objects.create(name='Футболка %s' % merch_num, image='images/ITkQUlYzSBU.jpg', description=None,
                                 price=3200, composition='Хлопок', size='m', color=None)
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/shop/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('shop'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('shop'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main/shop.html')


class ShopDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.merch = Merch.objects.create(name='Футболка', image='images/ITkQUlYzSBU.jpg', description=None,
                                 price=3200, composition='Хлопок', size='m', color=None)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/shop/%s/' % self.merch.pk)
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('shop_detail', kwargs={'pk':self.merch.pk,}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('shop_detail', kwargs={'pk':self.merch.pk,}))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main/shop_page.html')

class TicketsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_tickets = 3
        for ticket_num in range(number_of_tickets):
            TicketsShop.objects.create(date='2023-08-07', city='Екатерингбург %s' % ticket_num, club='Пять бакланов', street='Жировиха, 5')
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/tickets/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('tickets'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('tickets'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main/tickets.html')




class IndexViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main/index.html')

class AboutsUsViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/about_us/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('about_us'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('about_us'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main/about_us.html')


class EntryViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/entry/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('entry'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('entry'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main/entry.html')

class LoginViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/login/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main/login.html')

class CartViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/cart/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cart_detail'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('cart_detail'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'main/cart_detail.html')



























