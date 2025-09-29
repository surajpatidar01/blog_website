from django.contrib import admin
from . models import Category,Blogs
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name', 'created_at', 'updated_at')

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'created_at', 'updated_at','author','blog_image','status','is_featured')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['id','title','author','category__category_name','created_at','updated_at']
    list_editable = ('is_featured',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Blogs,BlogsAdmin)
