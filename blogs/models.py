from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify  # ✅ import slugify

# Category model
class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

# Status choices
STATUS_CHOICE = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

# Blogs model
class Blogs(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=2000)
    blog_body = models.TextField(max_length=3000)
    status = models.CharField(max_length=100, choices=STATUS_CHOICE, default='draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title

    # ✅ Auto-generate slug from title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
