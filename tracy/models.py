from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

class categories(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name


class Image(models.Model):
    description = models.TextField()
    locations = models.TextField()
    title = models.CharField(max_length=30,default="title")
    categories = models.ManyToManyField(categories)
    image = CloudinaryField('image')
    


    def __str__(self):
        return self.title

    def save_image(self):
        self.save()
    
    def delete_image():
        self.delete()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(categories__name__contains = search_term)
        return images

    @classmethod
    def get_image_by_id(cls,id):
        Image = cls.objects.get(id = id)
        return Image
    @classmethod
    def filter_by_location(cls,search_term):
        location = Location.objects.get(name = search_term)
        images = cls.objects.filter(location = location)
        return images