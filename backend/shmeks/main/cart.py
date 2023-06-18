from decimal import Decimal
from django.conf import settings
from .models import Merch

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, merch):
        merch_id = str(merch.id)
        if merch_id not in self.cart:
            self.cart[merch_id] = {'price': str(merch.price)}
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, merch):
        merch_id = str(merch.id)
        if merch_id in self.cart:
            del self.cart[merch_id]
            self.save()

    def __iter__(self):
        merch_ids = self.cart.keys()
        merch_all = Merch.objects.filter(id__in=merch_ids)
        for merch in merch_all:
            self.cart[str(merch.id)]['merch'] = merch

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            yield item

    def __len__(self):
        return sum(len(item) for item in self.cart.values())

    def get_total_price(self):
        return sum(item['price'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True













