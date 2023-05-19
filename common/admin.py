from django.contrib import admin
from .models import (People,
Category, 
SubCategory, 
Detail, 
News,
Pdf, 
PdfNews, 
Contact,
SubTag, 
Tag
)


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'who', 'is_governor')
    list_display_links = ('id', 'who')
    list_editable = ('is_governor',)
    list_filter = ('is_governor',)
    search_fields = ('who', 'content')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}



@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    list_filter = ('category',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'views_count', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('subcategory',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Pdf)
class PdfAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    list_filter = ('detail',)
    search_fields = ('title',)


@admin.register(PdfNews)
class PdfNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    list_filter = ('news',)
    search_fields = ('title',)



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'views_count', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('is_uzbek',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'date')
    list_display_links = ('full_name',)

    search_fields = ('full_name', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


@admin.register(SubTag)
class SubTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tag')
    list_display_links = ('id', 'title', 'tag')
    list_filter = ('tag', )
    search_fields = ('title', 'tag')
