from django.test import TestCase
from .forms import ItemForm


# Create your tests here.

class TestItemForm(TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpFormsClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownFormsClass")
        print("")  # Add a space for better readability

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_item_name_is_required(self):
        print("test_item_name_is_required")
        form = ItemForm({"name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors.keys())
        self.assertEqual(form.errors["name"][0], "This field is required.")

    def test_done_field_is_not_required(self):
        print("test_done_field_is_not_required")
        form = ItemForm({"name": "This is a test item"})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_meta_class(self):
        print("test_fields_are_explicit_in_form_meta_class")
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ["name", "done"])
