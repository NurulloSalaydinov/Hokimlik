from modeltranslation.translator import register, TranslationOptions
from .models import People, Category, SubCategory, Detail, News, Tag, SubTag


@register(People)
class PeopleTranslationOptions(TranslationOptions):
    fields = ('who', 'content')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(SubTag)
class SubTagTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Detail)
class DetailTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')



