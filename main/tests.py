from django.test import TestCase, Client
from .models import Item

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

# class ItemTest(TestCase):
#     def check_item(self):
#         item = Item(
#             name='Terra Blade',
#             rarity=5,
#             amount=1,
#             description='Ini terra blade'
#         )

#         self.assertEqual(item.name, 'Terra Blade')
#         self.assertEqual(item.rarity, 5)
#         self.assertEqual(item.amount, 1)
#         self.assertEqual(item.description, 'Ini terra blade')