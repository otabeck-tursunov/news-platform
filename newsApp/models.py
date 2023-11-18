from django.utils import timezone
from django.db import models

class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='news')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.Draft
    )

    objects = models.Manager()
    published = PublishManager()


    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.title
