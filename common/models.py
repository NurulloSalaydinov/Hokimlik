from django.shortcuts import reverse
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

    def get_subcategory(self):
        subcategories = SubCategory.objects.filter(category=self)
        return subcategories

    def get_absolute_url(self):
        return "/hello"
        # return reverse("model_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        verbose_name = 'Turkum'
        verbose_name_plural = 'Turkumlar'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Turkum')
    title = models.CharField(verbose_name='Sarlavha', max_length=255)
    slug = models.SlugField(verbose_name='*')

    def get_absolute_url(self):
        return reverse('common:subcategory', kwargs={'slug': self.slug})

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

    def get_absolute_url(self):
        return reverse("common:detail", kwargs={"slug": self.slug})
    

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
    image = models.ImageField(upload_to='news_images/%y/%m/%d/', verbose_name='Rasm', blank=True, null=True)
    content = RichTextField(verbose_name='Kontent')
    views_count = models.PositiveIntegerField(verbose_name='Korilganlar soni', default=0)
    is_uzbek = models.BooleanField(verbose_name='Ozbekiston yangiligimi?', default=True)
    created_at = models.DateField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('common:news_detail', kwargs={'slug': self.slug})
        # return reverse("model_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'


class PdfNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Qaysi yangilik uchun?')
    title = models.CharField(verbose_name='PDF uchun sarlavha', max_length=255)
    pdf_file = models.FileField(verbose_name='Fayl', upload_to='pdf/%y/%m/%d/')

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        verbose_name = 'PDF Fayl (Yangiliklar uchun)'
        verbose_name_plural = 'PDF Fayllar (Yangiliklar uchun)'


class Contact(models.Model):
    PROVINCES = (
        ('Andijon viloyati', 'Andijon viloyati'),
        ('Toshkent viloyati', 'Toshkent viloyati'),
        ('Buhoro viloyati', 'Buhoro viloyati'),
        ('Jizzax viloyati', 'Jizzax viloyati'),
        ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'),
        ('Namangan viloyati', 'Namangan viloyati'),
        ('Samarqand viloyati', 'Samarqand viloyati'),
        ('Surxondaryo viloyati', 'Surxondaryo viloyati'),
        ('Sirdaryo viloyat', 'Sirdaryo viloyat'),
        ('Farg`ona viloyati', 'Farg`ona viloyati'),
        ('Xorazm viloyati', 'Xorazm viloyati'),
        ('Navoi viloyati', 'Navoi viloyati'),
        ('Qoraqalpog`iston viloyati', 'Qoraqalpog`iston viloyati'),
    )
    WORKERTYPES = (
        ('Jismoniy shaxs', 'Jismoniy shaxs'),
        ('Yakka tartibdagi tadbirkor', 'Yakka tartibdagi tadbirkor'),
        ('Yuridik shaxs', 'Yuridik shaxs'),
    )
    GENDER = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    )
    JOB = (
        ('Ish bilan taminlangan', 'Ish bilan taminlangan'),
        ('Ishsiz', 'Ishsiz'),
        ('Nafaqada', 'Nafaqada'),
        ('Talaba', 'Talaba'),
    )
    full_name = models.CharField(verbose_name='F.I.SH', max_length=255)
    businessman = models.CharField(verbose_name='Yuridik shaxs nomi(Tadbirkor)', max_length=255)
    email = models.EmailField(verbose_name='Elektron manzil', max_length=255)
    phone = models.CharField(verbose_name='Telefon raqam', max_length=50)
    province_select = models.CharField(verbose_name='Viloyat', max_length=255, choices=PROVINCES)
    province = models.CharField(verbose_name='Viloyat', max_length=255)
    address =  models.CharField(verbose_name='Manzil', max_length=255)
    work_type = models.CharField(verbose_name='Shaxs', max_length=255, choices=WORKERTYPES)
    gender = models.CharField(verbose_name='Jinsi', max_length=255, choices=GENDER)
    birthday = models.CharField(verbose_name='Tugilgan kun', max_length=255)
    job = models.CharField(verbose_name='Hozirgi kasb holati', max_length=255, choices=JOB)
    description = models.CharField(verbose_name='Murojaatnoma', max_length=500)
    date = models.DateTimeField(verbose_name='Sana', auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}"

