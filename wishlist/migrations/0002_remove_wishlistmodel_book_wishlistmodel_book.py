# Generated by Django 4.2.3 on 2024-01-17 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_borrowmodel'),
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistmodel',
            name='book',
        ),
        migrations.AddField(
            model_name='wishlistmodel',
            name='book',
            field=models.ManyToManyField(to='book.bookmodel'),
        ),
    ]
