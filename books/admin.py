from django.contrib import admin
from .models import Book, Category, ISBN

# Register your models here.

class ISBNInline(admin.StackedInline):
    model = ISBN
    can_delete = False
    verbose_name_plural = 'ISBN Details'
    readonly_fields = ('isbn_number',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'display_categories', 'rate', 'views')
    list_filter = ('user', 'categories', 'rate')
    search_fields = ('title', 'description', 'user__username', 'categories__name') 
    inlines = [ISBNInline]

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    display_categories.short_description = 'Categories'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ISBN)
class ISBNAdmin(admin.ModelAdmin):
    list_display = ('isbn_number', 'book_title', 'author_title')
    search_fields = ('isbn_number', 'book__title', 'author_title')
    readonly_fields = ('isbn_number', 'book_title') 
