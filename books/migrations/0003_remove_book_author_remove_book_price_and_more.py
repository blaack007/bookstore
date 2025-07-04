# Generated by Django 5.2.3 on 2025-06-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_book_isbn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='rate',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
