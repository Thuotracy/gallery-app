from django.test import TestCase
from .models import Image, Location, categories

# Create your tests here.
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.location = Location(name = "Nairobi")
        self.location.save_location()
        self.image = Image(id = 1,title = "test",description = "test description",location = self.location, image_url = "path/to/image")

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_image(self):
        self.image.save_image()
        self.images = Image.objects.all()
        self.assertTrue(len(self.images) > 0)

    def test_get_image_by_id(self):
        self.image.save_image()
        self.image = Image.get_image_by_id(1)
        self.assertTrue(isinstance(self.image,Image))

    def test_update_image(self):
        self.image.save_image()
        self.image = Image.objects.filter(id = 1).update(image_url = "/image")
        self.updated_image = Image.get_image_by_id(1)
        self.assertEqual(self.updated_image.image_url,"/image")

    def test_search_by_category(self):
        self.image.save_image()
        self.category = categories(name = "test")
        self.category.save_category()
        self.image = Image.get_image_by_id(1).categories.add(self.category)
        self.searched_images = Image.search_by_category('test')
        self.assertTrue(len(self.searched_images) > 0)