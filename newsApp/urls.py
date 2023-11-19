from django.urls import path
from .views import news_list, news_detail, homePageView, ContactPageView

urlpatterns = [
    path('', homePageView, name='home-page'),
    path('news/', news_list, name="news-list"),
    path('<int:id>/', news_detail, name="news-detail"),
    path('contact-us/', ContactPageView.as_view(), name="contact-page"),
]