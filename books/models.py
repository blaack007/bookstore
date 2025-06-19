from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    rate = models.PositiveSmallIntegerField(default=0) # Assuming rate is 0-5 or similar, adjust if needed
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('book_detail', args=[str(self.id)])
