from django.test import TestCase
from .models import Item


class TestModel(TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpModelsClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownModelsClass")
        print("")  # Add a space for better readability

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_done_field_by_default_is_false(self):
        print("test_done_field_by_default_is_false")
        item = Item.objects.create(name="Test ToDo Item")
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        print("test_item_string_method_returns_name")
        item = Item.objects.create(name="Test ToDo Item")
        self.assertEqual(str(item), "Test ToDo Item")
