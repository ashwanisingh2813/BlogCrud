# Generated by Django 3.2.16 on 2023-12-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_blog_banner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]