from datetime import datetime

from .models import News, Category


def latest_news(request):
    latest_news = News.published.all().order_by('-publish_time')[:10]
    context = {
        'latest_news': latest_news,
        'now_time': datetime.now().strftime(" %B %d, %Y"),
        'top_categories': Category.objects.all()[::-1][:10]
    }

    return context
