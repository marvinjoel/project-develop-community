# Generated by Django 3.2.8 on 2022-01-02 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_editorlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursosLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=250, unique=True, verbose_name='Cursos url')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Cursos name')),
                ('description', models.TextField(blank=True, max_length=250, null=True, verbose_name='Cursos description')),
                ('image', models.CharField(blank=True, max_length=200, null=True, verbose_name='Cursos image')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
    ]