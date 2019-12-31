from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_image = models.FileField()

    def __str__(self):
        return self.category_name

class Food(models.Model):
    food_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    food_name = models.CharField(max_length=200)
    available = models.IntegerField(default=1)
    food_image = models.FileField()
    price = models.IntegerField()

    def __str__(self):
        return self.food_name

class Order(models.Model):
    name = models.CharField(max_length=50)
    table_no = models.CharField(max_length=10)
    food = models.ManyToManyField(Food,related_name="orderd_food")
    amount = models.IntegerField()

    def __str__(self):
        return self.name


