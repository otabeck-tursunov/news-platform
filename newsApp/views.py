from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView

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
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:10]
    local_news = News.published.filter(category__name='Mahalliy').order_by('-publish_time')[:6]
    context = {
        'news_list': news_list,
        'categories': categories,
        'local_news': local_news
    }
    return render(request, 'news/index.html', context)

class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.model.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:10]
        context['local_news'] = News.published.filter(category__name='Mahalliy').order_by('-publish_time')[:6]
        return context

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
