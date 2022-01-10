from django.contrib import admin

from community.models import GamesLink, Link_Group, Community_info, InglesLink, APILink, EditorLink, CursosLink, \
    RetosLink, LibrosLink, MecanografiaLink, FrameworkCssLink, TiktokLink


@admin.register(Community_info)
class Community_infoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']

@admin.register(Link_Group)
class LinkGroupsAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'created']
    readonly_fields = ('name', 'description', 'image', 'created')

@admin.register(GamesLink)
class LinkGamesAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'created']
    readonly_fields = ('name', 'description', 'image', 'created')

@admin.register(InglesLink)
class LinkInglesAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'created']
    readonly_fields = ('name', 'description', 'image', 'created')

@admin.register(APILink)
class LinkApiAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'created']
    readonly_fields = ('name', 'description', 'image', 'created')

@admin.register(EditorLink)
class LinkApiAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'created']
    readonly_fields = ('name', 'description', 'image', 'created')

@admin.register(CursosLink)
class LinkApiAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'created']
    readonly_fields = ('name', 'description', 'image', 'created')

@admin.register(RetosLink)
class LinkRetosAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'created']
    readonly_fields = ('name', 'description', 'image', 'created')

@admin.register(LibrosLink)
class LinkLibrosAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'created']
    readonly_fields = ('name', 'description', 'image', 'created')

@admin.register(MecanografiaLink)
class LinkLibrosAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'created']
    readonly_fields = ('name', 'description', 'image', 'created')

@admin.register(FrameworkCssLink)
class LinkFrameworkCssAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'created']
    readonly_fields = ('name', 'description', 'image', 'created')

@admin.register(TiktokLink)
class LinkTiktokAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'created']
    readonly_fields = ('name', 'description', 'image', 'created')