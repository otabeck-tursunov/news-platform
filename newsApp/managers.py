from django.db import models
from .models import News

# class PublishManager(models.Manager)
#      def get_queryset(self):
#           return super().get_queryset().filter(status=News.status.Published)