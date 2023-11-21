from django.urls import path
from .views import news_list, news_detail, HomePageView, ContactPageView, handler404, newsByCategories, about, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('yangiliklar/', news_list, name="news-list"),
    path('yangiliklar/<slug:news>/', news_detail, name="news-detail"),
    path('yangiliklar/<slug:news>/tahrirlash/', NewsUpdateView.as_view(), name="news-update"),
    path('yangiliklar/<slug:news>/o\'chirish/', NewsDeleteView.as_view(), name="news-delete"),
    path('aloqa/', ContactPageView.as_view(), name="contact-page"),
    path('kategoriyalar/<slug:category>/', newsByCategories, name="category-news"),
    path('biz-haqimizda/', about, name="about-page"),
    path('sahifa-topilmadi/', handler404, name='handler404')
]
