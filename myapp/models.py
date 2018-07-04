from django.db import models
from django.conf import settings
User=settings.AUTH_USER_MODEL
class Categories(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    image = models.ImageField(upload_to='picture', null=True, blank=True)

    def __str__(self):
        return "Title : "+self.title+",\tPrice : "+str(self.price)

class Checkout(models.Model):
    country_choice=(
        ('In','India'),
        ('Pak','Pakistan'),
        ('Sri','Sri Lanka'),
        ('Ch','China')
    )
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    cname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    country=models.CharField(max_length=50,
                             choices=country_choice,
                             null=True)
    address=models.CharField(max_length=200)
    town=models.CharField(max_length=200)
    zip=models.CharField(max_length=10)
    phone=models.CharField(max_length=11)

    def __str__(self):
        return self.fname

    def __unicode__(self):
        return self.fname

class Cart(models.Model):
    user=models.ForeignKey(User)
    product=models.ForeignKey(Product)
    quantity=models.IntegerField()
    total_price=models.FloatField()

    def __str__(self):
        return self.product.title