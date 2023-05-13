from django.urls import path
from .import views


app_name = 'common'


urlpatterns = [
    path('', views.home_view, name='home'),
    path('category/<slug:slug>/', views.subcategory_detail, name='subcategory'),
    path('details/<slug:slug>', views.detail, name='detail'),
    path('news/', views.news_list, name='news'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('contact/', views.contact, name='contact'),
    path('set-language/', views.set_language, name='set_language')
]


