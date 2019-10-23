from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from project_name.main import views
from project_name.main.views import ArticleListView

app_name = 'main'
urlpatterns = [
    path(
        route='',
        view=views.HomePageView.as_view(),
        name='home'
    ),
    path(
        route='articles/create',
        view=views.ArticleCreateView.as_view(),
        name='article_create'
    ),
    path(
        route='articles/list',
        view=ArticleListView.as_view(),
        name='article_list'
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)