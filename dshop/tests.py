from django.test import TestCase
from dshop.models import Product, Category


# Test Models
class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            name='smartfony',
            # parent='',
            slug='smartfony'
        )

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        # Тест на соответсвие ожидаемой ссылки
        self.assertEquals(category.get_absolute_url(), '/dshop/smartfony/')


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            category=Category.objects.create(
                name='smartfony',
                # parent='',
                slug='smartfony'
            ),
            name='LG',
            slug='lg',
            # image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
            description='Описание',
            price=100,
            stock=10,
            available=True,
            created='20.12.2019',
            updated='19.01.2020')

    def test_get_absolute_url(self):
        product = Product.objects.get(id=1)
        # Тест на соответсвие ожидаемой ссылки
        self.assertEquals(product.get_absolute_url(), '/dshop/product/lg/')

