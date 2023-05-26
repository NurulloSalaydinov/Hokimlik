from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .models import Category, SubCategory, News, People, Pdf, Detail, PdfNews, Tag, SubTag
from .forms import ContactForm


def home_view(request):
    people = People.objects.filter(is_governor=True)
    news_people = People.objects.filter(is_governor=False)
    latest_new = News.objects.last()
    news = News.objects.order_by('-created_at').exclude(id=latest_new.id)
    uzbek_news = News.objects.filter(is_uzbek=True)
    tag = Tag.objects.last()
    subtag_tag = SubTag.objects.filter(tag=tag)
    tags = Tag.objects.exclude(id=tag.id)
    context = {
        'governors': people,
        'news_people': news_people,
        'news': news,
        'latest_new': latest_new,
        'uzbek_news': uzbek_news,
        'tag': tag,
        'tags': tags,
        'subtag_tag': subtag_tag
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
    news = News.objects.filter(categories__in=[subcategory.id])
    context = {
        'subcategories': subcategories,
        'details': details,
        'obj': subcategory,
        'news': news
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


def news_list(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news.html', context)


def news_detail(request, slug):
    detail = get_object_or_404(News, slug=slug)
    pdf = PdfNews.objects.filter(news=detail).first()
    detail.views_count += 1
    detail.save()
    context = {
        'detail': detail,
        'pdf': pdf
    }
    return render(request, 'detail_news.html', context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Muvaffaqiyatli yuborildi, tez orada siz bilan bog'lanishadi!"))
            return redirect('/')
    return render(request, 'contact.html', {'form': form})


def search_results(request):
    q = request.GET.get('q', '')
    detail_list = Detail.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    news_list = News.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    subcategories = SubCategory.objects.all()[:6]
    context = {
        'detail_list': detail_list,
        'news_list': news_list,
        'subcategories': subcategories
    }
    return render(request, 'search_results.html', context)
