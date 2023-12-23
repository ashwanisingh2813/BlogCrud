from django.contrib import admin
from web import models

# Register your models here.
@admin.register(models.Contactus)
class RegisterAdmin(admin.ModelAdmin):
    list_display=['id','name','email','subject','message']

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['id','categories','title','description','writer','date','image']

@admin.register(models.Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display=['blog','name','email','subject','comments']
