"""BlogingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('blog/',views.blog,name='blog'),

    path('addNewBlog/',views.addNewBlog,name='addnewblog'),
    path('showData/',views.showData,name='showdata'),
    path('editBlog/<int:id>/',views.editBlog,name='editblog'),
    path('deleteBlog/<int:id>/',views.deleteBlog,name='deleteblog'),

    path('postdetails/<int:blog_id>/', views.postDetails, name='postdetails'),


    path('contact/',views.contact,name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
