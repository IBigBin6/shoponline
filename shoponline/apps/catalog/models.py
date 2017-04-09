#-*-coding:utf-8-*-
from __future__ import unicode_literals
import django.utils.timezone as timezone
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField("名称",max_length=250,unique=True)
    description=models.TextField("描述")
    created_at=models.DateTimeField("创建时间",auto_now_add=True)
    updated_at=models.DateTimeField("更新时间",auto_now=True)

    def __unicode__(self):
        return self.name

def upload_path_handler(instance,filename):
    filename=instance.name+'.jpg'
    return "{file}".format(file=filename)

class Product(models.Model):
    name=models.CharField("名称",max_length=255,unique=True)
    slug=models.SlugField("Slug",max_length=50,unique=True)
    price=models.DecimalField("价格",max_digits=9,decimal_places=2)
    description=models.TextField("描述")
    quantity=models.IntegerField("数量")
    image=models.ImageField("图片",upload_to=upload_path_handler,max_length=50)
#    categories=models.ManyToManyField(Category)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product',args=(self.slug,))

class Cart(models.Model):
    created_at=models.DateTimeField("时间",auto_now=True)
    products=models.ManyToManyField(Product)
    total=models.DecimalField("总额",max_digits=9,decimal_places=2)




