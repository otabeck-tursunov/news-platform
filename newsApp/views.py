from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from .models import Category, News
from .forms import ContactForm


def news_list(request):
    news_list = News.published.all()
    context = {
        "news_list": news_list
    }
    return render(request, 'news/news_list.html', context=context)


def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context)


def homePageView(request):
    news = News.published.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'categories': categories
    }
    return render(request, 'news/index.html', context)


# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('contact-page')
#     context = {
#         'form': form
#     }
#     return render(request, 'news/contact.html', context)

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('contact-page')
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)