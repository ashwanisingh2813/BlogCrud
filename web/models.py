from django.db import models

# Create your models here.

class Contactus(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=150)

    class Meta:
        db_table='contactus'

class Blog(models.Model):
    categories=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    description=models.TextField()
    writer=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='blog/')
    banner_image=models.ImageField(upload_to='banner/',null=True)
    
    class Meta:
        db_table='blog'

class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    date=models.DateTimeField(auto_now_add=True,null=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    comments=models.TextField()

    class Meta:
        db_table='comments'