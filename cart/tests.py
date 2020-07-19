from dataclasses import dataclass
from decimal import Decimal
from django.conf import settings
from django.test import TestCase
from cart.cart import Cart
from dshop.models import Category, Product


@dataclass
class MockedSession(dict):
    modified = False


@dataclass
class MockedRequest:
    session = MockedSession()


class CartTest(TestCase):
    def setUp(self):
        self.category = Category(name="smartphones", slug="smart")
        self.category.save()
        self.test_product1 = Product(
            category=self.category, name="Xperia", stock=12, price=1000
        )
        self.test_product2 = Product(
            category=self.category, name="Iphone", stock=12, price=50000
        )
        self.test_product1.save()
        self.test_product2.save()
        self.cart = Cart(MockedRequest())

    def test_add(self):
        self.cart.add(self.test_product1, 1, update_quantity=True)
        self.assertEquals(len(self.cart.cart), 1)
        self.assertTrue(str(self.test_product1.id) in self.cart.cart)
        product = self.cart.cart[str(self.test_product1.id)]
        self.assertEquals(product["quantity"], 1)
        self.assertEquals(product["price"], str(self.test_product1.price))

    def test_update(self):
        self.cart.add(self.test_product1, 1, update_quantity=True)
        self.assertTrue(str(self.test_product1.id) in self.cart.cart)
        self.cart.add(self.test_product1, 1)
        product = self.cart.cart[str(self.test_product1.id)]
        self.assertEquals(product["quantity"], 2)

    def test_save(self):
        self.cart.save()
        self.assertTrue(self.cart.session.modified)
        self.assertTrue(settings.CART_SESSION_ID in self.cart.session)

    def test_remove(self):
        self.cart.add(self.test_product1, 1, update_quantity=True)
        self.cart.add(self.test_product2, 1, update_quantity=True)
        self.cart.remove(self.test_product1)
        self.assertEquals(len(self.cart.cart), 1)
        self.assertTrue(str(self.test_product2.id) in self.cart.cart)
        product = self.cart.cart[str(self.test_product2.id)]
        self.assertEquals(product["quantity"], 1)
        self.assertEquals(product["price"], str(self.test_product2.price))

    # работа итератора __iter__ я так понимаю провериться в тесте def test_get_total_price(self):

    def test_get_total_price(self):
        self.cart.add(self.test_product1, 1, update_quantity=True)
        self.cart.add(self.test_product2, 1, update_quantity=True)
        test_sum_price = self.test_product1.price + self.test_product2.price
        total = sum(Decimal(item['price']) * item['quantity'] for item in self.cart.cart.values())
        self.assertEquals(total, test_sum_price)

    def test_clear(self):
        del self.cart.session
        self.assertTrue(settings.CART_SESSION_ID not in self.cart)
