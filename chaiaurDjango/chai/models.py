from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class chaiVarity(models.Model):
    CHHAI_TYPE_CHOICE=[
        ('C', 'Chai'),
        ('T', 'Tea'),
        ('G', 'Green Tea'),
        ('O', 'Oolong Tea'),
        ('B', 'Black Tea'),
        ('P', 'Pu-erh Tea'),
        ('S', 'Sencha'),
        ('J', 'Jasmine'),
        ('L', 'Lemongrass'),
        ('M', 'Matcha'),
        ('R', 'Rooibos'),
        ('K', 'Kopi Luwak'),
        ('W', 'White Tea'),
        ('X', 'Yirgacheffe'),
        ('Y', 'Yerba Mate'),
        ('Z', 'Zen Tea'),
    ]
    name = models.CharField(max_length=100,  default='simple chai')
    image= models.ImageField(upload_to="chais/", default='default_image.jpg')
    dateadded=models.DateTimeField(timezone.now)
    type = models.CharField(max_length=2, choices=CHHAI_TYPE_CHOICE)
    description = models.TextField(max_length=500,default='')
    price = models.IntegerField(default=50)

    def __str__(self):
        return self.name

# one to many
class Reviews(models.Model):
    chai= models.ForeignKey(chaiVarity, on_delete=models.CASCADE,related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    comment = models.TextField(max_length=500)
    date_added = models.DateTimeField(timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"

# many to many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_Varieties=models.ManyToManyField(chaiVarity,related_name="stores")

    def __str__(self):
        return self.name
    
# one to one

class chaiCertificate(models.Model):
    chai = models.OneToOneField(chaiVarity, on_delete=models.CASCADE ,related_name="certificate")
    certificate_number=models.CharField(max_length=100)
    issuing_date=models.DateField(default=timezone.now)
    expiration_date=models.DateField()

    def __str__(self):
        return f"certificate for {self.chai.name}"

    



    
    


