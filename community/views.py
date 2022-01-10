from re import template
from django.views.generic import TemplateView
from community.models import Community_info, Link_Group, GamesLink, InglesLink, APILink, EditorLink, CursosLink, \
    RetosLink, LibrosLink, MecanografiaLink, FrameworkCssLink


class PortadaView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio'
        context['comment'] = Community_info.objects.all()
        return context


class GamesLinkView(TemplateView):
    template_name = 'games.html'

    def get_context_data(self, **kwargs):
        context = super(GamesLinkView, self).get_context_data(**kwargs)
        context['title'] = 'Games'
        context['games'] = GamesLink.objects.all()
        return context

class LinksGroupView(TemplateView):
    template_name = 'linkgroups.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = Link_Group.objects.all()
        return context

class LinksInglesView(TemplateView):
    template_name = 'ingles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingles'] = InglesLink.objects.all()
        return context

class LinksApiView(TemplateView):
    template_name = 'api.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['api'] = APILink.objects.all()
        return context

class LinksEditorView(TemplateView):
    template_name = 'editor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['editor'] = EditorLink.objects.all()
        return context

class LinksCursosView(TemplateView):
    template_name = 'cursos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = CursosLink.objects.all()
        return context

class LinksRetosView(TemplateView):
    template_name = 'retos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['retos'] = RetosLink.objects.all()
        return context

class LinksLibrosView(TemplateView):
    template_name = 'libros.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libros'] = LibrosLink.objects.all()
        return context

class LinksMecanogarfiaView(TemplateView):
    template_name = 'mecanografia.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mecanografia'] = MecanografiaLink.objects.all()
        return context

class LinksFrameworkCssView(TemplateView):
    template_name = 'framework.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['framework'] = FrameworkCssLink.objects.all()
        return context



