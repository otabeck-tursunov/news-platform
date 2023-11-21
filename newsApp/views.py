from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView

from .models import Category, News
from .forms import ContactForm


def news_list(request):
    news_list = News.published.all()
    context = {
        "news_list": news_list
    }
    return render(request, 'news/news_list.html', context=context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
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
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:5]
        context['local_news'] = News.published.filter(category__name='Mahalliy').order_by('-publish_time')[:6]
        context['tech_news'] = News.published.filter(category__name='Texnologiya').order_by('-publish_time')[:6]
        context['foreign_news'] = News.published.filter(category__name='Xorij').order_by('-publish_time')[:6]
        context['sport_news'] = News.published.filter(category__name='Sport').order_by('-publish_time')[:6]
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


def newsByCategories(request, category):
    context = {
        'category': get_object_or_404(Category, slug=category),
        'category_news': News.objects.filter(category__slug=category).order_by('-publish_time')
    }
    return render(request, 'news/news-by-categories.html', context)


def about(request):
    return render(request, 'news/biz_haqimizda.html')


def handler404(request, exception=None):
    news_list = News.published.all().order_by('-publish_time')[:5]
    context = {
        'news_list': news_list
    }
    return render(request, 'news/404.html', context=context, status=404)


class NewsUpdateView(UpdateView):
    model = News
    fields = ('title', 'body', 'image', 'category', 'status')
    template_name = 'crud/news-edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('news')
        context['news'] = self.model.objects.get(slug=slug)
        return context

    def get_object(self, queryset=None):
        slug = self.kwargs.get('news')
        return get_object_or_404(News, slug=slug)


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/news-delete.html'
    success_url = reverse_lazy('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('news')
        context['news'] = self.model.objects.get(slug=slug)
        return context

    def get_object(self, queryset=None):
        slug = self.kwargs.get('news')
        return get_object_or_404(News, slug=slug)
