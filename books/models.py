from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
import uuid

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class ISBN(models.Model):
    book = models.OneToOneField('Book', on_delete=models.CASCADE, primary_key=True, related_name='isbn_details') 
    author_title = models.CharField(max_length=200) 

    book_title = models.CharField(max_length=200) 
    isbn_number = models.CharField(max_length=13, unique=True, editable=False) 

    def __str__(self):
        return f"{self.isbn_number} ({self.book.title})"

    def save(self, *args, **kwargs):
        if not self.isbn_number:

            self.isbn_number = str(uuid.uuid4().hex)[:13]
        super().save(*args, **kwargs)

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    categories = models.ManyToManyField(Category, related_name='books')
    title = models.CharField(
        max_length=50, 
        validators=[
            MinLengthValidator(10, message="Title must be at least 10 characters long."),
            MaxLengthValidator(50, message="Title cannot exceed 50 characters.")
        ]
    )
    description = models.TextField(null=True, blank=True)
    rate = models.PositiveSmallIntegerField(default=0) 
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('book_detail', args=[str(self.id)])


