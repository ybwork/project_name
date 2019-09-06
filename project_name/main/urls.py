from django.urls import path

from project_name.main import views

app_name = 'main'
urlpatterns = [
    path(
        route='',
        view=views.HomePageView.as_view(),
        name='home'
    )
]