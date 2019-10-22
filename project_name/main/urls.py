from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from project_name.main import views

app_name = 'main'
urlpatterns = [
    path(
        route='',
        view=views.HomePageView.as_view(),
        name='home'
    ),
    path(
        route='articles/',
        view=views.ArticleCreateView.as_view(),
        name='article_create'
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)