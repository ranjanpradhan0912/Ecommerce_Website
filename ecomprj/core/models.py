from django.db import models
from shortuuidfield import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Category(models.Model):
    cid=ShortUUIDField(unique=True,length=10,max_length=30,prefix="cat",alphabet="abcdefghijklm")
    title=models.CharField(max_length=100) #Title,Heading
    image=models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural="Categories"
    
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' %(self.image.url))
    
    def __str__(self):
        return self.title

class Vendor(models.Model):
    vid=ShortUUIDField(unique=True,length=10,max_length=30,prefix="ven",alphabet="abcdefghijklm")
    title=models.CharField(max_length=100) #Title,Heading
    image=models.ImageField(upload_to=user_directory_path)
    description=models.TextField(null=True,blank=True)
    address=models.CharField(max_length=100,default="India") 
    contact=models.CharField(max_length=100,default"1234567890") 
    chat_resp_time=models.CharField(max_length=100,default="100") 
    shipping_on_time=models.CharField(max_length=100,default="100") 
    authentic_rating=models.CharField(max_length=100,default="100") 
    days_return=models.CharField(max_length=100,default="100") 
    warranty_period=models.CharField(max_length=100,default="100") 
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    


