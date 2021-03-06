# Generated by Django 3.2.8 on 2021-12-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_gameslink_link_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='InglesLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=250, unique=True, verbose_name='Ingles url')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Ingles name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Ingles description')),
                ('image', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ingles image')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
    ]
