from django.urls import path

from community.views import PortadaView, LinksGroupView, GamesLinkView, LinksInglesView, LinksApiView, LinksEditorView, \
    LinksCursosView, LinksRetosView, LinksLibrosView, LinksMecanogarfiaView, LinksFrameworkCssView, LinksTiktokView, \
    LinksYouTubeView

urlpatterns = [
    path('', PortadaView.as_view(), name="home"),
    path('groups/', LinksGroupView.as_view(), name="groups"),
    path('games/', GamesLinkView.as_view(), name="games"),
    path('ingles/', LinksInglesView.as_view(), name="ingles"),
    path('api/', LinksApiView.as_view(), name="api"),
    path('editor-ide/', LinksEditorView.as_view(), name="editor"),
    path('courses/', LinksCursosView.as_view(), name="cursos"),
    path('challenges/', LinksRetosView.as_view(), name="retos"),
    path('book/', LinksLibrosView.as_view(), name="book"),
    path('typing/', LinksMecanogarfiaView.as_view(), name="typing"),
    path('framework/', LinksFrameworkCssView.as_view(), name="framework"),
    path('tiktok/', LinksTiktokView.as_view(), name="tiktok"),
    path('youtube/', LinksYouTubeView.as_view(), name="youtube"),

]
