from django.test import TestCase
from main.models import Merch, Releases, TicketsShop
# Create your tests here.

class TicketsShopModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        TicketsShop.objects.create(date='2023-08-07', city='Екатерингбург', club='Пять бакланов', street='Жировиха, 5')

    def test_date_label(self):
        ticket = TicketsShop.objects.get(id=1)
        field_label = ticket._meta.get_field('date')
        field_value = field_label.value_from_object(ticket)
        self.assertEquals(str(field_value), '2023-08-07')

    def test_city_label_max_length(self):
        ticket = TicketsShop.objects.get(id=1)
        max_length = ticket._meta.get_field('city').max_length
        self.assertEquals(max_length, 256)

    def test_club_label_max_length(self):
        ticket = TicketsShop.objects.get(id=1)
        max_length = ticket._meta.get_field('club').max_length
        self.assertEquals(max_length, 256)
    def test_street_label_max_length(self):
        ticket = TicketsShop.objects.get(id=1)
        max_length = ticket._meta.get_field('street').max_length
        self.assertEquals(max_length, 256)

class ReleasesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Releases.objects.create(name='Gnoj', image='releases/LZltnFM-vnU.jpg', apple_music=None, spotify='https://www.spotify.com/int/why-not-available/',
                                vkontakte='https://vk.com/', youtube='https://www.youtube.com/',
                                youtube_music='https://music.youtube.com/', release_description='Новый альбом уже вышел!')

    def test_name_label_max_length(self):
        release = Releases.objects.get(id=1)
        max_length = release._meta.get_field('name').max_length
        self.assertEquals(max_length, 256)
    def test_image_label(self):
        release = Releases.objects.get(id=1)
        release_url = release._meta.get_field('image')
        release_value = release_url.value_from_object(release)
        self.assertEquals(release_value, 'releases/LZltnFM-vnU.jpg')
    def test_apple_music_none(self):
        release = Releases.objects.get(id=1)
        field_label = release._meta.get_field('apple_music')
        field_value = field_label.value_from_object(release)
        self.assertIsNone(field_value, None)

    def test_sporify_url(self):
        release = Releases.objects.get(id=1)
        field_label = release._meta.get_field('spotify')
        field_value = field_label.value_from_object(release)
        self.assertEquals(field_value, 'https://www.spotify.com/int/why-not-available/')

    def test_vkontakte_url(self):
        release = Releases.objects.get(id=1)
        field_label = release._meta.get_field('vkontakte')
        field_value = field_label.value_from_object(release)
        self.assertEquals(field_value, 'https://vk.com/')
    def test_youtube_url(self):
        release = Releases.objects.get(id=1)
        field_label = release._meta.get_field('youtube')
        field_value = field_label.value_from_object(release)
        self.assertEquals(field_value, 'https://www.youtube.com/')
    def test_youtube_music_url(self):
        release = Releases.objects.get(id=1)
        field_label = release._meta.get_field('youtube_music')
        field_value = field_label.value_from_object(release)
        self.assertEquals(field_value, 'https://music.youtube.com/')
    def test_release_description(self):
        release = Releases.objects.get(id=1)
        field_label = release._meta.get_field('release_description')
        field_value = field_label.value_from_object(release)
        self.assertEquals(field_value, 'Новый альбом уже вышел!')
class MerchModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Merch.objects.create(name='Футболка', image='images/ITkQUlYzSBU.jpg', description=None,
                             price=3200, composition='Хлопок', size='m', color=None)

    def test_name_label_max_length(self):
        merch = Merch.objects.get(id=1)
        max_length = merch._meta.get_field('name').max_length
        self.assertEquals(max_length, 256)

    def test_image_label(self):
        merch = Merch.objects.get(id=1)
        merch_url = merch._meta.get_field('image')
        merch_value = merch_url.value_from_object(merch)
        self.assertEquals(merch_value, 'images/ITkQUlYzSBU.jpg')

    def test_description_none(self):
        merch = Merch.objects.get(id=1)
        field_label = merch._meta.get_field('description')
        field_value = field_label.value_from_object(merch)
        self.assertIsNone(field_value, None)

    def test_price_max_digits(self):
        merch = Merch.objects.get(id=1)
        max_digits = merch._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 10)

    def test_composition(self):
        merch = Merch.objects.get(id=1)
        field_label = merch._meta.get_field('composition')
        field_value = field_label.value_from_object(merch)
        self.assertEquals(field_value, 'Хлопок')

    def test_size_max_length(self):
        merch = Merch.objects.get(id=1)
        max_length = merch._meta.get_field('size').max_length
        self.assertEquals(max_length, 128)

    def test_color_max_length(self):
        merch = Merch.objects.get(id=1)
        max_length = merch._meta.get_field('color').max_length
        self.assertEquals(max_length, 128)

    def test_size_label(self):
        merch = Merch.objects.get(id=1)
        field_label = merch._meta.get_field('size')
        field_value = field_label.value_from_object(merch)
        self.assertEquals(field_value, 'm')

    def test_color_none(self):
        merch = Merch.objects.get(id=1)
        field_label = merch._meta.get_field('color')
        field_value = field_label.value_from_object(merch)
        self.assertIsNone(field_value, None)


































