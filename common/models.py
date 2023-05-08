from django.db import models
from ckeditor.fields import RichTextField



class People(models.Model):
    image = models.ImageField(verbose_name='Rasm', upload_to='government/%y/%m/%d/')
    who = models.CharField(verbose_name='Kimligi?', max_length=255)
    content = RichTextField(verbose_name='Malumot')
    is_governor = models.BooleanField(verbose_name='Rahbar?', default=True)

    def __str__(self):
        return f"{self.id} {self.who}"

    class Meta:
        verbose_name = 'Rahbariyat'
        verbose_name_plural = 'Rahbariyatlar'


class Category(models.Model):
    title = models.CharField(verbose_name='Sarlavha', max_length=255)
    slug = models.SlugField(verbose_name='*')

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        verbose_name = 'Turkum'
        verbose_name_plural = 'Turkumlar'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Turkum')
    title = models.CharField(verbose_name='Sarlavha', max_length=255)
    slug = models.SlugField(verbose_name='*')

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        verbose_name = 'Qoshimcha turkum'
        verbose_name_plural = 'Qoshimcha turkumlar'


class Detail(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Qoshimcha turkum')
    title = models.CharField(verbose_name='Sarlavha', max_length=255)
    slug = models.SlugField(verbose_name='*')
    image = models.ImageField(upload_to='detail_images/%y/%m/%d/', verbose_name='Rasm', blank=True, null=True)
    content = RichTextField(verbose_name='Kontent')
    views_count = models.PositiveIntegerField(verbose_name='Korilganlar soni', default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        verbose_name = 'Malumot'
        verbose_name_plural = 'Malumotlar'


class Pdf(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, verbose_name='Qaysi malumot uchun?')
    title = models.CharField(verbose_name='PDF uchun sarlavha', max_length=255)
    pdf_file = models.FileField(verbose_name='Fayl', upload_to='pdf/%y/%m/%d/')

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        verbose_name = 'PDF Fayl'
        verbose_name_plural = 'PDF Fayllar'


class News(models.Model):
    title = models.CharField(verbose_name='Yangilik uchun sarlavha', max_length=255)
    slug = models.SlugField(verbose_name='*')
    content = RichTextField(verbose_name='Kontent')
    views_count = models.PositiveIntegerField(verbose_name='Korilganlar soni', default=0)
    is_uzbek = models.BooleanField(verbose_name='Ozbekiston yangiligimi?', default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
