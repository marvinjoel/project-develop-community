import datetime
from django.db import models
from django.utils import timezone

from .utils.link_data import LinkData


class Community_info(models.Model):
    title = models.CharField(verbose_name='Título',max_length=300, blank=True, null=True)
    description = models.TextField(verbose_name='Descripción', blank=True, null=True)
    r_social1 = models.CharField(verbose_name='Facebook', max_length=200, blank=True, null=True)
    r_social2 = models.CharField(verbose_name='Instagram', max_length=200, blank=True, null=True)
    r_social3 = models.CharField(verbose_name='Linkedin', max_length=200, blank=True, null=True)
    r_social4 = models.CharField(verbose_name='Telegram', max_length=200, blank=True, null=True)
    r_social5 = models.CharField(verbose_name='Twitter', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Community_info'
        verbose_name_plural = 'Community_infos'
        ordering = ['id']


class Link_Enlace(models.Model):
    whatsapp = models.CharField(verbose_name='Whatsapp', max_length=200, blank=True, null=True)
    telegram = models.CharField(verbose_name='Telegram', max_length=200, blank=True, null=True)
    discord = models.CharField(verbose_name='Discord', max_length=200, blank=True, null=True)

    def __str__(self):
        return f'Grupo: {self.whatsapp}'

    class Meta:
        verbose_name = 'Link_Enlace'
        verbose_name_plural = 'Links_Enlaces'
        ordering = ['id']


class Link_Group(models.Model):
    url = models.URLField('group url',max_length=250,unique=True,blank=False,null=False)
    name = models.CharField('group name', max_length=150, blank=True, null=True)
    description = models.TextField('group description', blank=True, null=True)
    image = models.CharField('group image', max_length=200, blank=True, null=True)
    created = models.DateTimeField('date created',auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        link_data = LinkData(self.url)
        url_data = link_data.get_data()

        self.name = url_data.get('name', None)
        self.description = url_data.get('description', None)
        self.image = url_data.get('image', None)

        super(Link_Group, self).save()


class GamesLink(models.Model):
    url = models.URLField('API url',max_length=250,unique=True,blank=False,null=False)
    name = models.CharField('API name', max_length=150, blank=True, null=True)
    description = models.TextField('API description', blank=True, null=True)
    image = models.CharField('API image', max_length=200, blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        link_data = LinkData(self.url)
        url_data = link_data.get_data()

        self.name = url_data.get('name', None)
        self.description = url_data.get('description', None)
        self.image = url_data.get('image', None)

        super(GamesLink, self).save()

class InglesLink(models.Model):
    url = models.URLField('Ingles url',max_length=250,unique=True,blank=False,null=False)
    name = models.CharField('Ingles name', max_length=150, blank=True, null=True)
    description = models.TextField('Ingles description', blank=True, null=True)
    image = models.CharField('Ingles image', max_length=200, blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        link_data = LinkData(self.url)
        url_data = link_data.get_data()

        self.name = url_data.get('name', None)
        self.description = url_data.get('description', None)
        self.image = url_data.get('image', None)

        super(InglesLink, self).save()

class APILink(models.Model):
    url = models.URLField('API url',max_length=250,unique=True,blank=False,null=False)
    name = models.CharField('API name', max_length=150, blank=True, null=True)
    description = models.TextField('API description', blank=True, null=True)
    image = models.CharField('API image', max_length=200, blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        link_data = LinkData(self.url)
        url_data = link_data.get_data()

        self.name = url_data.get('name', None)
        self.description = url_data.get('description', None)
        self.image = url_data.get('image', None)

        super(APILink, self).save()

class EditorLink(models.Model):
    url = models.URLField('Editor url',max_length=250,unique=True,blank=False,null=False)
    name = models.CharField('Editor name', max_length=150, blank=True, null=True)
    description = models.TextField('Editor description', blank=True, null=True, max_length=250)
    image = models.CharField('Editor image', max_length=200, blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        link_data = LinkData(self.url)
        url_data = link_data.get_data()

        self.name = url_data.get('name', None)
        self.description = url_data.get('description', None)
        self.image = url_data.get('image', None)

        super(EditorLink, self).save()

class CursosLink(models.Model):
    url = models.URLField('Cursos url',max_length=250,unique=True,blank=False,null=False)
    name = models.CharField('Cursos name', max_length=150, blank=True, null=True)
    description = models.TextField('Cursos description', blank=True, null=True, max_length=250)
    image = models.CharField('Cursos image', max_length=200, blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        link_data = LinkData(self.url)
        url_data = link_data.get_data()

        self.name = url_data.get('name', None)
        self.description = url_data.get('description', None)
        self.image = url_data.get('image', None)

        super(CursosLink, self).save()

class RetosLink(models.Model):
    url = models.URLField('Retos url',max_length=250,unique=True,blank=False,null=False)
    name = models.CharField('Retos name', max_length=150, blank=True, null=True)
    description = models.TextField('Retos description', blank=True, null=True, max_length=250)
    image = models.CharField('Retos image', max_length=200, blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        link_data = LinkData(self.url)
        url_data = link_data.get_data()

        self.name = url_data.get('name', None)
        self.description = url_data.get('description', None)
        self.image = url_data.get('image', None)

        super(RetosLink, self).save()

class LibrosLink(models.Model):
    url = models.URLField('Libros url',max_length=250,unique=True,blank=False,null=False)
    name = models.CharField('Libros name', max_length=150, blank=True, null=True)
    description = models.TextField('Libros description', blank=True, null=True, max_length=250)
    image = models.CharField('Libros image', max_length=200, blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        link_data = LinkData(self.url)
        url_data = link_data.get_data()

        self.name = url_data.get('name', None)
        self.description = url_data.get('description', None)
        self.image = url_data.get('image', None)

        super(LibrosLink, self).save()

class MecanografiaLink(models.Model):
    url = models.URLField('Mecanografia url',max_length=250,unique=True,blank=False,null=False)
    name = models.CharField('Mecanografia name', max_length=150, blank=True, null=True)
    description = models.TextField('Mecanografia description', blank=True, null=True, max_length=250)
    image = models.CharField('Mecanografia image', max_length=200, blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        link_data = LinkData(self.url)
        url_data = link_data.get_data()

        self.name = url_data.get('name', None)
        self.description = url_data.get('description', None)
        self.image = url_data.get('image', None)

        super(MecanografiaLink, self).save()

class FrameworkCssLink(models.Model):
    url = models.URLField('Framework url',max_length=250,unique=True,blank=False,null=False)
    name = models.CharField('Framework name', max_length=150, blank=True, null=True)
    description = models.TextField('Framework description', blank=True, null=True, max_length=250)
    image = models.CharField('Framework image', max_length=200, blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

    def save(self):
        link_data = LinkData(self.url)
        url_data = link_data.get_data()

        self.name = url_data.get('name', None)
        self.description = url_data.get('description', None)
        self.image = url_data.get('image', None)

        super(FrameworkCssLink, self).save()