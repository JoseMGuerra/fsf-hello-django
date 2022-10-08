from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpViewsClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownViewsClass")
        print("")  # Add a space for better readability

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_get_todo_list(self):
        print("test_get_todo_list")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/todo_list.html")

    def test_get_add_item_page(self):
        print("test_get_add_item_page")
        response = self.client.get("/add")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/add_item.html")

    def test_get_edit_item_page(self):
        print("test_get_edit_item_page")
        item = Item.objects.create(name="Test Todo Item")
        response = self.client.get(f"/edit/{item.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/edit_item.html")

    def test_can_add_item(self):
        print("test_can_add_item")
        response = self.client.post("/add", {"name": "Test Added Item"})
        self.assertRedirects(response, "/")

    def test_can_delete_item(self):
        print("test_can_delete_item")
        item = Item.objects.create(name="Test Todo Item")
        response = self.client.get(f"/delete/{item.id}")
        self.assertRedirects(response, "/")
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        print("test_can_toggle_item")
        item = Item.objects.create(name="Test Todo Item", done=True)
        response = self.client.get(f"/toggle/{item.id}")
        self.assertRedirects(response, "/")
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        print("test_can_edit_item")
        item = Item.objects.create(name="Test Todo Item", done=True)
        response = self.client.post(
                                    f"/edit/{item.id}",
                                    {"name": "Updated name"})
        self.assertRedirects(response, "/")
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, "Updated name")
