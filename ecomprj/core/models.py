from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
class Category(models.Model):
    cat_id=ShortUUIDField(unique=True,length=10,max_length=30,prefix="cat",alphabet="abcdefghijklm")
    title=models.CharField(max_length=100) #Title,Heading
    image=models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural="Categories"
    
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' %(self.image.url))
    
    def __str__(self):
        return self.title


