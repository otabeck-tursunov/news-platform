# Generated by Django 4.2.7 on 2023-11-19 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0002_rename_craeted_time_news_created_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
