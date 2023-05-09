from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, SubCategory, News, People, Pdf, Detail


def home_view(request):
    people = People.objects.filter(is_governor=True)
    news_people = People.objects.filter(is_governor=False)
    latest_new = News.objects.last()
    news = News.objects.order_by('-created_at').exclude(id=latest_new.id)
    uzbek_news = News.objects.filter(is_uzbek=True)
    context = {
        'governors': people,
        'news_people': news_people,
        'news': news,
        'latest_new': latest_new,
        'uzbek_news': uzbek_news,
    }
    return render(request, 'index.html', context)

def set_language(request):
    lang = request.GET.get('language', None)
    if lang is not None:
        return redirect(f'/{lang}/')
    return redirect('/')


def subcategory_detail(request, slug):
    subcategory = get_object_or_404(SubCategory.objects.select_related('category'), slug=slug)
    subcategories = SubCategory.objects.select_related('category').filter(category=subcategory.category)
    details = Detail.objects.filter(subcategory=subcategory)
    context = {
        'subcategories': subcategories,
        'details': details,
        'obj': subcategory
    }

    return render(request, 'regions.html', context)


def detail(request, slug):
    detail = get_object_or_404(Detail.objects.select_related('subcategory'), slug=slug)
    subcategories = SubCategory.objects.select_related('category').filter(category=detail.subcategory.category)
    pdf = Pdf.objects.filter(detail=detail).first()
    detail.views_count += 1
    detail.save()
    context = {
        'subcategories': subcategories,
        'detail': detail,
        'pdf': pdf
    }
    return render(request, 'detail_post.html', context)

